from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.core.urlresolvers import reverse

class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name="profile")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    university = models.CharField(max_length=50, blank=True)
    graduation_year = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)
    degree_subject = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        # return reverse('people.profile', args=[self.user.username])
        return '/%s' % self.user.username

    def __str__(self):  
          return "%s's profile" % self.user

    @classmethod
    def _create(cls, sender, instance, created, **kwargs):  
        if created:  
           profile, created = cls.objects.get_or_create(user=instance)

    description = """
# header 1

paragraph 1

template tag >>{{ user }}<<
    """

post_save.connect(UserProfile._create, sender=User)