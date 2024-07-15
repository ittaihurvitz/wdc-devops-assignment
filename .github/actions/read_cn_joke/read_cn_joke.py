import os
import sys
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from base import Base

class ChuckNorris(Base):
    """
    This class inherits from Base class.
    Its purpose is to read from Chuck Norris jokes API and return only the joke text.
    """

    def __init__(self):
        super().__init__()

    def add_arguments(self):
        self.parser.add_argument("--url", dest="url", help="url to Chuck Norris API URL", default="https://api.chucknorris.io/jokes/random")

    def prepare(self):
        print("debug prepre")

    def on_exception(self, e):
        print("debugging exception")
        print(e)
        raise

    def run(self):
        print("Start debugging")
        print(self.args.url)
        response = requests.get(self.args.url)
        print(response)
        if response.status_code == 200:
            print("response 200")
            data = response.json()
            print(data)
            joke = data.get("value", "No joke found.")
            print(joke)
        else:
            raise Exception("Failed to retrieve a joke.")

    def on_exception(self, e):
        raise Exception from e

    def on_end(self):
        pass

    def execute(self):
        print("debug execute")
        self.parse_arguments()
        try:
            self.prepare()
            self.run()
        except Exception as e:
            self.on_exception(e)
        finally:
            self.on_end()

if __name__ == '__main__':
    print("running read_cn_joke.py")
    sys.exit(ChuckNorris().execute())
