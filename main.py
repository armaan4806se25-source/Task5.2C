from gpiozero import PWMLED
import tkinter as tk

# LED setup
main_light = PWMLED(18)


def select_room():
    choice = room.get()

    if choice == "Living Room":
        main_light.value = intensity.get() / 100


def change_intensity(value):
    if room.get() == "Living Room":
        main_light.value = float(value) / 100


def exit_program():
    main_light.off()
    window.destroy()


# Create main window
window = tk.Tk()
window.title("Smart Home Light Control")
window.geometry("450x450")

# Heading
title = tk.Label(
    window,
    text="Smart Home Light Control",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Room selection section
room_frame = tk.LabelFrame(
    window,
    text="Select Room",
    padx=15,
    pady=10
)
room_frame.pack(padx=20, pady=10, fill="x")

room = tk.StringVar()
room.set("Living Room")

tk.Radiobutton(
    room_frame,
    text="Living Room",
    variable=room,
    value="Living Room",
    command=select_room
).pack(anchor="w")


# Intensity control section
intensity_frame = tk.LabelFrame(
    window,
    text="Living Room Brightness",
    padx=15,
    pady=15
)
intensity_frame.pack(padx=20, pady=15, fill="x")

intensity = tk.Scale(
    intensity_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=300,
    label="Brightness (%)",
    command=change_intensity
)

intensity.set(50)
intensity.pack()


# Exit button
exit_button = tk.Button(
    window,
    text="Exit",
    width=12,
    command=exit_program
)
exit_button.pack(pady=20)


window.mainloop()