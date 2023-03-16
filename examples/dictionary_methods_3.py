internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}

another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)

print(internet_celebrities)

internet_celebrities_copy = internet_celebrities.copy()

internet_celebrities.clear()
print(internet_celebrities)
print(internet_celebrities_copy)
