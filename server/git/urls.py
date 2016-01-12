from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^get-contributors', views.getContributors, name='getContributors'),

    url(r'^get-pull-requests', views.getPullRequests, name='getPullRequests'),

    url(r'^get-recent-issues', views.getRecentIssues, name='getRecentIssues'),

    url(r'^get-mvp', views.getMVP, name='getMVP'),

]
