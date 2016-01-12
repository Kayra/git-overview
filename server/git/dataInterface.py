from .githubAPI import Git

gitData = Git()


def topContributors():
    """
    Returns the top five contributors to the repository.
    Each dict in the list is composed of:
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
            contributorsList.append({'contributions': contributions, 'name': name, 'url': url, 'avatarUrl': avatarUrl})

        except AttributeError:
            pass

    sorted(contributorsList)

    return(contributorsList[:5])


def recentPullRequests():
    """
    Returns the five most recent pull requests.
    Each dict in the list is composed of:
    title(string), creationDate(datetime.datetime), url(string), body(string)
    """

    pullRequests = gitData.openPullRequests()

    pullRequestList = []

    for pullRequest in pullRequests:
        title = pullRequest.title
        creationDate = pullRequest.created_at
        url = pullRequest.html_url
        body = pullRequest.body
        pullRequestList.append({'title': title, 'creationDate': creationDate, 'url': url, 'body': body})

    sorted(pullRequestList)

    return(pullRequestList[:5])


def recentIssues():
    """
    Returns the five most recent issues.
    Each dict in the list is composed of:
    title(string), creationDate(datetime.datetime), url(string), body(string)
    """

    issues = gitData.issues()

    issuesList = []

    for issue in issues:
        title = issue.title
        creationDate = issue.created_at
        url = issue.html_url
        body = issue.body
        issuesList.append({'title': title, 'creationDate': creationDate, 'url': url, 'body': body})

    sorted(issuesList)

    return(issuesList[:5])


def mostMergesUser():
    """
    Returns the user who has merged the most pull requests.
    The dictionary is composed of:
    name(string)
    """

    pulls = gitData.closedPullRequests()

    pullsList = []

    for pull in pulls:
        try:
            pullsList.append((pull.merged_by.name.encode('utf-8')))
        except AttributeError:
            pass

    name = max(set(pullsList), key=pullsList.count)

    return({'name': name})
