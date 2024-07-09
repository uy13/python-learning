album = {"title": "The Dark Side of the Moon",
         "artist": "Pink Floyd",
         "year": 1973,
         "tracks": ("Speak to Me",
                    "Breathe",
                    "On the Run",
                    "Time",
                    "The Great Gig in the Sky",
                    "Money",
                    "Us and Them",
                    "Any Colour You Like",
                    "Brain Damage",
                    "Eclipse")}
# for key in album:
# print(f"{key}: {album[key]}")

for key, value in album.items():
    print(f"{key}: {value}")
