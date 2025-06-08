# Vercel Python API

This is a Python API project deployed on Vercel's serverless platform. The project provides a simple API endpoint structure using Python.

## Project Structure

```
.
├── api/
│   └── index.py        # Main API handler
├── vercel.json         # Vercel configuration
└── requirements.txt    # Python dependencies
```

## Setup

1. Clone this repository:
```bash
git clone <your-repository-url>
cd vercel-python-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create your API endpoints in the `api/index.py` file.

## Deployment

This project is configured for deployment on Vercel. The `vercel.json` configuration includes:

- Python runtime configuration using `@vercel/python`
- API route configuration directing `/api` to `api/index.py`

To deploy:

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy to Vercel:
```bash
vercel
```

## API Routes

The API is configured with the following route:
- `/api` - Main API endpoint

## Development

To develop locally:

1. Create your API endpoints in the `api/index.py` file
2. Test locally using Vercel CLI:
```bash
vercel dev
```

## License

[Your chosen license]

## Contributing

Feel free to open issues and pull requests! 