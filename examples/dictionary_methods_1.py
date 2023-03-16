cool_bands = {"Queen": "Bohemian Rhapsody",
              "Bee Gees": "Stayin' Alive",
              "U2": "One",
              "Michael Jackson": "Billie Jean",
              "The Beatles": "Hey Jude",
              "Bob Dylan": "Like a Rolling Stone"}


print(len(cool_bands))


print(cool_bands.keys())

# how to for loop through a dictionary

for key in cool_bands:
    print(key)

print(cool_bands.values())

for key, value in cool_bands.items():
    print(key, value)

print(cool_bands.get("The Promise of the Real", "This band is not cool"))






