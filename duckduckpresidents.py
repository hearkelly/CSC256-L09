# JUSTIN BRANCH
# CSC 256.0001
# 7 NOV 2022

# LAB 09: DUCKDUCKGO - Testing


import requests

# import pytest

# list of Presidential Surnames
# ignores Q. "Adams", W. "Bush" and consecutive runs for "Cleveland"
PRESIDENTS = ["Washington", "Jefferson", "Madison", "Monroe", "Adams",
              "Jackson", "Buren", "Harrison", "Tyler", "Polk", "Taylor",
              "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant",
              "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison",
              "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
              "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower",
              "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush",
              "Clinton", "Obama", "Trump", "Biden"]


# returns a list of US President surnames IF name is in string: url>jsonList>'RelatedTopics'>'Text'
def duckDuckPresidents():
    ddgPresList = []

    url = "http://api.duckduckgo.com/?q=\"presidents of the united states\"&format=json"
    response = requests.get(url)
    print(response)

    # list
    jsonList = response.json()
    for surname in PRESIDENTS:  # check each name
        for data in jsonList['RelatedTopics']:  # check each 'Text'
            if surname in data['Text']:
                ddgPresList.append(surname)
                break  # until surname in 'Text'

    return ddgPresList


def test_duckDuckPresidents():
    rList = duckDuckPresidents()  # returns list of surnames in JSON 'RelatedTopics' 'Text'
    assert len(PRESIDENTS) == len(rList)
