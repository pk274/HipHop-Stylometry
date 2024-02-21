# Paul Kull, 2024

import shutil
import json
import re

from os import listdir
from os.path import isfile, join, getsize, dirname
from os import remove


dataPath = dirname(__file__) + '/Data/'
#artistNames = ['Snoop Dogg', 'Eminem', 'Obie Trice', 'Kendrick Lamar', 'Dr. Dre', 'Jay-Z', 'Ice Cube']
artistNames = ['Dr. Dre SOI', 'Eminem', 'Jay-Z', 'Kendrick Lamar', 'Snoop Dogg',]

def relocate_files():
        for artist in artistNames:
                artistName = artist
                artistTag = artist[0]

                onlyfiles = [f for f in listdir(dataPath + artistName) if isfile(join(dataPath + artistName, f))]

                i = 0
                for file in onlyfiles:
                        shutil.copy(dataPath + artistName + "/" + file, dataPath + 'corpus/' + artistTag + "_" + str(i))
                        #shutil.copy(dataPath + artistName + "/" + file, 'C:/Users/Paul/Desktop/Unistuff/1. sem/dh/dataset/' + artistName + '/' + file)
                        i += 1

def delete_small_files(minSize = 1000):
        onlyfiles = [f for f in listdir(dataPath + 'corpus') if isfile(join(dataPath + '/corpus', f))]

        size = 0
        i = 0
        for file in onlyfiles:
                size = getsize(dataPath + '/corpus' + file)
                if size < minSize:
                        remove(dataPath + '/corpus' + file)
                i += 1

def find_largest_files(numFiles = 50):
        for artist in artistNames:
                cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artist)
                onlyfiles = [f for f in listdir(dataPath+cleanArtistName) if isfile(join(dataPath + cleanArtistName, f))]
                iteration = 0
                while len(onlyfiles) > numFiles:
                        iteration += 1
                        print(iteration)
                        smallestFileSize = 999999999999999999999999
                        smallestFile = onlyfiles[0]
                        for file in onlyfiles:
                                if getsize(dataPath+cleanArtistName+'/'+file) < smallestFileSize:
                                        smallestFile = file
                                        smallestFileSize = getsize(dataPath+cleanArtistName+'/'+file)
                        remove(dataPath+cleanArtistName+'/'+smallestFile)
                        onlyfiles.remove(smallestFile)



def delete_features():
        i = 0
        for artist in artistNames:
                print(i)
                i += 1
                cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artist)
                with open('C:/Users/Paul/Desktop/Unistuff/1. sem/dh/projekt/00songs'+cleanArtistName+'.json', encoding='utf-8') as f:
                    songs = json.load(f)
                for song in songs:
                        title = song['title']
                        primaryArtist = song['primary_artist']['name']
                        songTitle = re.sub('[<,>,:,",/,\,|,?,*]', '', song['title'])
                        if primaryArtist.casefold() != artist.casefold():
                                if isfile(dataPath + '/corpus'+artist+'/'+songTitle+'.txt'):
                                        remove(dataPath + '/corpus'+artist+'/'+songTitle+'.txt')

def delete_unfit_versions():
        unfitWords = ['show', 'clean', 'performance', 'original', 'mix', 'edit', 'mix', 'demo', 'video', 'instrumental', 'radio', 'acapella']
        i = 0
        for artist in artistNames:
                cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artist)
                onlyfiles = [f for f in listdir(dataPath+cleanArtistName) if isfile(join(dataPath + cleanArtistName, f))]

                for file in onlyfiles:
                        fileName = file.casefold()
                        delete = False
                        for word in unfitWords:
                                if word.casefold() in fileName: delete = True; break
                        if delete:
                                remove(dataPath + cleanArtistName + "/" + file)

def delete_songs_by_date(yearDifference = 15):
        for artist in artistNames:
                year = None
                if artist == 'Eminem':
                        year = 1999
                if artist == 'Jay-Z':
                        year = 1999
                if artist == 'Snoop Dogg':
                        year = 1992
                if artist == 'Kendrick Lamar':
                        year = 2012

                if year == None: continue
                cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artist)

                with open(dirname(__file__) + '/00songs'+cleanArtistName+'.json', encoding='utf-8') as f:
                    songs = json.load(f)
                for song in songs:
                        songTitle = re.sub('[<,>,:,",/,\,|,?,*]', '', song['title'])
                        title = song['title']
                        releaseYear = song['release_date_components']
                        if releaseYear is None:
                                if isfile(dataPath + artist+'/'+songTitle+'.txt'):
                                        remove(dataPath + artist+'/'+songTitle+'.txt')
                                        print("removed bc of none")
                                continue
                        releaseYear = releaseYear['year']
                        if abs(releaseYear - year) > yearDifference or releaseYear is None:
                                if isfile(dataPath + artist+'/'+songTitle+'.txt'):
                                        remove(dataPath +artist+'/'+songTitle+'.txt')
                                        print('removed bc of year')



if __name__ == "__main__":
        #delete_features()
        #delete_unfit_versions()
        #delete_small_files(800)
        #delete_songs_by_date()
        find_largest_files(150)
        relocate_files()
        pass