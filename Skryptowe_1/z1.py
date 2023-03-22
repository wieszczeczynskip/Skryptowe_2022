print("Hello!")
files = []

# files = ["view.jpg", "test.txt", "game.csv", "work.doc", "quiz.txt", "note.txt", "foto.jpg"]
# view.jpg
# test.txt
# game.csv
# work.doc
# quiz.txt
# note.txt
# foto.jpg

while True:
    file = input("Type in the name of the file. End - [0]\n")
    if file == "0":
        break
    files.append(file)

files.sort()

jpg = []
txt = []
csv = []
doc = []

for i in files:
    if i.endswith(".jpg"):
        jpg.append(i)
    if i.endswith(".csv"):
        csv.append(i)
    if i.endswith(".doc"):
        doc.append(i)
    if i.endswith(".txt"):
        txt.append(i)

print(jpg)
print(csv)
print(doc)
print(txt)

extensions = dict()

extensions[".jpg"] = len(jpg)
extensions[".csv"] = len(csv)
extensions[".doc"] = len(doc)
extensions[".txt"] = len(txt)

print(extensions)

