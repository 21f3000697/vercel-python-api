import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import parse_qs, urlparse

        # Parse query parameters
        query = parse_qs(urlparse(self.path).query)
        names = query.get('name', [])

        # Load marks data (list of dicts)
        with open('q-vercel-python.json') as f:
            data = json.load(f)

        # Extract marks for the requested names
        marks = []
        for name in names:
            for entry in data:
                if entry["name"] == name:
                    marks.append(entry["marks"])
                    break  # Stop searching after first match

        # Prepare response
        response = json.dumps({"marks": marks})

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response.encode())
