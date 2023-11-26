import tkinter as tk
from random import choice
import time

USER_TYPED_WORD = ""
LONG_SENTENCE = [
    "The quick brown fox jumps over the lazy dog, exploring the vast wilderness with curiosity and grace, while the moon shines brightly in the night sky, casting a gentle glow upon the landscape.",
    "In a world full of complexities and uncertainties, it is essential to find moments of tranquility and peace, allowing the mind to unwind and the soul to connect with the beauty that surrounds us.",
    "As the sun sets on the horizon, painting the sky with hues of orange and pink, we reflect on the journey of life, embracing the challenges and cherishing the moments that define who we are.",
    "Amidst the chaos of modern living, we often forget to appreciate the simple pleasures—a warm cup of tea, the rustle of leaves in the wind, and the laughter of loved ones echoing in the air.",
    "With every keystroke, we weave the tapestry of our thoughts and ideas, creating a narrative that unfolds with each passing moment, a testament to the power of expression and the art of communication.",
    "Time is a relentless force, marching forward with unwavering determination, yet within its ceaseless flow, we find opportunities to make a difference, to leave an imprint that transcends the boundaries of existence."
]

CHAR_COUNT = 0
CURRENT_CHAR_COUNT = []

def generate_random_sentence():
    return choice(LONG_SENTENCE)

def start_timer():
    text_to_type.config(text=generate_random_sentence())
    text_area.delete('1.0', tk.END)  # Clear the text area

def stop_timer():
    text_to_type.config(text=generate_random_sentence())
    text_area.delete('1.0', tk.END)

def find_speed(current_char_count, char_count):
    if char_count > 1:
        current_timestamp = current_char_count[char_count - 1]
        last_timestamp = current_char_count[char_count - 2]
        difference = current_timestamp - last_timestamp
        return difference
    return 0

def keep_trace(event):
    global USER_TYPED_WORD, CHAR_COUNT, CURRENT_CHAR_COUNT
    timestamp = int(time.time())
    char = event.char
    USER_TYPED_WORD += char
    CHAR_COUNT += 1
    CURRENT_CHAR_COUNT.append(timestamp)

    words_typed = tk.Label(app, text=USER_TYPED_WORD, font=custom_font)
    words_typed.grid(row=4, column=0, sticky='w')

    typing_speed = find_speed(CURRENT_CHAR_COUNT, CHAR_COUNT)
    trace_typed = tk.Label(app, text=f"User Speed= {typing_speed:.2f} characters per second", font=custom_font)
    trace_typed.grid(row=4, column=1, sticky='w')

app = tk.Tk()
app.title("Typing Speed Calculator")
custom_font = ("Arial", 14, "bold")

label = tk.Label(app, text="Typing Speed Calculator", font=custom_font)
label.grid(row=0, column=0, columnspan=2)

your_text_to_type = tk.Label(app, text="Your sentence to be typed within a minute", font=custom_font)
your_text_to_type.grid(row=1, column=0, sticky='w')

text_to_type = tk.Label(app, text=generate_random_sentence(), font=custom_font)
text_to_type.grid(row=1, column=1, sticky='w')

text_area = tk.Text(app, width=40, height=5, wrap=tk.WORD)
text_area.grid(row=2, column=0, columnspan=2)

start_button = tk.Button(app, text="Start the timer", command=start_timer)
start_button.grid(row=3, column=0, columnspan=2, sticky='w')

stop_button = tk.Button(app, text="Stop the timer", command=stop_timer)
stop_button.grid(row=3, column=1, columnspan=2, sticky='w')

canvas_width = 600
canvas_height = 500
canvas = tk.Canvas(app, width=canvas_width, height=canvas_height)
canvas.grid(row=4, column=0, columnspan=2, sticky='w')

text_area.bind('<Key>', keep_trace)
app.mainloop()
