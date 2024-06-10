from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os

def parseItem(item):
    if (item.startswith('-')):
        item = item[1:]
    if (item.isdigit()):
        return 1
    else:
        return 0

print("=== CHALLONGE PARSER ===")
bracket = input("> URL: ")
choice = int(input("> Type (0 for Double Elim, 1 for Swiss): "))

req = Request(
    url=bracket,
    headers={'User-Agent': 'Mozilla/5.0'}
)
txt = urlopen(req).read()
soup = BeautifulSoup(txt, features="html.parser")

os.system('cls')
print("=== CHALLONGE PARSER ===")
print(f"> URL: {bracket}")
print(f"> Type (0 for Double Elim, 1 for Swiss): {choice}")

for script in soup(["script", "style"]):
    script.extract()

text = soup.get_text(separator="\n")

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

if (choice == 0):
    start_index = text.find("Finals") + 7
    end_index = text.find("Losers") + 1
    text = text[start_index:end_index]
    text = text.splitlines()
elif (choice == 1):
    rounds = int(input("> Round count: "))
    start_index = text.find(f"Round {rounds}\n") + 8
    text = text[start_index:]
    text = text.splitlines()

elems = {}
for i in range(len(text)):
    if (parseItem(text[i]) == 1):
        elems[i] = int(text[i])
    else:
        elems[i] = text[i]

pick = int(input(("\nWHAT TO DO?\n0 - Show matches\n1 - Show raw text\n2 - Show tabulated matches\n\n> ")))
print()
for i in range(len(elems)-7):
    if (isinstance(elems[i], str) and elems[i]==elems[i+2] and elems[i+4]==elems[i+6] and isinstance(elems[i+4], str)):
        if (pick == 0):
            print(f"Match {elems[i-1]} ~ {elems[i]} | {elems[i+3]} : {elems[i+7]} | {elems[i+4]}")
        elif (pick == 1):
            print(f"{elems[i-1]}\t{elems[i]}\t{elems[i+1]}\t{elems[i+2]}\t{elems[i+3]}\t{elems[i+4]}\t{elems[i+5]}\t{elems[i+6]}\t{elems[i+7]}")
        elif (pick == 2):
            print(f"{elems[i]}\t{elems[i+1]}\t{elems[i+3]}\t{elems[i+7]}\t{elems[i+4]}\t{elems[i+5]}\t{elems[i-1]}")

input()