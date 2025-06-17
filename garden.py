import keyboard
import threading
import time
from datetime import datetime
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw, ImageFont

# Configurable hours
START_HOUR = 9
END_HOUR = 17
WAIT_INTERVAL = 60  # seconds between cycles
running = True

def is_within_active_hours():
    now = datetime.now()
    return True

def key_hold_loop():
    while running:
        if is_within_active_hours():
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Holding 'A'")
            keyboard.press('a')
            time.sleep(3)
            keyboard.release('a')

            print(f"[{datetime.now().strftime('%H:%M:%S')}] Holding 'D'")
            keyboard.press('d')
            time.sleep(3)
            keyboard.release('d')
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Outside working hours")

        time.sleep(WAIT_INTERVAL)

def create_icon_image():
    image = Image.new('RGB', (64, 64), color='#222222')
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    draw.text((12, 22), "AD", font=font, fill='white')
    return image

def on_quit(icon, item):
    global running
    running = False
    icon.stop()

def setup_tray_icon():
    menu = Menu(MenuItem('Quit', on_quit))
    icon = Icon("KeyPresser", icon=create_icon_image(), menu=menu)
    return icon

if __name__ == "__main__":
    thread = threading.Thread(target=key_hold_loop, daemon=True)
    thread.start()

    tray_icon = setup_tray_icon()
    tray_icon.run()
