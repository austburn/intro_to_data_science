import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.

    response = requests.get(url)
    response = json.loads(response.text)
    top_artist = response['topartists']['artist'][0]['name']

    return top_artist


if __name__ == '__main__':
    url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&format=json&api_key=6f8f282fa5f4e90f6eadbfd88f1a77af'
    print api_get_request(url)
