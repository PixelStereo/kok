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
    url(r'^$', views.home),
    url(r'^home$', views.home),
    url(r'^clear$', views.clear),
    url(r'^rainbow$', views.rainbow),
    url(r'^item$', views.new_item),
    url(r'^item/(?P<id_item>\d+)$', views.view_item),
    url(r'^items$', views.list_items),
    url(r'^items/(?P<filter_attribute>\s+)/(?P<filter_value>\s+)$', views.list_items),
    url(r'^date$', views.date_actuelle),
    url(r'^hello/(?P<name>\w+)$', views.hello),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)$', views.addition),
]
