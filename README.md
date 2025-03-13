# NAVEE PIN Brute-Force Tool

This project automates the process of brute-forcing the **4-digit PIN** on a **NAVEE Electric Scooter** using **Android UI automation** via `uiautomator2` or **ADB commands**.

---

## 🔹 **Features**
 Automatically **enters PINs** from `9999` down to `0000`  
 Uses **Android UI automation** via `uiautomator2`  
 **Stops immediately** when the correct PIN is found  
 **Fast execution** with optimized input methods  

---

## 🛠 **Requirements**
- Python `3.8+`
- Android phone with **USB Debugging enabled**
- Installed `adb` (Android Debug Bridge)
- Installed Python dependencies

---

##  **Installation & Setup**
### **1️⃣ Install ADB (Android Debug Bridge)**
- **Windows:** Download [platform-tools](https://developer.android.com/studio/releases/platform-tools) and extract.
- **Linux/macOS:** Install via terminal:
```bash
    sudo apt install adb   # Ubuntu/Debian
    brew install adb       # macOS (Homebrew)
``` 

### **2️⃣ Install Required Python Packages**
```bash
pip install uiautomator2
```

### **3️⃣ Enable Developer Mode on Android**
Go to Settings > About Phone
Tap "Build Number" 7 times to enable Developer Mode
Enable USB Debugging under Developer Options

### **4️⃣ Connect Android Device**
Ensure ADB detects your phone:
```bash
adb devices
```
*Note: If the phone shows as unauthorized, accept the USB Debugging prompt on your phone.*


### **Run the Brute-Force Script**
python brute_force_navee.py
