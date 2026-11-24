import tkinter as tk
from gpiozero import PWMOutputDevice

# GPIO18 - Physical Pin 12
led = PWMOutputDevice(18, frequency=1000)

led_on = True

def change_brightness(value):
    brightness = int(float(value))
    brightness_label.config(text=f"{brightness}%")

    if led_on:
        led.value = brightness / 100

def turn_on():
    global led_on
    led_on = True
    led.value = brightness_slider.get() / 100
    status_label.config(text="LED STATUS: ON", fg="#22c55e")

def turn_off():
    global led_on
    led_on = False
    led.off()
    status_label.config(text="LED STATUS: OFF", fg="#ef4444")

def close_app():
    led.off()
    led.close()
    root.destroy()


# Main window
root = tk.Tk()
root.title("LED Brightness Controller")
root.geometry("450x400")
root.configure(bg="#101827")
root.resizable(False, False)

root.protocol("WM_DELETE_WINDOW", close_app)

# Heading
tk.Label(
    root,
    text="LED CONTROLLER",
    font=("Arial", 22, "bold"),
    fg="#38bdf8",
    bg="#101827"
).pack(pady=25)

tk.Label(
    root,
    text="Raspberry Pi 4 | GPIO18",
    font=("Arial", 11),
    fg="white",
    bg="#101827"
).pack()

# Brightness percentage
brightness_label = tk.Label(
    root,
    text="50%",
    font=("Arial", 38, "bold"),
    fg="white",
    bg="#101827"
)
brightness_label.pack(pady=20)

# Slider
brightness_slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=330,
    command=change_brightness,
    bg="#1e293b",
    fg="white",
    troughcolor="#38bdf8",
    highlightthickness=0,
    font=("Arial", 11)
)
brightness_slider.set(50)
brightness_slider.pack(pady=10)

tk.Label(
    root,
    text="LED INTENSITY",
    fg="white",
    bg="#101827",
    font=("Arial", 10)
).pack()

# Buttons
button_frame = tk.Frame(root, bg="#101827")
button_frame.pack(pady=25)

tk.Button(
    button_frame,
    text="TURN ON",
    command=turn_on,
    bg="#16a34a",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="flat"
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="TURN OFF",
    command=turn_off,
    bg="#dc2626",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="flat"
).pack(side=tk.LEFT, padx=10)

# Status
status_label = tk.Label(
    root,
    text="LED STATUS: ON",
    fg="#22c55e",
    bg="#101827",
    font=("Arial", 12, "bold")
)
status_label.pack(pady=10)

root.mainloop()