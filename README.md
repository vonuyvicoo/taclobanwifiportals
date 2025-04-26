
# Captive Portal Bypass (Tacloban Edition)

This project explores techniques for bypassing captive portals commonly found in public Wi-Fi networks, with a focus on those encountered in Tacloban.  
It is intended to demonstrate security gaps in poorly configured or outdated network setups.

---

## 🚨 Disclaimer

This project is intended **for educational purposes only**.  
It is designed to help users understand how captive portals work and explore network behavior in public Wi-Fi environments.

**Unauthorized access to networks is illegal.**  
The author does **not** condone or support any misuse of this tool, and assumes **no responsibility** for any actions taken using the contents of this repository.

> Wi-Fi solutions providers should take note of this security vulnerability.  
> If you need someone to implement proper security measures, contact us at [sanghaya.org](https://sanghaya.org).

Use responsibly and ethically. ⚠️

---

## 🧠 Features
- Lightweight and scriptable
- Selenium-based browser automation

---

## 🔧 Dependencies

Install the required Python package:

```bash
pip install selenium

```

> Make sure you have the correct [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed for your version of Chrome, and that it's accessible in your system's PATH.

----------

## ⚙️ Configuration

Before running the script, open the file and update the following variables:

```python
CHROMEDRIVER_PATH = 'YOUR_CHROMEDRIVER_PATH'
TARGET_URL = 'http://captive.apple.com OR http://gstatic.com/generate_204'
THREAD_COUNT = 15

```

-   `CHROMEDRIVER_PATH`: Full path to your `chromedriver` binary
    
-   `TARGET_URL`: A commonly whitelisted URL used to trigger captive portals, if you're on apple, use captive.apple.com, if you're on windows, use gstatic.com/generate_204
    
-   `THREAD_COUNT`: Number of concurrent browser threads (be cautious not to overload your system or network)
    

----------

## 🚀 Usage

```bash
cd 6-digit/
python [filename.py]

```

Replace `wlan0` with your actual wireless network interface.

----------

## 📜 License

MIT License. See `LICENSE` for details.
