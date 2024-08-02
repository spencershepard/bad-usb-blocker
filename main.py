# This script will monitor keyboard input to try to detect malicious USB devices emulating a keyboard.
# It will detect if key presses are faster than human input. It will then insert additional key input to disrupt the attack.

import keyboard
import random

class Blocker:
    def __init__(self, kps_speed_limit=10):
        self.last_key_time = 0
        self.kps_speed_limit = kps_speed_limit
        self.keys_to_insert = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        self.keys_to_monitor = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        self.last_key_pressed = ""
        self.key_press_times = [] # Buffer of key press times, limited to 10
        print("Blocker initialized with speed limit: " + str(self.kps_speed_limit) + "kps")

    def on_key_press(self, event):

        if event.name not in self.keys_to_monitor:
            return
        
        # Ignore held keys
        if self.last_key_pressed == event.name:
            return
        else:
            self.last_key_pressed = event.name
        
        # Calculate key press speed
        current_time = event.time
        self.key_press_times.append(current_time)
        if len(self.key_press_times) > 10:
            self.key_press_times.pop(0)

        # Calculate average key presses per second
        average_kps = 0
        if len(self.key_press_times) > 1:
            average_kps = len(self.key_press_times) / (self.key_press_times[-1] - self.key_press_times[0])
        
        # If key presses are faster than the speed limit, insert additional key
        if average_kps > self.kps_speed_limit:
            print("Detected fast key presses. Inserting additional key.")
            random_case = random.randint(0, 1)
            random_key = self.keys_to_insert[random.randint(0, len(self.keys_to_insert) - 1)]
            if random_case == 0:
                random_key = random_key.upper()

            # Type the random key    
            keyboard.write(random_key)

        self.last_key_time = event.time
        print("KPS: " + str(average_kps))


blocker = Blocker(kps_speed_limit=10)
keyboard.on_press(blocker.on_key_press)
keyboard.wait()