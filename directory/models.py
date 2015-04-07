from django.db import models
from django.contrib.auth.models import User

from localflavor.us.models import USStateField, PhoneNumberField

import markdown
import bleach


class Profile(models.Model):
    about = models.TextField(
        blank=True
    )
    town_city = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Town/City'
    )
    state = USStateField(
        blank=True
    )
    phone_number = PhoneNumberField(
        blank=True
    )
    profile_image = models.ImageField(
        blank=True,
        upload_to='users/profile_images'
    )

    # relationships
    user = models.OneToOneField(User)

    # timestamps
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def get_location(self):
        return ', '.join([self.town_city, self.state])

    def get_about_as_html(self):
        return bleach.clean(
            markdown.markdown(self.about),
            tags=bleach.ALLOWED_TAGS + ['p']
    )


class Education(models.Model):
    class_year = models.PositiveIntegerField()

    # relationships
    user = models.ForeignKey(User)
    school = models.ForeignKey('School')

    degree = models.CharField(
        max_length=100,
        blank=True
    )

    # timestamps
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __unicode__(self):
        return " '".join([self.school.name, str(self.class_year % 100)])

    class Meta:
        ordering = ('-class_year',)


class Link(models.Model):
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    LINKEDIN = 'linkedin'
    PERSONAL = 'personal'
    OTHER = 'other'

    EDUCATION_TYPE_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (LINKEDIN, 'Linkedin'),
        (PERSONAL, 'Personal'),
        (OTHER, 'Other'),
    )

    type = models.CharField(
        max_length=20,
        choices=EDUCATION_TYPE_CHOICES
    )

    url = models.URLField()

    # relations
    user = models.ForeignKey(User)

    # timestamps
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __unicode__(self):
        return u'%s - %s' % (self.type, self.url)

    def get_icon_class(self):
        if self.type == self.FACEBOOK:
            return 'fa-facebook'
        elif self.type == self.TWITTER:
            return 'fa-twitter'
        elif self.type == self.LINKEDIN:
            return 'fa-linkedin'
        elif self.type == self.PERSONAL:
            return 'fa-globe'
        elif self.type == self.OTHER:
            return 'fa-link'

    def get_display_text(self):
        if self.type == self.FACEBOOK:
            return "Facebook"
        elif self.type == self.TWITTER:
            return "Twitter"
        elif self.type == self.LINKEDIN:
            return "LinkedIn"
        elif self.type == self.PERSONAL:
            return "Personal site"
        elif self.type == self.OTHER:
            return self.url

    class Meta:
        ordering = ('type',)


class School(models.Model):
    HIGH_SCHOOL = 'high_school'
    COLLEGE = 'college'
    GRADUATE_SCHOOL = 'graduate_school'

    EDUCATION_TYPE_CHOICES = (
        (HIGH_SCHOOL, 'High School'),
        (COLLEGE, 'College'),
        (GRADUATE_SCHOOL, 'Graduate School'),
    )

    type = models.CharField(
        max_length=20,
        choices=EDUCATION_TYPE_CHOICES
    )

    name = models.CharField(
        max_length=100
    )

    # timestamps
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
