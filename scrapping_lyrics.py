from bs4 import BeautifulSoup
import requests


def messages_love():
    url = "https://genius.com/Elton-john-tiny-dancer-lyrics"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    song = soup.select('.Lyrics__Container-sc-1ynbvzw-2.jgQsqn')
    lyric=song[0].text
    return [lyric[i:i+40] for i in range(0, len(lyric), 40)]


def messages_mix():
    url = "https://www.allthelyrics.com/lyrics/elvis_presley/only_you-lyrics-423192.html"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    song = soup.select('.content-text-inner')
    lyric="".join(song[0].text.split('\n'))
    return [lyric[i:i+40] for i in range(0, len(lyric), 40)]


def messages_hate():
    url = "https://genius.com/The-all-american-rejects-gives-you-hell-lyrics"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    song = soup.select('.Lyrics__Container-sc-1ynbvzw-2.jgQsqn')
    lyric=song[2].text
    return [lyric[i:i+40] for i in range(0, len(lyric), 40)]
