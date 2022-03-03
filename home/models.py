from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=True, null=True)
    bio = models.CharField(max_length=255, default=True, null=True)
    #gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    profile_image = models.ImageField(default='images/default_avatar_profile.jpg', upload_to='images', null=True,
                                      blank=True)
    country = models.CharField(max_length=255, default=True, null=True)

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
