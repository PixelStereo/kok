"""kok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home),
    url(r'^clear$', views.clear),
    url(r'^new-item$', views.new_item),
    url(r'^new-item/$', views.new_item),
    url(r'^item/(?P<id_item>\d+)$', views.view_item),
    url(r'^items/$', views.list_items),
    url(r'^items$', views.list_items),
    url(r'^items/(?P<filter_attribute>\s+)/(?P<filter_value>\s+)$', views.list_items),
    url(r'^new-location$', views.new_location),
    url(r'^new-location/$', views.new_location),
    url(r'^locations/$', views.list_locations),
    url(r'^locations$', views.list_locations),
    url(r'^location/(?P<id_location>\d+)$', views.view_location),
    url(r'^locations/(?P<filter_attribute>\s+)/(?P<filter_value>\s+)$', views.list_locations),
    url(r'^new-person$', views.new_person),
    url(r'^new-person/$', views.new_person),
    url(r'^person/(?P<id_person>\d+)$', views.view_person),
    url(r'^persons/$', views.list_persons),
    url(r'^persons$', views.list_persons),
    url(r'^persons/(?P<filter_attribute>\s+)/(?P<filter_value>\s+)$', views.list_persons),
    # TODO : move the following lines to a demo project
    url(r'^rainbow$', views.rainbow),
    url(r'^date$', views.date_actuelle),
    url(r'^hello/(?P<name>\w+)$', views.hello),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)$', views.addition),
]
