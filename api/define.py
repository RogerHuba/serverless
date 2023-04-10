from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

# https://serverless-fawn-iota.vercel.app/api/define?word="python"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        given_dictionary = dict(query_string_list)
        word = given_dictionary.get('word')


        self.wfile.write(word.encode())
        return