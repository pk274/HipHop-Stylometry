# Paul Kull, 2024

import shutil
import json
import re

from os import listdir
from os.path import isfile, join, getsize, dirname
from os import remove


dataPath = dirname(__file__) + '/Data/'
tablePath = dirname(__file__) + '/'

#artistNames = ['Snoop Dogg', 'Eminem', 'Obie Trice', 'Kendrick Lamar', 'Dr. Dre', 'Jay-Z', 'Ice Cube']
artistNames = ['Eminem', 'Jay-Z', 'Kendrick Lamar', 'Snoop Dogg', 'Dr. Dre']
#artistNames = ['Eminem', 'Jay-Z', 'Kendrick Lamar', 'Snoop Dogg']
#artistNames = ['Dr. Dre']
#artistNames = ['Taylor Swift', 'Bob Dylan', 'Eminem', 'Jay-Z', 'Kendrick Lamar', 'Snoop Dogg']

def relocate_files(addSOI = True):
        for artist in artistNames:
                artistName = artist
                artistTag = artist

                onlyfiles = [f for f in listdir(dataPath + artistName) if isfile(join(dataPath + artistName, f))]

                i = 0
                for file in onlyfiles:

                        shutil.copy(dataPath + artistName + "/" + file, dataPath + 'corpus/' + artistTag + "_" + str(i))
                        #shutil.copy(dataPath + artistName + "/" + file, 'C:/Users/Paul/Desktop/Unistuff/1. sem/dh/dataset/' + artistName + '/' + file)
                        i += 1
        if addSOI:
                onlyfiles = [f for f in listdir(dataPath + 'Dr. Dre SOI') if isfile(join(dataPath + 'Dr. Dre SOI', f))]
                for file in onlyfiles:

                        shutil.copy(dataPath + 'Dr. Dre SOI' + "/" + file, dataPath + 'corpus/' + file)


def relocate_and_group_by_year(addSOI = True):
        for artist in artistNames:
                i = 0
                cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artist)
                with open(dirname(__file__) + '/00songs'+cleanArtistName+'.json', encoding='utf-8') as f:
                        songs = json.load(f)

                groupedSongs = []
                for song in songs:
                        primaryArtist = song['primary_artist']['name']
                        if (primaryArtist.casefold() != artist.casefold()): continue
                        songTitle = re.sub('[<,>,:,",/,\,|,?,*]', '', song['title'])
                        if song in groupedSongs or not isfile(dataPath + artist+'/'+songTitle+'.txt'): continue
                        releaseYear = song['release_date_components']
                        if releaseYear is None:
                                shutil.copy(dataPath + artist + "/" + songTitle + '.txt', dataPath + 'corpus/' + artist + "_" + str(i))
                                i += 1
                                continue
                        releaseYear = releaseYear['year']
                        if (artist == 'Bob Dylan' or artist == 'Taylor Swift'):
                                fYear = open(dataPath+'corpus/Songs '+artist+'_'+str(releaseYear)+'.txt', 'w', encoding='utf-8', errors='ignore')
                        else:
                                fYear = open(dataPath+'corpus/'+artist+'_'+str(releaseYear)+'.txt', 'w', encoding='utf-8', errors='ignore')
                        for song2 in songs:
                                primaryArtist2 = song2['primary_artist']['name']
                                if (primaryArtist2.casefold() != artist.casefold()): continue
                                releaseYear2 = song2['release_date_components']
                                if releaseYear2 is None: continue
                                releaseYear2 = releaseYear2['year']
                                if releaseYear2 != releaseYear: continue
                                songTitle2 = re.sub('[<,>,:,",/,\,|,?,*]', '', song2['title'])
                                if not isfile(dataPath + artist+'/'+songTitle2+'.txt'): continue
                                fSong = open(dataPath + artist + "/" + songTitle2+'.txt', 'r', encoding='utf-8', errors='ignore')
                                lyrics = fSong.read()
                                fSong.close()
                                fYear.write(lyrics)
                                fYear.write('\n')
                        fYear.close()
        if addSOI:
                onlyfiles = [f for f in listdir(dataPath + 'Dr. Dre SOI') if isfile(join(dataPath + 'Dr. Dre SOI', f))]
                for file in onlyfiles:

                        shutil.copy(dataPath + 'Dr. Dre SOI' + "/" + file, dataPath + 'corpus/' + file)


