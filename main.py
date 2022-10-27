import spotipy
from spotipy.oauth2 import SpotifyOAuth

import creds

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.client_id,
                                               client_secret=creds.client_secret,
                                               redirect_uri=creds.redirect_url,
                                               scope=scope))

results = sp.current_user_top_tracks(limit=50, time_range='long_term')

for idx, item in enumerate(results['items']):
    artist_str = item['artists'][0]['name']
    if len(item['artists']) > 1:
        artist_str = artist_str + ', '
        for art_idx in range(1, len(item['artists'])):
            artist_str = artist_str + item['artists'][art_idx]['name']
            if art_idx < len(item['artists']) - 1:
                artist_str = artist_str + ', '
    print(str(idx + 1) + ') ' + item['name'] + ' - ' + artist_str)
