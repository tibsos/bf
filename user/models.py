from django.db import models as m

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(m.Model):

    user = m.OneToOneField(User, on_delete = m.CASCADE, related_name = 'p')

    name = m.TextField()
    initials = m.CharField(max_length = 3)

    dark = m.BooleanField(default = False)

    premium = m.BooleanField(default = False)


    def __str__(self):

        return f"{self.name} | {self.user.username}"

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        Profile.objects.create(user = instance)
    