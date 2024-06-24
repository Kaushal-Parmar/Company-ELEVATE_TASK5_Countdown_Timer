import time
import tkinter as tk
from tkinter import messagebox

def countdown(seconds):
    start_time = time.time()
    end_time = start_time + seconds
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes, seconds = divmod(remaining_seconds, 60)
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
    print("\nTime's up!")

def main():
    print("Welcome to the Countdown Timer!")
    duration = int(input("Enter the duration in seconds: "))
    countdown(duration)

if __name__ == "__main__":
    main()




class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        self.label = tk.Label(self.root, text="Enter duration in seconds:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)
    
    def start_timer(self):
        try:
            duration = int(self.entry.get())
            self.root.after(0, self.countdown, duration * 1000)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number of seconds.")
    
    def countdown(self, milliseconds):
        remaining_seconds = milliseconds / 1000
        end_time = time.time() + remaining_seconds
        while time.time() < end_time:
            remaining_seconds = int(end_time - time.time())
            minutes, seconds = divmod(remaining_seconds, 60)
            self.label.config(text=f"Time remaining: {minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
        messagebox.showinfo("Countdown Timer", "Time's up!")

def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
