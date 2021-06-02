# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine2 = {}
    for word in magazine:
        if word in magazine2:
            magazine2[word] += 1
        else:
            magazine2[word] = 1
    for word in note:
        if word not in magazine2:
            print("No", word)
            return
        if magazine2[word] < 1:
            print("No", word)
            return
        magazine2[word] -= 1
    print("Yes")


magazine = "give me one grand today night".split(" ")
note = "give one grand today".split(" ")

print(checkMagazine(magazine, note))
