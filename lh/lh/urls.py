from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'lh_project.views.home', name='home'),

     url(r'^api/', include('loghouse.urls')),

    # rest framework authentication
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
]
