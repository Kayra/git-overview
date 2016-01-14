from .githubAPI import Git
from .models import Contributor, PullRequest, Issue, User

gitData = Git()


def topContributors():
    """
    Returns the top five contributors to the repository.
    Each set in the list is composed of:
    name(string), contributions(int), url(string), avatar_url(string)
    """

    contributors = gitData.contributors()

    contributorsList = []

    for contributor in contributors:
        try:
            name = contributor.name.encode('utf-8')
            contributions = contributor.contributions
            url = contributor.html_url
            avatarUrl = contributor.avatar_url
            contributorsList.append((contributions, name, url, avatarUrl))
        except AttributeError:
            pass

    sorted(contributorsList)

    for index, contributor in enumerate(contributorsList[:5]):
        Contributor.objects.update_or_create(contributions=contributor[0], name=contributor[1].decode('utf-8'), url=contributor[2], avatarUrl=contributor[3], position=index)


def recentPullRequests():
    """
    Returns the five most recent pull requests.
    Each set in the list is composed of:
    title(string), creationDate(datetime.datetime), url(string), body(string)
    """

    pullRequests = gitData.openPullRequests()

    pullRequestList = []

    for pullRequest in pullRequests:
        title = pullRequest.title
        creationDate = pullRequest.created_at.date()
        url = pullRequest.html_url
        body = pullRequest.body
        pullRequestList.append((title, creationDate, url, body))

    sorted(pullRequestList)

    for index, pullRequest in enumerate(pullRequestList[:5]):
        PullRequest.objects.update_or_create(title=pullRequest[0], creationDate=pullRequest[1], url=pullRequest[2], body=pullRequest[3], position=index)


def recentIssues():
    """
    Returns the five most recent issues.
    Each set in the list is composed of:
    title(string), creationDate(datetime.datetime), url(string), body(string)
    """

    issues = gitData.issues()

    issueList = []

    for issue in issues:
        title = issue.title
        creationDate = issue.created_at.date()
        url = issue.html_url
        body = issue.body
        issueList.append((title, creationDate, url, body))

    sorted(issueList)

    for index, issue in enumerate(issueList[:5]):
        Issue.objects.update_or_create(title=issue[0], creationDate=issue[1], url=issue[2], body=issue[3], position=index)


def mostMergesUser():
    """
    Returns the user who has merged the most pull requests.
    The set is composed of:
    name(string)
    """

    pullRequests = gitData.closedPullRequests()

    pullsList = []

    for pullRequest in pullRequests:
        try:
            pullsList.append((pullRequest.merged_by.name.encode('utf-8')))
        except AttributeError:
            pass

    userName = max(set(pullsList), key=pullsList.count)

    User.objects.update_or_create(id=1, name=userName.decode('utf-8'))


def updateAPIData():
    topContributors()
    recentPullRequests()
    recentIssues()
    mostMergesUser()
