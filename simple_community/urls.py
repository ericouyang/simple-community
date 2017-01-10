from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

handler403 = 'simple_community.views.permission_denied'

urlpatterns = [
    # Examples:
    # url(r'^$', 'simple_community.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='pages/home.haml')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^directory/', include('directory.urls')),
    url(r'^accounts/', include('allauth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
