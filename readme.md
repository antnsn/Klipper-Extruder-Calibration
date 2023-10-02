# Klipper Extruder Calibration Tool
A simple web-based tool to assist in calibrating the rotation_distance for extruders in Klipper.

## 🌟 Features
- 🖥 Intuitive form-based interface to input the required measurements.
- 📖 Step-by-step instructions to guide the user through the calibration process.
- 🧮 Computes the new rotation_distance based on user inputs.
- 📋 "Copy to clipboard" feature for easy copying of the computed result.


## 🔧 Setup and Running
1. Prerequisites:
Ensure you have Python installed on your machine.

Install necessary Python libraries: Flask. This can be achieved using the provided requirements.txt file:
```bash
pip install -r requirements.txt
```


2. Running the App:
Navigate to the project directory in your terminal and execute:

```bash
python app.py
```


Once the Flask server is up and running, open your web browser and go to:

```bash
http://127.0.0.1:5000/
```

## 📘 Usage
Follow the on-screen instructions. Input the necessary measurements and let the tool compute the new rotation_distance for your Klipper extruder.

## 🐳 Docker Support
For those who prefer running applications in containers, the Klipper Extruder Calibration Tool is available on Docker Hub.

You can pull and run the docker image directly from mrplecto/klipper-extruder-calibrate repository:

```bash
docker pull mrplecto/klipper-extruder-calibrate
docker run -p 5000:5000 mrplecto/klipper-extruder-calibrate
```

After executing the above commands, the tool should be accessible in your browser at http://localhost:5000.

This provides a streamlined way to run the calibration tool without having to set up the environment locally.