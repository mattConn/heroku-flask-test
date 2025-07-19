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

## Heroku Deployment

### Prerequisites
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- Git repository initialized
- Heroku account

### Deployment Steps

1. **Login to Heroku**:
```bash
heroku login
```

2. **Create a new Heroku app**:
```bash
heroku create your-app-name
```

3. **Set Python buildpack**:
```bash
heroku buildpacks:set heroku/python
```

4. **Deploy to Heroku**:
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

5. **Open your app**:
```bash
heroku open
```

### Automatic Deployment (Push to Main)

To enable automatic deployment when pushing to the main branch:

1. **Connect GitHub repository** in Heroku Dashboard:
   - Go to your app in Heroku Dashboard
   - Navigate to "Deploy" tab
   - Select "GitHub" as deployment method
   - Connect your GitHub repository

2. **Enable automatic deploys**:
   - In the "Automatic deploys" section
   - Select "main" branch
   - Click "Enable Automatic Deploys"
   - Optionally enable "Wait for CI to pass before deploy"

3. **Deploy changes**:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

The app will automatically deploy to Heroku when you push to the main branch.

### Environment Variables
If you need environment variables, set them using:
```bash
heroku config:set VARIABLE_NAME=value
```