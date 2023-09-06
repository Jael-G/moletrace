
<img src="https://raw.githubusercontent.com/Jael-G/moletrace/master/examples/moletrace_banner.png" alt="MoleTrace-banner">
<h1 style="font-size: 75px; margin-left: 20px;">MoleTrace</h1>

MoleTrace is a Python-based cybersecurity application designed for precise location retrieval using Google's geolocation API. It empowers post-access reconnaissance with a comprehensive set of features:

## Features
- **Target Tracking Dashboard**: Monitor all your executed scripts and saved targets through an intuitive Flask-based dashboard.

- **Payload Generator**: Automatically generate deployable scripts that can be executed in accessed target computers to gather necessary data about nearby access points.

- **Interactive Geo-Map**: Visualize the precise locations of your targets as markers in a Leaflet interactive map.

- **SQLite3 Database**: Securely store target data in an embedded SQLite3 database.
## Installation

#### Clone the repository
```
git clone https://github.com/JAEL-G/moletrace.git
```

#### Navigate to the project directory
```
cd moletrace
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

## GUI

The GUI is ran on a flask server and allows easy control and usage of all the features

- #### LANDING

When loaded the server will show the landing page. The GUI consists of three main tabs,
all accessed using a top panel for easy changing of the pages. 

<img src="https://raw.githubusercontent.com/Jael-G/moletrace/master/examples/landing_example.png" alt="Picture of Landing Page">

- #### TARGETS

Shows a table containing all the information of captured targets

<img src="https://raw.githubusercontent.com/Jael-G/moletrace/master/examples/targets_page_example.png" alt="Picture of Targets Page">


- #### PAYLOADS GENERATOR

Generate payloads in the selected language to be executed in target systems
(Only Python and Shell for now)

<img src="https://raw.githubusercontent.com/Jael-G/moletrace/master/examples/payloads_page_example.png" alt="Picture of Payloads Page">

- #### LOCATIONS MAP

Interactive map that allows to see where the locations precisely are. The coordinates in the 
marks pop-up have a hyperlink to the Google Maps page. 

<img src="https://raw.githubusercontent.com/Jael-G/moletrace/master/examples/location_page_example.png" alt="Picture of Payloads Page">
