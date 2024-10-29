import unittest
from unittest.mock import patch
import repoCommits 

class TestGetRepoCommits(unittest.TestCase):
    
    @patch('repoCommits.requests.get')
    def testValidRepo(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'name': 'Repo1'},
            {'name': 'Repo2'}
        ]
        
        mock_get.side_effect = [
            mock_get.return_value,
            mock_get.return_value,
            mock_get.return_value,
        ]
        mock_get.return_value.json.side_effect = [
            [{}, {}],
            [{}, {}, {}] 
        ]

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