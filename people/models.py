import re

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

_markdown_help_text = 'Parsed as Markdown with inline HTML. See <a href="https://daringfireball.net/projects/markdown/">https://daringfireball.net/projects/markdown/</a>.'

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
    description = models.TextField(blank=True, help_text=_markdown_help_text)

    def get_absolute_url(self):
        # return reverse('people.profile', args=[self.user.username])
        return '/%s' % self.user.username

    def __str__(self):  
          return "%s's profile" % self.user

    @classmethod
    def _create(cls, sender, instance, created, **kwargs):  
        if created:  
           profile, created = cls.objects.get_or_create(user=instance)

post_save.connect(UserProfile._create, sender=User)

_project_name_regex = re.compile(r'^[a-z\-]+$')

class Project(models.Model):

    user = models.ForeignKey(User, related_name="projects")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(r'^[0-9a-zA-Z\-_]*$', 'Only alphanumeric characters, - and _ are allowed.')
        ]
    )
    summary = models.TextField()
    description = models.TextField(help_text=_markdown_help_text)

    def get_absolute_url(self):
        # return reverse('people.project', args=[self.user.username, self.name])
        return '/%s/%s' % (self.user.username, self.name)

    def __str__(self):  
          return self.name