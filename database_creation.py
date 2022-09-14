import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS artists (artist,genres,songs,popularity,link)')
conn.commit()

df = pd.read_csv("dataset/artists-data.csv")
df.to_sql("artists", conn, if_exists='replace', index=False)

c.execute('CREATE TABLE IF NOT EXISTS lyrics (alink,sname,slink,lyric,language)')
conn.commit()

df = pd.read_csv("dataset/lyrics-data.csv")
df.to_sql("lyrics", conn, if_exists='replace', index=False)