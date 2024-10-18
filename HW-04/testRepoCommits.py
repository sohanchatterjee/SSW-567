import unittest
import repoCommits 

class TestGetRepoCommits(unittest.TestCase):
    def testValidRepo(self):
        repo_data = [
            {'name': 'Repo1', 'commits':[{},{}]},
            {'name': 'Repo2', 'commits':[{},{},{}]}
        ]
        result = repoCommits.getRepoCommits('any', repo_data)
        expected_result = [
            "Repo: Repo1 Number of commits: 2",
            "Repo: Repo2 Number of commits: 3"
        ]
        self.assertEqual(result, expected_result)
    
    def testNoRepoData(self):
        result = repoCommits.getRepoCommits('any',[])
        self.assertEqual(result, [])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()