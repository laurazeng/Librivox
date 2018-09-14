# tests/test_librivox.py

from pytest import fixture
import vcr 
from librivox import API

@fixture
def audiobook_keys():
    return ['id', 'title', 'description', 'url_text_source', 
            'language', 'copyright_year', 'num_sections', 'url_rss',
            'url_zip_file', 'url_project', 'url_librivox',
            'url_other', 'totaltime', 'totaltimesecs', 'authors']

@fixture
def audiotrack_keys():
    return ['id', 'section_number', 'title', 'listen_url',
            'language', 'playtime']

@fixture
def author_keys():
    return ['id', 'first_name', 'last_name', 'dob', 'dod']

@vcr.use_cassette('tests/cassettes/get-audiobook.yml')
def test_get_audiobook(audiobook_keys):
    api = API()
    id = '52'
    params = {'id': id, 'format': 'json'}
    response = api.get_audiobooks(params)

    assert response['books'] is not None

    audiobook = response['books'][0]

    assert audiobook['id'] == id, "The id should be in the response"
    assert set(audiobook_keys).issubset(audiobook.keys()), "All keys should be in the reponse"

@vcr.use_cassette('tests/cassettes/get-audiotrack.yml')
def test_get_audiotrack(audiotrack_keys):
    api = API()
    id = '52'
    params = {'id': id, 'format': 'json'}
    response = api.get_audiotracks(params)

    assert response['sections'] is not None

    audiotrack = response['sections']

    assert audiotrack['id'] == id, "The id should be in the response"
    assert set(audiotrack_keys).issubset(audiotrack.keys()), "All keys should be in the reponse"

@vcr.use_cassette('tests/cassettes/get-author.yml')
def test_get_author(author_keys):
    api = API()
    id = '52'
    params = {'id': id, 'format': 'json'}
    response = api.get_authors(params)

    assert response['authors'] is not None

    author = response['authors'][0]

    assert author['id'] == id, "The id should be in the response"
    assert set(author_keys).issubset(author.keys()), "All keys should be in the reponse"
