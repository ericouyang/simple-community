from django import forms
from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User
from models import Education, Link, Profile

from crispy_forms.helper import FormHelper
from localflavor.us.forms import USStateField

ProfileInlineFormSet = inlineformset_factory(User, Profile, exclude=(), can_delete=False)
EducationInlineFormSet = inlineformset_factory(User, Education, exclude=(), extra=0)
LinkInlineFormSet = inlineformset_factory(User, Link, exclude=(), extra=0)


class InlineFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InlineFormSetHelper, self).__init__(*args, **kwargs)
        self.template = 'bootstrap/table_inline_formset.html'
        self.form_tag = False

class UserSearchForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        required=False
    )
    last_name = forms.CharField(
        label='Last Name',
        required=False
    )
    profile__town_city = forms.CharField(
        label='Town/City',
        required=False
    )

    profile__state = USStateField(
        label='State',
        required=False
    )

    education__school__name = forms.CharField(
        label='School Name',
        required=False
    )
    education__class_year = forms.CharField(
        label='Class Year',
        required=False
    )