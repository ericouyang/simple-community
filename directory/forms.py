from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User
from models import Education, Link, Profile

from crispy_forms.helper import FormHelper

ProfileInlineFormSet = inlineformset_factory(User, Profile, can_delete=False)
EducationInlineFormSet = inlineformset_factory(User, Education, extra=0)
LinkInlineFormSet = inlineformset_factory(User, Link, extra=0)


class InlineFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InlineFormSetHelper, self).__init__(*args, **kwargs)
        self.template = 'bootstrap/table_inline_formset.html'
        self.form_tag = False
