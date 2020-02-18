import unittest

from .gitHubAPI import gitHubAPI

class TestGitHubAPI(unittest.TestCase):
    def test_commit_results(self):
        expect = ["Repo: shengda567 Number of commits : 2",
                  "Repo: shengda567 Number of commits : 1",
                  "Repo: shengda567 Number of commits : 2",
                  "Repo: shengda567 Number of commits : 1",
                  "Repo: shengda567 Number of commits : 3",
                  "Repo: shengda567 Number of commits : 2",
                  "Repo: shengda567 Number of commits : 7"]
        self.assertEqual(gitHubAPI("shengda567"), expect)

    def test_invalid_name(self):
        self.assertEqual(gitHubAPI('asdfasdf'), "invalid name")

if __name__ == '__main__':
    print('Running unit tests for GitHubAPI')
    unittest.main()