from flask import Flask, request, render_template
import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': os.getenv('DB_USER'),  # Replace with your MySQL username
    'password': os.getenv('DB_PASSWORD'),  # Replace with your MySQL password
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'database': os.getenv('DB_DATABASE'),
}

# Hardcoded weather data (for simplicity)
weather_data = {
    "london": "Rainy, 15°C",
    "new york": "Sunny, 25°C",
    "tokyo": "Cloudy, 20°C",
    "default": "Sunny, 25°C"  # Default message for unknown cities
}


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_message = None
    city = None
    error = None
    connection = None
    cursor = None
    if request.method == 'POST':
        city = request.form.get('city', '').strip().lower()

        if not city:
            error = "Please enter a city name!"
        else:
            # Store the query in MySQL
            try:
                connection = mysql.connector.connect(**db_config)
                cursor = connection.cursor()
                query = "INSERT INTO queries (city) VALUES (%s)"
                cursor.execute(query, (city,))
                connection.commit()
            except mysql.connector.Error as err:
                error = f"Database error: {err}"
            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
            # Get weather message (hardcoded)
            weather_message = weather_data.get(city, weather_data['default'])

    return render_template('index.html', weather_message=weather_message, city=city, error=error)


if __name__ == '__main__':
    app.run(debug=True)
