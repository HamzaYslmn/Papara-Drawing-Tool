import time
import pyautogui
import keyboard
from PIL import Image

pyautogui.PAUSE = 0.03

def get_mouse_position(prompt):
    input(f"{prompt}\nHazır olduğunuzda Enter'a basın ve farenizi o noktaya getirin...")
    return pyautogui.position()

# --- Capture the Drawing Area ---
print("Paint (veya çizim yapmak istediğiniz program) penceresini açın ve çizim alanının görünür olduğundan emin olun.")

# Select the drawing area's TOP RIGHT and BOTTOM LEFT corners.
top_right = get_mouse_position("Çizim alanının SAĞ ÜST köşesini seçin")
bottom_left = get_mouse_position("Çizim alanının SOL ALT köşesini seçin")

# Compute the drawing area's boundaries based on the selected corners.
# Top-left coordinate for the drawing area:
draw_x = bottom_left.x   # left boundary
draw_y = top_right.y     # top boundary
draw_width = top_right.x - bottom_left.x
draw_height = bottom_left.y - top_right.y

print(f"Seçilen alan - Sol Üst: ({draw_x}, {draw_y}), Genişlik: {draw_width}, Yükseklik: {draw_height}")

# --- Load the Image and Fit It to the Drawing Area ---
try:
    image = Image.open("image.png").convert("RGB")
except Exception as e:
    print("Resim açılamadı:", e)
    exit(1)

# Fit the image to the drawing area while preserving its aspect ratio.
scale_factor = min(draw_width / image.width, draw_height / image.height)
new_width = int(image.width * scale_factor)
new_height = int(image.height * scale_factor)
scaled_image = image.resize((new_width, new_height))

# Calculate offsets to center the scaled image in the drawing area.
offset_x = draw_x + (draw_width - new_width) // 2
offset_y = draw_y + (draw_height - new_height) // 2

print("Çizim 5 saniye içinde başlayacak. Lütfen çizim programınıza geçin.")
time.sleep(5)

threshold = 30  # Pixel will be drawn if any channel is below this value.
cancelled = False

# --- Drawing Loop ---
for y in range(new_height):
    if keyboard.is_pressed('esc'):
        cancelled = True
        break
    x = 0
    while x < new_width:
        if keyboard.is_pressed('esc'):
            cancelled = True
            break
        r, g, b = scaled_image.getpixel((x, y))
        # Draw if the pixel is not nearly white
        if r < threshold or g < threshold or b < threshold:
            start_x = x
            while x < new_width:
                r2, g2, b2 = scaled_image.getpixel((x, y))
                if not (r2 < threshold or g2 < threshold or b2 < threshold):
                    break
                x += 1
            screen_start_x = offset_x + start_x
            screen_end_x = offset_x + x - 1
            screen_y = offset_y + y
            pyautogui.moveTo(screen_start_x, screen_y, duration=0)
            pyautogui.mouseDown()
            pyautogui.moveTo(screen_end_x, screen_y, duration=0)
            pyautogui.mouseUp()
        else:
            x += 1
    if cancelled:
        break

if cancelled:
    print("Çizim iptal edildi!")
else:
    print("Çizim tamamlandı!")
