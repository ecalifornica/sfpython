from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list, name="faq_list"),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name="faq_detail"),
]

