import os
from enum import Enum

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import creds

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.client_id,
                                               client_secret=creds.client_secret,
                                               redirect_uri=creds.redirect_url,
                                               scope=scope))


# clamps a given limit based on the query guidelines outlined in the Spotify Web API documentation
def limit_clamper(x):
    if x <= 0:
        return 1
    elif x > 50:
        return 50
    else:
        return x


# enum representing the term lengths supported by the Spotify Web API
# list with the parameter to be used in the request in the 0th index and the title of such a request in the 1st index
class Term(Enum):
    SHORT = ['short_term', 'the Past 4 Weeks']
    MEDIUM = ['medium_term', 'the Past 6 Months']
    LONG = ['long_term', 'All Time']


# titles a query based on the limit, data, and time range
def titler(limit, the_data, time_range):
    if limit == 1:
        the_data = the_data[:-1]
        return f'Your Top {the_data} of {time_range.value[1]}:'
    else:
        return f'Your Top {limit} {the_data} of {time_range.value[1]}:'


# gets the users top tracks based on a given limit and time range
def top_tracks_func(limit, time_range):
    limit = limit_clamper(limit)
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range.value[0])

    top_tracks_list = []
    for idx, item in enumerate(top_tracks['items']):
        artist_str = item['artists'][0]['name']
        if len(item['artists']) > 1:
            artist_str = artist_str + ', '
            for art_idx in range(1, len(item['artists'])):
                artist_str = artist_str + item['artists'][art_idx]['name']
                if art_idx < len(item['artists']) - 1:
                    artist_str = artist_str + ', '
        top_tracks_list.append(item['name'] + ' - ' + artist_str)
    return [top_tracks_list, titler(limit, 'Tracks', time_range)]


# gets the users top artists based on a given limit and time range
def top_artists_func(limit, time_range):
    limit = limit_clamper(limit)
    top_artists = sp.current_user_top_artists(limit=limit, time_range=time_range.value[0])

    top_artists_list = []
    for idx, item in enumerate(top_artists['items']):
        top_artists_list.append(item['name'])
    return [top_artists_list, titler(limit, 'Artists', time_range)]


# formats the resulting list to be readable
def list_formatter(input_list):
    n = len(input_list[0])
    result = [input_list[1], os.linesep]
    for x in range(n):
        result.append(str(x + 1) + ') ' + input_list[0][x])
        result.append(os.linesep)
    return ''.join(result)


# for the time being, print the results to the console
print(list_formatter(top_tracks_func(10, Term.LONG)))
print(list_formatter(top_artists_func(10, Term.LONG)))
