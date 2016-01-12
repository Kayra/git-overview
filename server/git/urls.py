from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^get-contributors', views.getContributors, name='getContributors'),

    url(r'^get-pull-requests', views.getPullRequests, name='getPullRequests'),

    url(r'^get-issues', views.getIssues, name='getIssues'),

    url(r'^get-most-merges-user', views.getMostMergesUser, name='getMostMergesUser'),

]
