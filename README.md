# Weather Query App

A simple Flask web application that allows users to query weather information for different cities. The application stores user queries in a MySQL database for tracking purposes.

## Features

- Query weather information for cities
- Store search queries in a MySQL database
- Simple, user-friendly web interface
- Environment variable configuration for database credentials

## Prerequisites

- Python 3.6+
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-query-app.git
   cd weather-query-app
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install flask mysql-connector-python python-dotenv
   ```

4. Set up your MySQL database:
   ```sql
   CREATE DATABASE weather_app;
   USE weather_app;
   CREATE TABLE queries (
       id INT AUTO_INCREMENT PRIMARY KEY,
       city VARCHAR(255) NOT NULL,
       query_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

5. Create a `.env` file in the project root with your database credentials:
   ```
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_DATABASE=weather_app
   ```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Enter a city name in the form and submit to see the weather information.

## Current Supported Cities

The application currently uses hardcoded weather data for the following cities:
- London
- New York
- Tokyo

For any other city, a default weather message will be displayed.

## Project Structure

- `app.py` - The main Flask application
- `templates/index.html` - HTML template for the web interface (not included in this snippet)
- `.env` - Environment variables for database configuration

## Future Improvements

- Integrate with a real weather API
- Add user authentication
- Implement caching for frequent queries
- Add more detailed weather information

## License

This project is licensed under the MIT License - see the LICENSE file for details.