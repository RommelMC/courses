from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^courses/destroy/(?P<id>[0-9]+)$', views.destroy, name='destroy'),
    url(r'^courses/delete/(?P<id>[0-9]+)$', views.delete, name='delete'),
    url(r'^courses/comments/(?P<id>[0-9]+)$', views.comment, name='comment'),
    url(r'^courses/addcomment/(?P<id>[0-9]+)$', views.addcomment, name='addcomment'),
    url(r'^courses/add', views.add, name='add'),
]

