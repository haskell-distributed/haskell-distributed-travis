# Requires Python 2.6 or 2.7
import json
import sys
import urllib
import os

repo_slug = os.environ['TRAVIS_REPO_SLUG']
pull_request = os.environ['TRAVIS_PULL_REQUEST']
branch = os.environ['TRAVIS_BRANCH']
owner, repo = repo_slug.split('/')

is_fork = owner != 'haskell-distributed'
is_pull_request = pull_request != 'false'

def get_pull_request_base_branch(repo_slug, pull_request):
    url = "https://api.github.com/repos/{0}/pulls/{1}".format(repo_slug, pull_request)
    return json.load(urllib.urlopen(url))['base']['ref']

def print_upstream_branch():
    if is_fork and not is_pull_request:
        if branch == 'master':
            print('master')
        else:
            # we have to assume the upstream branch is development
            print('development')
    elif is_pull_request:
        # If this is a pull request or fork, we use the branch name
        # from the upstream base repo (e.g. development), rather
        # than the branch name from the fork (e.g. fix-xxx).
        print(get_pull_request_base_branch(repo_slug, pull_request))
    else:
        # For non-forked, non-pull-request commits
        print(branch)

if __name__ == '__main__':
    print_upstream_branch()
