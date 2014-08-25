import gists
from unittest import mock

def test_build_gist_list_url():
    url = gists.build_gist_list_url('mgdelacroix')
    assert url == 'https://api.github.com/users/mgdelacroix/gists'

def test_status_code(mock):
    f = mock.patch('gists.get_user_gists')
    f('mgdelacroix').status_code = 200

    assert gists.get_user_gists_status_code('mgdelacroix') == 200
