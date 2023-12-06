from flask import Flask, jsonify
import math
import json
import time
# Define a constant for the desired angular speed in degrees per second
ANGULAR_SPEED = 10
# Initialize a variable to store the previous time
prev_time = time.time()

app = Flask(__name__)


# Define a function that takes the radius, angle, and center coordinates of a circle
def draw_circle(radius, angle, center_x, center_y):
    # Calculate the x and y coordinates of the point on the circle
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    # Return the x and y coordinates and the angle
    return x, y, angle


# Read the data from the file
data = json.load(open("robot_status", "r"))

# Define the initial parameters
radius = 500  # The radius of the circle in pixels
angle = 0  # The initial angle in degrees
center_x = data["xPos"]  # The x coordinate of the center of the circle
center_y = data["yPos"]  # The y coordinate of the center of the circle


@app.route('/robot_status', methods=['GET'])
def robot_status():
    # Declare the angle variable as global
    global angle
    global prev_time
    # Call the draw_circle function and get the x, y, and angle values
    x, y, angle = draw_circle(radius, angle, center_x, center_y)
    data["xPos"], data["yPos"], data["rot"] = x, y, -angle
    # Get the current time
    curr_time = time.time()
    # Calculate the elapsed time in seconds
    elapsed_time = curr_time - prev_time
    # Update the angle by multiplying the angular speed and the elapsed time
    angle += ANGULAR_SPEED * elapsed_time
    # Update the previous time
    prev_time = curr_time

    # Create a JSON response with the data
    response = jsonify(data)
    # Add the header to allow cross-origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')
    # Return the response
    # Convert the values to strings before joining them
    print(" | ".join([str(data["xPos"]), str(data["yPos"]), str(data["rot"])]))
    return response


if __name__ == '__main__':
    # Indent the last two lines
    app.run(debug=True)
    print("The app is running")
