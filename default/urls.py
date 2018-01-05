from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.signin),
    url(r'^signup/',views.signup),
    url(r'^ask/',views.ask),
    url(r'^answer/',views.answer),
    url(r'^answerset/',views.answerset),
    url(r'^problemset/',views.problemset),
    url(r'^logout/',views.logout)
]