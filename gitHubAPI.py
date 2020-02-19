import requests
import json


class GitHubAPI:
    def __init__(self, username):
        self.username = username

    def get_response(self):
        response = requests.get(f"https://api.github.com/users/{self.username}/repos")
        return response

    def get_repo_commit_dict(self):
        data = self.get_response().json()

        dict = {}
        for repo in data:
            repository_name = repo["name"]
            commits = requests.get(f"https://api.github.com/repos/{self.username}/{repository_name}/commits")
            commits_number = len(commits.json())
            dict[repository_name] = commits_number
        #print(dict)
        return dict

    def print_data(self):
        dict = self.get_repo_commit_dict()
        for repo_name, repo_commits in dict.items():
            print(f"Repo: {repo_name} Number of commits : {repo_commits}")

    def response_valid(self):
        return self.get_response().status_code == 200

def main():
    username = input("input your username: ")
    GitHubAPI(f"{username}").print_data()
    #print(GitHubAPI("adfadfasdfsdfegrtyfgdsg").get_response())


if __name__ == '__main__':
    main()
