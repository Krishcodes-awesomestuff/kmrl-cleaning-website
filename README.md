# KMRL Metro Depot - Cleaning Management System

This project is a web-based dashboard for managing and monitoring the cleaning activities of trains at the KMRL Metro Depot. It provides real-time updates on cleaning progress, air quality, and staff activity.

## Features

- **Dashboard Overview**: Displays the number of trains cleaned, air quality index, current staff on duty, and trains pending cleaning.
- **Recent Cleaning Activities**: Logs the latest cleaning activities with timestamps, staff IDs, and train information.
- **Air Quality Monitor**: Visualizes the air quality index with a status indicator (Good, Moderate, Poor).
- **Daily Cleaning Progress**: Tracks the daily cleaning progress with a progress bar.
- **Control Buttons**: Allows refreshing data and resetting the daily count.

## Project Structure

```
kmrl-cleaning/
├── app.py                # Flask backend for handling API requests and rendering templates
├── templates/
│   └── index.html        # Frontend HTML template for the dashboard
```

## Prerequisites

- Python 3.7 or higher
- Flask library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/kmrl-cleaning.git
   cd kmrl-cleaning
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the dashboard to monitor and manage cleaning activities.

## API Endpoints

- **`GET /`**: Renders the dashboard.
- **`POST /data`**: Receives cleaning data from the ESP32 device.
- **`GET /status`**: Returns the current status as JSON.
- **`POST /reset`**: Resets the daily cleaning count.

## How It Works

1. The ESP32 device sends cleaning data to the `/data` endpoint in JSON format.
2. The server processes the data, updates the in-memory database, and logs the activity.
3. The dashboard dynamically displays the updated data, including cleaning history, air quality, and progress.

## Frontend Details

The dashboard is built using HTML, CSS, and JavaScript. It uses the Jinja2 templating engine to dynamically render data from the Flask backend.

### Key Components

- **Stats Grid**: Displays key metrics like trains cleaned, air quality, and staff on duty.
- **Cleaning Log**: Shows the most recent cleaning activities.
- **Air Quality Panel**: Visualizes the air quality index with a circular meter.
- **Progress Section**: Tracks daily cleaning progress with a progress bar.

## Auto-Refresh

The dashboard automatically refreshes every 15 seconds to fetch the latest data.

## Reset Daily Count

The "Reset Daily Count" button allows resetting the daily cleaning count and clearing the cleaning history.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Font Awesome](https://fontawesome.com/) for icons.
- [Flask](https://flask.palletsprojects.com/) for the backend framework.

## Screenshots

![Dashboard Screenshot](screenshot.png)

---

Feel free to contribute to this project by submitting issues or pull requests!
