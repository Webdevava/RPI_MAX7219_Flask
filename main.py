from flask import Flask, render_template, request, redirect, url_for
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT
import threading
import time
import os

# Get the absolute path of the current file (main.py)
base_dir = os.path.abspath(os.path.dirname(__file__))

# Define the absolute path to the templates directory
template_dir = os.path.join(base_dir, 'templates')

# Create the Flask app with the absolute template path
app = Flask(__name__, template_folder=template_dir)

# Initialize SPI and LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

# Store the message, scroll speed, and state
current_message = ""
scroll_speed = 0.05
display_thread = None
stop_thread = False
is_display_on = True

def scroll_text():
    global current_message, stop_thread, scroll_speed
    while not stop_thread:
        legacy.show_message(device, current_message, fill="white", font=proportional(CP437_FONT), scroll_delay=scroll_speed)
        time.sleep(0.1)  # Small delay between scrolls

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_message, display_thread, stop_thread, scroll_speed, is_display_on
    if request.method == 'POST':
        if 'message' in request.form:
            new_message = request.form['message']
            if new_message != current_message:
                current_message = new_message
                if display_thread and display_thread.is_alive():
                    stop_thread = True
                    display_thread.join()
                stop_thread = False
                display_thread = threading.Thread(target=scroll_text)
                display_thread.start()
        elif 'toggle' in request.form:
            is_display_on = not is_display_on
            if not is_display_on:
                stop_thread = True
                if display_thread:
                    display_thread.join()
                display_thread = None
        elif 'speed' in request.form:
            try:
                new_speed = float(request.form['speed'])
                if 0.01 <= new_speed <= 1.0:
                    scroll_speed = new_speed
            except ValueError:
                pass
        return redirect(url_for('index'))
    return render_template('index.html', message=current_message, is_display_on=is_display_on, scroll_speed=scroll_speed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
