import os
import requests
import json

def main():
    url = "https://api.chucknorris.io/jokes/random"
    print(url)
    response = requests.get(url)
    print("The response is:")
    print(response)
    joke = response.json().get('value')
    print("The joke is:")
    print(joke)

if __name__ == "__main__":
    main()
