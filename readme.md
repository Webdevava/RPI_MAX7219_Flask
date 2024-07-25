# LED Matrix Controller

This project uses a Raspberry Pi with a MAX7219 LED matrix to display scrolling text. The Flask web application allows you to control the LED matrix display through a web interface. It is compatible with any Raspberry Pi model, including the Raspberry Pi Zero.

## File Structure
```
└── 📁RPI_MAX7219
    └── main.py
    └── readme.md
    └── 📁templates
        └── index.html
```


## Pin Connections

Ensure the following pin connections between your Raspberry Pi and the MAX7219 LED matrix:

- **VCC** to **3.3V** (Pin 1 on Raspberry Pi)
- **GND** to **GND** (Pin 6 on Raspberry Pi)
- **DIN** to **MOSI** (Pin 19 on Raspberry Pi, GPIO 10)
- **CS** to **CE0** (Pin 24 on Raspberry Pi, GPIO 8)
- **CLK** to **SCLK** (Pin 23 on Raspberry Pi, GPIO 11)

## Prerequisites

1. Raspberry Pi with Raspbian OS installed (compatible with any model, including Raspberry Pi Zero).
2. Python 3.x and pip installed.
3. MAX7219 LED matrix connected to the Raspberry Pi.

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Ensure `requirements.txt` contains:
    ```
    Flask
    luma.core
    luma.led_matrix
    ```

## Running the Application

1. **Start the Flask application:**

    ```bash
    python app.py
    ```

2. **Access the web interface:**

    Open a web browser and go to `http://<raspberry-pi-ip>:5000` to view and control the LED matrix.

## Usage

- **Enter text** in the input field and click "Send" to scroll the text on the LED matrix.
- **Toggle On/Off** to turn the LED matrix display on or off.
- **Adjust Scroll Speed** using the slider and click "Set Speed" to change the speed of the scrolling text.

## Troubleshooting

- **Ensure correct pin connections** between the Raspberry Pi and MAX7219 LED matrix.
- **Check dependencies** and make sure all packages are installed correctly.
- **Verify Flask server** is running and accessible through the specified IP address.

## Compatibility

This project is compatible with all Raspberry Pi models, including the Raspberry Pi Zero. Ensure that you have the necessary GPIO pins and power requirements based on your specific Raspberry Pi model.
