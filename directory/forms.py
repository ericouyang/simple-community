from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User
from models import Education, Link, Profile

ProfileInlineFormSet = inlineformset_factory(User, Profile)
EducationInlineFormSet = inlineformset_factory(User, Education, extra=1)
LinkInlineFormSet = inlineformset_factory(User, Link, extra=1)
