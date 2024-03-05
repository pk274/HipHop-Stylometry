# Paul Kull, 2024

import requests
from bs4 import BeautifulSoup
import json
import re
import os
from os.path import dirname

# Genius access token and genius api url
accessToken = {'Authorization': 'Bearer fIiVYTN75YvyJc8gXBBxmGG5huYxIs-Q_KpnywD7T-Jkk5UfJSzCstr3ej3hKebK'}
url = 'http://api.genius.com'

# List of artists whose lyrics will be scraped
#artistNames = ['Taylor Swift', 'Eminem', 'Jay-Z', 'Kendrick Lamar', 'Snoop Dogg']

dataPath = dirname(__file__)+'/'


def print_page():
    # Test Function to print out a specific web page
    search_url = url + '/search'
    data = {'q': artistName}
    page = requests.get(search_url, params=data, headers=accessToken)
    print(page.text)


def find_artists_songs(artist):
    # First find artits suffix on genius
    search_url = url + '/search'
    data = {'q': artist}
    page = requests.get(search_url, params=data, headers=accessToken)
    artistSuffix = None
    jsonPage = page.json()
    for hit in jsonPage['response']['hits']:
        if hit['result']['primary_artist']['name'] == artistName:
            artistSuffix = hit['result']['primary_artist']['api_path']
            print(artistSuffix)
            break
    artistPage = url + artistSuffix + '/songs/'

    # Next go through songs and download their information
    songs = []
    keepScrolling = True
    index = 1
    while keepScrolling:
        page = requests.get(artistPage, params={'page': index}, headers=accessToken)
        jsonPage = page.json()
        song = jsonPage['response']['songs']

        if song:
            songs += song
            index += 1
        else:
            keepScrolling = False

    return songs


def get_lyrics(songs, artist, prefilter = True):
    # Visit the lyrics page in the song information and scrape the lyrics
    i = 0
    for song in songs:
        title = song['title']
        titleCF = title.casefold()
        if prefilter:
            if "Remix".casefold() in titleCF or "Version".casefold() in titleCF or "live".casefold() in titleCF or "acappella".casefold() in titleCF or "a cappella".casefold() in titleCF or "unplugged".casefold() in titleCF: continue             # In order to avoid duplicates
            if song['primary_artist']['name'].casefold() != artist.casefold(): continue
        print("Song", i, "of", len(songs), ",", song['title'])
        url = song['url']
        page = requests.get(url)
        soup = BeautifulSoup(page.text.replace('<br/>', '\n'), 'html.parser')

        divs = soup.find_all("div", class_=re.compile("^lyrics$|Lyrics__Container"))

        lyrics = "\n".join([div.get_text() for div in divs])

        lyrics = cleanLyrics(lyrics, artist, song['primary_artist']['name'])
        i += 1
        if lyrics == "": continue                                       # Dont save empty files
        songTitle = re.sub('[<,>,:,",/,\,|,?,*]', '', song['title'])    # Remove forbidden symbols for paths
        f = open(dataPath+'/Data/'+artist+'/'+songTitle+'.txt', 'w', encoding='utf-8', errors='ignore')
        f.write(lyrics)
        f.close()


def cleanLyrics(lyrics, artist, primaryArtist):
    # Filter lyrics to contain only lyrics from the artist of interest.
    # This works only if the songs are structured in the way they usually are on Genius.

    sectionSplit = r'\[([^\]]+)\]'

    sections = re.split(sectionSplit, lyrics)
    artistLyrics = ""
    addNextSection = False
    for i in range(0, len(sections)):
                text = sections[i].casefold()
                condition0 = 'Verse'.casefold() in text or 'Chorus'.casefold() in text or 'Hook'.casefold() in text or 'Intro'.casefold() in text or 'Outro'.casefold() in text or 'Bridge'.casefold() in text or 'Interlude'.casefold() in text
                condition1 = artist.casefold() in text or (not ':' in text and artist.casefold() == primaryArtist.casefold())
                condition2 = len(text) < 90
                if addNextSection == False and (condition0 and condition1 and condition2):
                        addNextSection = True
                        continue
                if addNextSection:
                        artistLyrics += text
                        addNextSection = False
    return artistLyrics



if __name__ == "__main__":
    for artistName in artistNames:
        j = 0
        print('Artist', j, 'of', len(artistNames), ':', artistName)
        print("Searching songs on Genius")
        songs = find_artists_songs(artistName)
        cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artistName)
        os.makedirs(os.path.dirname(dataPath+'/Data/'+cleanArtistName+'/00songs.json'), exist_ok=True)
        with open(dataPath+'00songs'+cleanArtistName+'.json', 'w', encoding='utf-8') as f:
            json.dump(songs, f, ensure_ascii=False, indent=4)
        #with open(dataPath+'00songs'+cleanArtistName+'.json', encoding='utf-8') as f:
        #    songs = json.load(f)
        print("Songs found, extracting lyrics now")
        get_lyrics(songs, artistName)
        j += 1