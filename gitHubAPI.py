import requests
import json


def gitHubAPI(username):

    response = requests.get(f"https://api.github.com/users/{username}/repos")

    data = response.json()
    list = []
    for repo in data:
        try:
            repository_name = repo["name"]
        except(TypeError, KeyError, IndexError):
            return "invalid name"
        else:
            commits = requests.get(f"https://api.github.com/repos/{username}/{repository_name}/commits")
            commits_number = len(commits.json())
            output = f"Repo: {username} Number of commits : {commits_number}"
            list.append(output)
    return list
if __name__ == '__main__':
    gitHubAPI("shengda567")