from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# https://serverless-fawn-iota.vercel.app/api/define?word="python"
# "https://api.dictionaryapi.dev/api/v2/entries/en/python"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        given_dictionary = dict(query_string_list)
        word = given_dictionary.get('word')

        base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        new_url = base_url + word
        req = requests.get(new_url)
        data = req.json
        definitions = []
        for word_data in data:
            definition = word_data["meanings"][0]["definitions"][0]["definition"]
            definitions.append(definition)
        message = str(definitions)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return

    # [{"word": "python", "phonetics": [
    #     {"audio": "https://api.dictionaryapi.dev/media/pronunciations/en/python-au.mp3",
    #      "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=79268748",
    #      "license": {"name": "BY-SA 4.0", "url": "https://creativecommons.org/licenses/by-sa/4.0"}},
    #     {"text": "/ˈpaɪθən/", "audio": ""}, {"text": "/ˈpaɪθɑːn/", "audio": ""}], "meanings": [
    #     {"partOfSpeech": "noun",
    #      "definitions": [{"definition": "A type of large constricting snake.", "synonyms": [], "antonyms": []},
    #                      {"definition": "Penis", "synonyms": [], "antonyms": []}], "synonyms": [], "antonyms": []}],
    #   "license": {"name": "CC BY-SA 3.0", "url": "https://creativecommons.org/licenses/by-sa/3.0"},
    #   "sourceUrls": ["https://en.wiktionary.org/wiki/python"]}]