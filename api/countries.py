from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests 
# import platform 

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        d = dict(query_string_list)

        if "name" in d:
            base_url = "https://restcountries.com/v3.1/name/"
            r = requests.get(base_url + d["name"])
            data = r.json()
     
            country = str(data[0]["name"]["common"])
            capital = str(data[0]['capital'][0])
            message = f"The capital of {country} is {capital}"

        elif "capital" in d:
            pass 
            
        else: 
          message = "Give me a country please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return







# class handler(BaseHTTPRequestHandler): 
#     def do_GET(self):
#         s = self.path
#         url_components = parse.urlsplit(s)
#         query_string_list = parse.parse_qsl(url_components.query)
#         dic = dict(query_string_list)

#         name = dic.get("name")

#         if name:
#             message = f"Aloha {name}"
#         else:
#             message = "Aloha stranger"

#         message += f"\nGreetings from Python version {platform.python_version()}"
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()

#         self.wfile.write(message.encode())

#http://localhost:3000/api/countries?name=Fred
#displays: Aloha Fred  #Greetings from Python version 3.9.10