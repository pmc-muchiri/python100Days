import csv
import time
import os
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Function to login and play video
def login_and_play(email):
    driver = webdriver.Chrome()  # Change this to the path of your Chrome webdriver
    driver.get("https://www.youtube.com/")

    # Login to YouTube
    email_input = driver.find_element_by_id("identifierId")
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)

    # Wait for the password input field to appear
    time.sleep(2)

    # Enter the password
    password_input = driver.find_element_by_name("password")
    password = password_entry.get()  # Get the password from the entry field
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # Wait for the login to complete
    time.sleep(5)

    # Play a video (replace 'VIDEO_ID' with your desired video ID)
    video_id = 'VIDEO_ID'
    driver.get(f"https://www.youtube.com/watch?v={video_id}")

    # Wait for the video to load
    time.sleep(5)

    # Play the video
    play_button = driver.find_element_by_class_name("ytp-play-button")
    play_button.click()

    # Wait for the video to finish playing
    time.sleep(10)

    # Close the browser
    driver.quit()

# Function to handle button click event
def play_videos():
    csv_file_path = csv_entry.get()  # Get the CSV file path from the entry field
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row['Email']
            login_and_play(email)

# Create the main window
window = tk.Tk()
window.title("YouTube Video Scheduler")

# Create a label for the CSV file path
csv_label = tk.Label(window, text="CSV File Path:")
csv_label.pack()

# Create an entry field for the CSV file path
csv_entry = tk.Entry(window)
csv_entry.pack()

# Create a label for the password
password_label = tk.Label(window, text="Password:")
password_label.pack()

# Create an entry field for the password
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create a button to play videos
play_button = tk.Button(window, text="Play Videos", command=play_videos)
play_button.pack()

# Run the main event loop
window.mainloop()
