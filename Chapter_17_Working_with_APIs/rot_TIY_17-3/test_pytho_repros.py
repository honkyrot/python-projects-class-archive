import requests


def test_assert_successful_code():
    """test the status code"""
    url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    assert r.status_code == 200
