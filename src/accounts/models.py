from django.conf import settings
from django.db import models

# Create your models here.

class UserProfileManager(models.Manager):
    def all(self):
        qs = self.get_queryset().all()
        print(dir(self))
        print(self.instance) # user
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.PROTECT) # user.profile   
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')    
    # user.profile.following - all users following
    # user.followed_by -- users that follow me - reverse relationship

    objects = UserProfileManager() # UserProfile.objects.all()
    # abc = UserProfileManager() # UserProfile.abc.all()

    def __str__(self):
        return str(self.following.all().count())
          
