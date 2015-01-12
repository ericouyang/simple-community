from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User

from forms import EducationInlineFormSet, LinkInlineFormSet, \
    ProfileInlineFormSet


class UserListView(ListView):
    model = User
    template_name = 'directory/user_list'


class UserDetailView(DetailView):
    model = User
    template_name = 'directory/user_detail'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'directory/user_update'
    fields = [
        'first_name',
        'last_name',
    ]
    success_url = '/directory'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['profile_form'] = ProfileInlineFormSet(instance=self.object)
        context['education_form'] = EducationInlineFormSet(instance=self.object)
        context['link_form'] = LinkInlineFormSet(instance=self.object)
        return context
