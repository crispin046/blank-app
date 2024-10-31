from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for crops
crops = [
    {"id": 1, "name": "Tomato", "optimal_soil": "Loamy", "pest": "Aphid"},
    {"id": 2, "name": "Wheat", "optimal_soil": "Clay", "pest": "Locust"},
]

# Get all crops
@app.route('/crops', methods=['GET'])
def get_crops():
    return jsonify(crops)

# Get a specific crop by ID
@app.route('/crops/<int:crop_id>', methods=['GET'])
def get_crop(crop_id):
    crop = next((crop for crop in crops if crop['id'] == crop_id), None)
    if crop is not None:
        return jsonify(crop)
    return jsonify({"error": "Crop not found"}), 404

# Add a new crop
@app.route('/crops', methods=['POST'])
def add_crop():
    new_crop = request.json
    new_crop['id'] = len(crops) + 1  # Simple ID assignment
    crops.append(new_crop)
    return jsonify(new_crop), 201

# Basic weather info endpoint (placeholder)
@app.route('/weather', methods=['GET'])
def get_weather():
    # Placeholder for weather data
    return jsonify({"temperature": "22°C", "condition": "Sunny"})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
