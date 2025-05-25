import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import parse_qs, urlparse

        query = parse_qs(urlparse(self.path).query)
        names = query.get('name', [])

        with open('q-vercel-python.json') as f:
            data = json.load(f)  # data is a list of dicts

        marks = []
        for name in names:
            found = False
            for entry in data:
                if entry["name"] == name:
                    marks.append(entry["marks"])
                    found = True
                    break
            # If you want to append None for missing names, uncomment below:
            # if not found:
            #     marks.append(None)

        response = json.dumps({"marks": marks})

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response.encode())
