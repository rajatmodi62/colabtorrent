# -*- coding: utf-8 -*-
"""Torrent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Uo1_KHGxOe_Dh4-DjQyEb0wROp-tMv0w
"""

TorrName = 'YOUR TORRENT NAME'

FolderPath = f'/content/drive/My Drive/{TorrName}'
TorrPath = f'{TorrName}.torrent'

def init():
  import os
  os.system('apt-get install transmission-cli')
  from google.colab import drive
  drive.mount('/content/drive')

def download(loc, tor):
  assert (os.path.exists(tor)==True), "The torrent file doesn't exist"
  print("If the cell is running for a long time check if the torrent has no seeders!")
  os.system(f"transmission-cli -w '{loc}' {tor}")
  print("DONE")

init()

download(FolderPath,TorrPath)