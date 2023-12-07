# AustriaSkills-Robot-ResponseSimulate
This is a python script that simulates the data from the Austria Skills Robot, which is a robot that was designed and built by my colleagues for the Austria Skills competition. The script sends fake data to the web interface in JSON format via http GET calls.

## What the script does

The script performs the following tasks:

- It loads the initial data from the `robot_status` file, which contains the robot's position, orientation, speed, battery level(*not implemented yet*), and other sensor data.
- It creates a web server using Flask and defines a route for `/robot_status`, which handles the GET requests from the web interface.
- It updates the data by moving the robot along a circular path with a constant angular speed and calculating the elapsed time between the current and previous time.
- It responds to the web interface with the updated data in JSON format and allows cross-origin requests.
- It prints the data to the console for debugging purposes.

## How to run the script

To run the script, you need to do the following steps:

- Clone this repository to your local machine.
- Install the dependencies.
- Run the script.
- Open your web browser and go to `http://localhost:5000/robot_status` (the port could differ) to see the JSON response.
- To test the web interface, go to the [AustriaSkills-Robot-WebInterface](https://github.com/H0lz3r-x64/AustriaSkills-Robot-WebInterface) repository, and follow the README's instructions.
