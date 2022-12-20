from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        #newly created user automatically gets profile created and linked to user
        user_profile = Profile(user=instance)
        user_profile.save()
        #new user automatically follows their own profile
        user_profile.follows.add(instance.profile)
        user_profile.save()
# signal executes create profile - refactored to use receiver decorator.
#post_save.connect(create_profile, sender=User)

