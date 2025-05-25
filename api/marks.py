import json

def handler(request, response):
    # Load marks data from the JSON file
    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)

    # Extract all "name" parameters from the query string
    names = request.query.getall("name", [])
    
    # Retrieve marks for each name (0 if not found)
    marks = [data.get(name, 0) for name in names]

    # Return JSON response with CORS headers
    return response.json(
        {"marks": marks},
        status=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type"
        }
    )
