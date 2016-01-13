from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import dataInterface


@api_view(['GET'])
def getContributors(request):
    """
    Returns the five users with the most contributions to the project.
    """

    contributorsDicts = dataInterface.topContributors()

    return Response(contributorsDicts)


@api_view(['GET'])
def getPullRequests(request):
    """
    Returns the five most recently opened pull requests.
    """

    pullRequestsDicts = dataInterface.recentPullRequests()

    return Response(pullRequestsDicts)


@api_view(['GET'])
def getIssues(request):
    """
    Returns the five most recently opened issues.
    """

    issueDicts = dataInterface.recentIssues()

    return Response(issueDicts)


@api_view(['GET'])
def getMostMergesUser(request):
    """
    Returns the user who has merged the most pull requests.
    """

    mostMergesUser = dataInterface.mostMergesUser()

    return Response(mostMergesUser)
