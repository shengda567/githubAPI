import unittest

from gitHubAPI import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.repo = GitHubAPI("shengda567")

    def test_repo_names(self):
        expect = ["222", "555-Project", "githubAPI", "hello-world",
                  "python810zsd", "SSW567A", "STpython810_repository", "Triangle567"]
        actual = []
        for repo_names in self.repo.get_repo_commit_dict():
            actual.append(repo_names)
        self.assertEqual(actual, expect)

    def test_valid_response(self):
        self.assertEqual(GitHubAPI('invalidinput1234567').response_valid(), False)
        self.assertEqual(GitHubAPI('shengda567').response_valid(), True)

if __name__ == '__main__':
    print('Running unit tests for GitHubAPI')
    unittest.main()
