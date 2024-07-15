import os
import requests
import json

def main():
    print("Starting function simple_test")
    url = "https://api.chucknorris.io/jokes/random"
    print(url)
    response = requests.get(url)
    print("simple_test - The response is:")
    print(response)
    joke = response.json().get('value')
    print("simple_test - The joke is:")
    print(joke)

if __name__ == "__main__":
    main()
