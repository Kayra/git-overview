from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^repository', views.RepositoryList.as_view(), name='repositoryList'),

    url(r'^contributors', views.ContributorList.as_view(), name='contributorList'),

    url(r'^pull-requests', views.PullRequestList.as_view(), name='pullRequestList'),

    url(r'^issues', views.IssueList.as_view(), name='issueList'),

    url(r'^most-merges-user', views.MostMergesUserList.as_view(), name='mostMergesUserList'),

]
