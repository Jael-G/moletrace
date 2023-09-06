<div style="display: flex; align-items: center;">
  <img src="https://raw.githubusercontent.com/JAEL-G/MoleTrace/blob/master/web/static/img/moletrace_logo.png" alt="MoleTrace-logo" width="175" height="175">
  <h1 style="font-size: 75px; margin-left: 20px;">MoleTrace</h1>
</div>

MoleTrace is a Python-based cybersecurity application designed for precise location retrieval using Google's geolocation API. It empowers post-access reconnaissance with a comprehensive set of features:

## Features
- **Target Tracking Dashboard**: Monitor all your executed scripts and saved targets through an intuitive Flask-based dashboard.

- **Payload Generator**: Automatically generate deployable scripts that can be executed in accessed target computers to gather necessary data about nearby access points.

- **Interactive Geo-Map**: Visualize the precise locations of your targets as markers in a Leaflet interactive map.

- **SQLite3 Database**: Securely store target data in an embedded SQLite3 database.
## Installation

#### Clone the repository
```
git clone https://github.com/JAEL-G/MoleTrace.git
```

#### Navigate to the project directory
```
cd MoleTrace
```

#### Install dependencies
```
pip install -r requirements.txt
```

#### Update .env API key
```
# .env
API_KEY="GOOGLE_GEOLOCATION_API_KEY"
```

#### Create Database
```
python generate_database.py
```

#### Run the application
```
python moletrace.py
```
## Usage
- Access the Web Dashboard via the opened server
- Generate executable payloads to run on target computers
- Obtain and save the location of targets