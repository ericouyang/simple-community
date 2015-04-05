from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.db.models import CharField

from django.http import HttpResponseRedirect

import django_filters
from django_filters.views import FilterView

from forms import EducationInlineFormSet, LinkInlineFormSet, \
    ProfileInlineFormSet, InlineFormSetHelper


class UserFilter(django_filters.FilterSet):
    filter_overrides = {
        CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_type': 'icontains',
            }
        }
    }
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile__state', 'profile__town_city', 'education__class_year', 'education__school__name']
        order_by = ['last_name']


class UserListView(FilterView):
    model = User
    filterset_class = UserFilter
    template_name = 'directory/user_list'


class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'directory/user_detail'


class RedirectUserDetailView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('user-detail', args=[self.request.user.username])


# see http://brantsteen.com/blog/django-adding-inline-formset-rows-without-javascript/
class UserUpdateView(UpdateView):
    model = User
    slug_field = 'username'
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

        if 'form' in kwargs:
            if 'add_education' in self.request.POST:
                self.request.POST['education_set-TOTAL_FORMS'] = \
                    int(self.request.POST['education_set-TOTAL_FORMS']) + 1
            elif 'add_link' in self.request.POST:
                self.request.POST['link_set-TOTAL_FORMS'] = \
                    int(self.request.POST['link_set-TOTAL_FORMS']) + 1
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
        context['form_helper'] = InlineFormSetHelper()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        education_form = context['education_form']
        link_form = context['link_form']
        if 'add_education' not in self.request.POST and \
           'add_link' not in self.request.POST and \
           form.is_valid() and profile_form.is_valid() \
           and education_form.is_valid() and link_form.is_valid():
            form.save()
            profile_form.save()
            education_form.save()
            link_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
