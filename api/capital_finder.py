from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_com = parse.urlsplit(s)
        query_string = parse.parse_qsl(url_com.query)
        dic = dict(query_string)


        if 'country' in dic:
            value = dic['counrty'].capitalize()
            url='https://restcountries.com/v2/name'
            r=requests.get(url+value)
            data=r.json()
            capital=data[0]['capital']
            message = f'The capital of {value} is {capital}'
        elif 'capital' in dic:
            pass
        else:
            message="provide me with counrty or capital name"



        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
