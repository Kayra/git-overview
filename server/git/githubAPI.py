from github import Github


class Git:

    git = Github()

    djangoOscarId = 1151051

    repository = git.get_repo(djangoOscarId)

    def contributors(self):
        return Git.repository.get_contributors()

    def openPullRequests(self):
        return Git.repository.get_pulls()

    def closedPullRequests(self):
        return Git.repository.get_pulls(state='closed')

    def issues(self):
        return Git.repository.get_issues()
