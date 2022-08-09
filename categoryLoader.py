import json

file = "dictionary.json"
with open(file, 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)


def get_dictionary():
    return dictionary


def get_categories():
    return dictionary["categories"]


def get_known():
    return dictionary["known"]
