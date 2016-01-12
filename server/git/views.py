import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import dataInterface


@api_view(['GET'])
def getContributors(request):
    """
    Returns the five users with the most contributions to the project.
    """

    contributorsList = dataInterface.topContributors()

    return Response(json.dumps(contributorsList))


@api_view(['GET'])
def getPullRequests(request):
    """
    Returns the five most recently opened pull requests.
    """

    pullRequestsList = dataInterface.recentPullRequests()

    return Response(json.dumps(pullRequestsList))


@api_view(['GET'])
def getIssues(request):
    """
    Returns the five most recently opened issues.
    """

    issuesList = dataInterface.recentIssues()

    return Response(json.dumps(issuesList))


@api_view(['GET'])
def getMostMergesUser(request):
    """
    Returns the user who has merged the most pull requests.
    """

    mostMergesUser = dataInterface.mostMergesUser()

    return Response(json.dumps(mostMergesUser))
