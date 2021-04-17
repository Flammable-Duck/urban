#!/bin/python
import sys, requests, json, textwrap

def search_urban(word):
    "returns the top definiton of a word at urban dictionary"
    url = "https://api.urbandictionary.com/v0/define"
    querystring = {"term": word}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return data

wrapper = textwrap.TextWrapper(width=70, initial_indent = "     ▍", subsequent_indent = "     ▍")
wrapper_sub = textwrap.TextWrapper(width=70, initial_indent = "      ", subsequent_indent = "      ")


try:
    searchterm = ' '.join(sys.argv[1:])
    data = search_urban(searchterm)
    if not data['list']:
        print("no results found!")
    else:
        definition = wrapper.wrap(text = data['list'][0]['definition'])
        example = wrapper_sub.wrap(text = data['list'][0]['example'])
    
        print("  \033[1m\033[4mFrom The Urban Dictionary:\033[0m")
        print("     " + searchterm + ":")
        for line in definition:
            print(line.replace("[", "").replace("]", ""))
        print("\033[3m\033[2m")
        for line in example:
            print(line.replace("[", "").replace("]", ""))
except:
    print("Urban Search - Search the Urban Dictionary\nUsage: urban <search term>")
