import re
import json
path = input("enter the path of the file: ")
class File():
    def getfile(self):
        txt = open(path, "r")
        text = txt.read()
        txt.close()
        return text

tet = File()
print(tet.getfile())

class calculate():
    def __init__(self, text):
        self.text = text
    def frases(self):
        counter = 0
        for i in self.text:
            if i == "." or i == "?" or i == "!":
                counter += 1
        return counter
    def words(self):
        return len(self.text.split(" ")) + (self.frases() -1)
    def ConV(self):
        listv = ["a","e","i","o","u","y"]
        counterv = 0
        counterc = 0
        for i in self.text:
            if i.lower() in listv:
                counterv +=1
            elif i != "?" and i != "!" and i !="." and i != " " and i.lower not in listv:
                counterc +=1
        return(f"there are {counterv} voyals and {counterc} consones")
    def maxv(self):
        listv = ["a","e","i","o","u","y"]
        vdict = {}
        for i in self.text:
            if i.lower() in listv:
                try:
                    vdict[i.lower()] +=1
                except:
                    vdict[i.lower()] = 1
        temp = 0
        tempv = ""
        for j , i in vdict.items():
            if i > temp:
                temp = i
                tempv = j

        return(f"there are {vdict} and the highes value is {tempv} with {temp}")
    def maxword(self):
        dictionary = {}
        for i in re.split(r"\n| |\.|\,", self.text):
            if i != "" and i != " ":
                try:
                    dictionary[i.lower()] +=1
                except:
                    dictionary[i.lower()] =1
        temp = 0
        tempv = ""
        for j , i in dictionary.items():
            if i > temp:
                temp = i
                tempv = j
        return(f"the word with the highes repeats is {tempv} with {temp} repeats")

calc = calculate(tet.getfile())

class openwritefile():
    def __init__(self, data):
        self.data = data
    def openwritejson(self):
        jsonfile = open("data.json", "w")
        json.dump(self.data, jsonfile)
data = f"there are {calc.frases()} frases, {calc.words()} words, {calc.ConV()} , {calc.maxv()}, {calc.maxword()} "
final = openwritefile(data)
final.openwritejson()