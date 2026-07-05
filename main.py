import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

MUSIC_DIR = "music"  # folder with your songs

def list_songs():
    print("\nAvailable songs:")
    if not os.path.exists(MUSIC_DIR):
        print("Music folder not found!")
        return
    found = False
    for genre in os.listdir(MUSIC_DIR):
        genre_path = os.path.join(MUSIC_DIR, genre)
        if os.path.isdir(genre_path):
            for song in os.listdir(genre_path):
                print(f"{genre} - {song}")
    