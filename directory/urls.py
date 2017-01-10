from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from views import UserListView, UserDetailView, UserUpdateView, \
    RedirectUserDetailView

urlpatterns = [
    url(r'^$',
        login_required(UserListView.as_view())
    ),
    url(r'^me$', RedirectUserDetailView.as_view(), name='current-user-detail'),
    url(
        r'^(?P<slug>[\w]+)$',
        login_required(UserDetailView.as_view()),
        name='user-detail'
    ),
    url(
        r'^(?P<slug>[\w]+)/update$',
        login_required(UserUpdateView.as_view()),
        name='user-update'
    )
]
