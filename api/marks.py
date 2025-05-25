import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import parse_qs, urlparse

        # Parse query parameters
        query = parse_qs(urlparse(self.path).query)
        names = query.get('name', [])

        # Load marks data
        with open('q-vercel-python.json') as f:
            data = json.load(f)

        # Extract marks for the requested names
        marks = []
        for name in names:
            mark = data.get(name)
            if mark is not None:
                marks.append(mark)
            else:
                marks.append(None)

        # Prepare response
        response = json.dumps({"marks": marks})

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response.encode())
        return
