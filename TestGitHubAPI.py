import unittest
from unittest import mock

from gitHubAPI import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.repo = GitHubAPI("shengda567")

    @mock.patch('requests.get')
    def test_repo_names(self, mockedReq):
        mockedReq.return_value = ["222", "555-Project", "githubAPI", "hello-world",
                                 "python810zsd", "SSW567A", "STpython810_repository", "Triangle567"]

        expect = ["222", "555-Project", "githubAPI", "hello-world",
                  "python810zsd", "SSW567A", "STpython810_repository", "Triangle567"]

        self.assertEqual(self.repo.get_response(), expect)


    @mock.patch('requests.get')
    def test_valid_response(self, mockedReq):
        mockedReq.return_value = 200
        #self.assertNotEqual(GitHubAPI('invalidinput1234567').get_response(), 200)
        self.assertEqual(self.repo.get_response(), 200)

if __name__ == '__main__':
    print('Running unit tests for GitHubAPI')
    unittest.main()
