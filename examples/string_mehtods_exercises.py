mixed_case = "A SONG OF ICE AND FIRE"

print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.istitle())

title_case = mixed_case.title()

print(title_case)

print(mixed_case.startswith("A"))
print(mixed_case.endswith("E"))

words = mixed_case.split()

print("".join(words).isalpha())