def relocate_and_group_by_name():
        for artist in artistNames:
                i = 0
                cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artist)
                with open(dirname(__file__) + '/00songs'+cleanArtistName+'.json', encoding='utf-8') as f:
                        songs = json.load(f)

                groupedSongs = []
                for song in songs:
                        primaryArtist = song['primary_artist']['name']
                        fArtist = open(dataPath+'corpus/'+artist+'.txt', 'w', encoding='utf-8', errors='ignore')
                        if (primaryArtist.casefold() != artist.casefold()): continue
                        songTitle = re.sub('[<,>,:,",/,\,|,?,*]', '', song['title'])
                        if song in groupedSongs or not isfile(dataPath + artist+'/'+songTitle+'.txt'): continue
                        releaseYear = song['release_date_components']
                        if releaseYear is None:
                                shutil.copy(dataPath + artist + "/" + songTitle + '.txt', dataPath + 'corpus/' + artist[0] + "_" + str(i))
                                i += 1
                                continue
                        releaseYear = releaseYear['year']
                        fArtist = open(dataPath+'corpus/'+artist[0]+'_'+str(releaseYear)+'.txt', 'w', encoding='utf-8', errors='ignore')
                        for song2 in songs:
                                primaryArtist2 = song2['primary_artist']['name']
                                if (primaryArtist2.casefold() != artist.casefold()): continue
                                releaseYear2 = song2['release_date_components']
                                if releaseYear2 is None: continue
                                releaseYear2 = releaseYear2['year']
                                if releaseYear2 != releaseYear: continue
                                songTitle2 = re.sub('[<,>,:,",/,\,|,?,*]', '', song2['title'])
                                if not isfile(dataPath + artist+'/'+songTitle2+'.txt'): continue
                                fSong = open(dataPath + artist + "/" + songTitle2+'.txt', 'r', encoding='utf-8', errors='ignore')
                                lyrics = fSong.read()
                                fSong.close()
                                fArtist.write(lyrics)
                                fArtist.write('\n')
                        fArtist.close()


def delete_small_files(minSize = 1000):
        onlyfiles = [f for f in listdir(dataPath + 'corpus') if isfile(join(dataPath + '/corpus', f))]

        size = 0
        i = 0
        for file in onlyfiles:
                size = getsize(dataPath + '/corpus/' + file)
                if size < minSize:
                        remove(dataPath + '/corpus/' + file)
                i += 1

def delete_duplicates():
        for artist in artistNames:
                cleanArtistName = re.sub('[<,>,:,",/,\,|,?,*]', '', artist)
                onlyfiles = [f for f in listdir(dataPath+cleanArtistName) if isfile(join(dataPath + cleanArtistName, f))]
                fileNames = []

                for file in onlyfiles:
                        fileName = file.casefold()
                        add = True
                        for name in fileNames:
                                if name == fileName:
                                        remove(dataPath + cleanArtistName + "/" + file)
                                        add = False
                                        fileNames.remove(name)
                                        break
                        if add:
                                fileNames += fileName

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
                with open(tablePath+'00songs'+cleanArtistName+'.json', encoding='utf-8') as f:
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
                                continue
                        releaseYear = releaseYear['year']
                        if abs(releaseYear - year) > yearDifference or releaseYear is None or (artist == 'Kendrick Lamar' and releaseYear < 2006):
                                if isfile(dataPath + artist+'/'+songTitle+'.txt'):
                                        remove(dataPath +artist+'/'+songTitle+'.txt')



if __name__ == "__main__":
        #delete_features()
        #delete_unfit_versions()
        #delete_duplicates()
        #delete_songs_by_date()
        #find_largest_files(250)
        #relocate_files()
        #delete_small_files(1300)
        relocate_and_group_by_year(False)
        delete_small_files(5000)

        #artistNames = ['Dr. Dre SOI']
        #relocate_files()
        pass