"""
Definition of urls for QukiHub.
사이트에 접속하면 Django는 가장먼저 urlpatterns를 보게됨.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views

from django.contrib import admin
# from django.conf.urls import include
# admin.autodiscover()

import app.forms
import app.views

urlpatterns = [  # 서버에 요청이 오면 누가 어떻게 처리할지 담당자를 처리

    # url(주소, 접속시 누가 처리할 것인지)
    url(r'^admin/', admin.site.urls),
    url(r'^$', app.views.Home.as_view(), name='home'),
    url(r'^contact$', app.views.Contact.as_view(), name='contact'),
    url(r'^about', app.views.About.as_view(), name='about'),
    url(r'^portfolio', app.views.Portfolio.as_view(), name='portfolio'),
    url(r'^activity', app.views.ActivityList.as_view(), name='activity_list'),
    url(r'^post/(?P<parent>\S+)/(?P<child>\S+)$', app.views.PostCategorizedList.as_view(), name='post_categorized_list'),
    url(r'^post/(?P<slug>\S+)$', app.views.PostItem.as_view(), name="post_item"),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'layout_index': 'auth',
                    'year': datetime.now().year,
                },
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^onlyadmin$', app.views.only_admin, name='onlyadmin'),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

]
