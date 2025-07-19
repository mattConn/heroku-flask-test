# Flask + React Demo

A simple Flask backend with React frontend demonstrating API communication.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

3. Open `index.html` in your browser

## Features

- Flask backend with two API endpoints:
  - `GET /api/hello` - Returns a greeting with timestamp
  - `POST /api/echo` - Echoes back user input
- React frontend with buttons to test both endpoints
- CORS enabled for cross-origin requests

The app demonstrates frontend-backend communication via fetch() calls.