from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

# https://serverless-fawn-iota.vercel.app/api/aloha?name=Roger
# Hello Roger.  How are you?
# Hello Stranger.  Stranger Danger!
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        self.wfile.write(s.encode())
        return