from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

from django.contrib.flatpages.models import FlatPage

def permission_denied(request):
    return render_to_response(
        'errors/permission_denied',
        context_instance=RequestContext(request)
    )

class HomePageView(TemplateView):
    template_name = "pages/home.haml"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        try:
            fp = FlatPage.objects.get(url='/')
            context['title'] = fp.title
            context['content'] = fp.content
        except Exception:
            context['title'] = 'Welcome to Simple Community'
            context['content'] = "It's simply a community"
        return context

    

    