# Python Firmware for Housefy Project

This Python firmware project is developed for the Housefy project, aimed at monitoring environmental data and uploading it to Firebase. The project includes monitoring temperature, humidity, light intensity, and air quality.

## Features

- Monitors temperature, humidity, CO2, TVOC, and light intensity.
- Calculates Air Quality Index (AQI).
- Uploads monitoring data to Firebase in real-time.
- Displays real-time data on an OLED display.

## Installation

This project requires Python 3.7 or higher. Follow these steps to install the necessary dependencies:

1. Clone the repository:
git clone https://github.com/your-username/your-repository.git
cd your-repository

2. Install dependencies (recommended within a virtual environment):
pip install -r requirements.txt

## Usage

After setting up all the hardware connections, run the main program:
python3 main.py

## Hardware Requirements

- Raspberry Pi (any model)
- Compatible sensors: Temperature & Humidity sensor (e.g., DHT22), Light sensor (e.g., TSL2561), Air Quality sensor (e.g., CCS811)
- OLED display

## Contributing

Contributions are welcome! Please submit your contributions via pull requests or issues.

## License

This project is licensed under the MIT License.

