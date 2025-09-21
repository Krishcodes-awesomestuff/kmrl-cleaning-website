from flask import Flask, request, jsonify, render_template
from datetime import datetime
import random

# Initialize the Flask app
app = Flask(__name__)

# This dictionary will act as a simple in-memory "database" for this example.
# In a real application, you would save this data to a proper database.
latest_data = {
    "staff_id": None,
    "air_quality": None,
    "last_cleaned": None,
    "daily_count": 0,  # Track trains cleaned today
    "cleaning_history": []  # Store recent cleaning activities
}

@app.route('/')
def dashboard():
    """
    Render the main dashboard with current data
    """
    return render_template('index.html', data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    """
    This function is triggered when the ESP32 sends data.
    It receives the JSON, adds a server-side timestamp, and stores it.
    """
    try:
        data = request.get_json()
        
        # The "last_cleaned" timestamp is generated here on the server
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_only = datetime.now().strftime("%H:%M:%S")
        
        # Update our stored data
        latest_data['staff_id'] = data.get('staff_id')
        latest_data['air_quality'] = data.get('air_quality')
        latest_data['last_cleaned'] = timestamp
        
        # Increment daily count when new cleaning is recorded
        if data.get('staff_id'):
            latest_data['daily_count'] += 1
            
            # Generate random train number for demo
            train_number = random.randint(1, 20)
            
            # Add to cleaning history (keep only last 5 entries)
            cleaning_entry = {
                'time': time_only,
                'staff_id': data.get('staff_id'),
                'train_info': f'Train #KMRL-{train_number:03d} - Cleaning Completed'
            }
            
            latest_data['cleaning_history'].insert(0, cleaning_entry)
            if len(latest_data['cleaning_history']) > 5:
                latest_data['cleaning_history'] = latest_data['cleaning_history'][:5]
        
        # Print the received data to the server console for debugging
        print(f"✅ Data received at {timestamp}:")
        print(f"   Staff ID: {latest_data['staff_id']}")
        print(f"   Air Quality: {latest_data['air_quality']}")
        print(f"   Daily Count: {latest_data['daily_count']}\n")
        
        # Send a success response back to the ESP32
        return jsonify({
            "status": "success", 
            "message": "Data received successfully",
            "daily_count": latest_data['daily_count']
        }), 200

    except Exception as e:
        print(f"❌ Error processing request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/status', methods=['GET'])
def get_status():
    """
    API endpoint to get the current status as JSON
    """
    return jsonify(latest_data)

@app.route('/reset', methods=['POST'])
def reset_daily_count():
    """
    Reset daily count (useful for testing or daily reset)
    """
    latest_data['daily_count'] = 0
    latest_data['cleaning_history'] = []
    return jsonify({"status": "success", "message": "Daily count reset"})

if __name__ == '__main__':
    # 'host=0.0.0.0' makes the server accessible from any device on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)