from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages import views

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from .views import HomePageView

handler403 = 'simple_community.views.permission_denied'

urlpatterns = [
    # Examples:
    # url(r'^$', 'simple_community.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePageView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^directory/', include('directory.urls')),
    url(r'^accounts/signup/$', RedirectView.as_view(url='/')),
    url(r'^accounts/', include('allauth.urls'))

    url(r'^(?P<url>.*/)$', views.flatpage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
