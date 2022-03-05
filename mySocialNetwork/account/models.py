from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.from_user} following {self.to_user}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    biography = models.TextField(blank=True, null=True)

    def followers_counts(self):
        return self.user.followings.count()

    def followings_counts(self):
        return self.user.followers.count()

    def posts_counts(self):
        return self.user.posts.count()