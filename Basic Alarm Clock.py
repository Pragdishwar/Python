import time
import datetime
import winsound  # Only works on Windows. For Linux, use the 'playsound' module.

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}...")

    while True:
        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("Wake up! It's time!")
            # Play the alarm sound (for Windows, use winsound; for other OS, you can use a sound library like playsound)
            winsound.Beep(1000, 1000)  # Beep sound: frequency 1000Hz for 1000 milliseconds
            
            break
        
        # Sleep for a short time to reduce CPU usage
        time.sleep(1)

# Get the user input for the alarm time (in HH:MM:SS format)
alarm_time = input("Enter the alarm time in HH:MM:SS format: ")

# Call the alarm function
set_alarm(alarm_time)
