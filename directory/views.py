from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect

from forms import EducationInlineFormSet, LinkInlineFormSet, \
    ProfileInlineFormSet


class UserListView(ListView):
    model = User
    template_name = 'directory/user_list'


class UserDetailView(DetailView):
    model = User
    template_name = 'directory/user_detail'


class RedirectUserDetailView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('user-detail', args=[self.request.user.id])


class UserUpdateView(UpdateView):
    model = User
    template_name = 'directory/user_update'
    fields = [
        'first_name',
        'last_name',
    ]

    def dispatch(self, *args, **kwargs):
        if not (self.request.user.id == self.get_object().id \
           or self.request.user.is_staff):
            raise PermissionDenied
        return super(UserUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['profile_form'] = ProfileInlineFormSet(
                self.request.POST, self.request.FILES,
                instance=self.object
            )
            context['education_form'] = EducationInlineFormSet(
                self.request.POST,
                instance=self.object
            )
            context['link_form'] = LinkInlineFormSet(
                self.request.POST,
                instance=self.object
            )
        else:
            context['profile_form'] = ProfileInlineFormSet(instance=self.object)
            context['education_form'] = EducationInlineFormSet(instance=self.object)
            context['link_form'] = LinkInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        education_form = context['education_form']
        link_form = context['link_form']
        if form.is_valid() and profile_form.is_valid() \
           and education_form.is_valid() and link_form.is_valid():
            form.save()
            profile_form.save()
            education_form.save()
            link_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
