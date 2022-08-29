import requests
from bs4 import BeautifulSoup
import json
import csv
import lxml
def writeJsonRequest():
    with open("request.json", "w") as f:
        f.write(requests.get("https://www.marvel.com/v1/pagination/grid_cards?offset=0&limit=2667&entityType=character&sortField=title&sortDirection=asc").text)


def writeLinksCsv(fileAdress):
    with open(fileAdress, "r", encoding="utf-8") as request:
        data = json.load(request)["data"]["results"]["data"]
        with open ("charactersLinks.csv", "w", newline="", encoding="utf8") as csv:
            mainLink = "https://www.marvel.com"
            for i in data:
                csv.write(f'{i["headline"]}${i["secondary_text"]}${mainLink+i["link"]["link"]}\n')


def writeCharactersinfoCsv(linksCsvAdress):
    with open(linksCsvAdress, "r", encoding="utf-8") as links:
        with open("charactersInfo.csv", "w", newline="", encoding="utf-8") as charactersCsv:
            NameAndlinksReader = csv.reader(links, delimiter="$")
            writer = csv.writer(charactersCsv, delimiter="%")
            for row in NameAndlinksReader:
                html = requests.get(row[2]).text
                infos = BeautifulSoup(html, "lxml")
                infos = infos.find("div", "accordion-body")

                character = row[0]
                personName = row[1]

                try:
                    universe = infos.find("p", string="Universe").parent.find("ul").text
                except:
                    universe = "unspecified"

                try:
                    other = infos.find("p", string="Other Aliases").parent.find("ul").text
                except:
                    other = "unspecified"

                try:
                    education = infos.find("p", string="Education").parent.find("ul").text
                except:
                    education = "unspecified"

                try:
                    place = infos.find("p", string="Place of Origin").parent.find("ul").text
                except:
                    place = "unspecified"

                try:
                    relatives = infos.find("p", string="Known Relatives").parent.find("ul").text
                except:
                    relatives = "unspecified"

                writer.writerow([character, personName, universe, other, education, place, relatives])


writeJsonRequest()
writeLinksCsv("request.json")
writeCharactersinfoCsv("charactersLinks.csv")
