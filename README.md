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
- Selenium-based browser automation (Python)
- JavaScript-based portal poking

---

## 🔧 Dependencies

Install the required Python package:

```bash
pip install selenium
```

> Make sure you have the correct [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed for your version of Chrome, and that it's accessible in your system's `PATH`.

---

## ⚙️ Configuration

Before running the Python script, open the file and update the following variables:

```python
CHROMEDRIVER_PATH = 'YOUR_CHROMEDRIVER_PATH'
TARGET_URL = 'http://captive.apple.com'  # or 'http://gstatic.com/generate_204'
THREAD_COUNT = 15
```

- `CHROMEDRIVER_PATH`: Full path to your `chromedriver` binary
- `TARGET_URL`: A commonly whitelisted URL used to trigger captive portals. If you’re on Apple devices, use `captive.apple.com`; if on Windows, use `gstatic.com/generate_204`
- `THREAD_COUNT`: Number of concurrent browser threads (be cautious not to overload your system or network)

---

## 🚀 Usage (Python)

```bash
cd 6-digit/
python bypass_portal.py --interface wlan0
```

Replace `wlan0` with your actual wireless network interface.

---

## 🚀 Usage (JavaScript)

You can run our lightweight JavaScript scripts directly in the captive portal page without Python:

1. Open the Wi-Fi captive portal in your browser.
2. Navigate to the **JavaScript-based** folder in this repo:
   ```
   javascript-based/cafe.js
   ```
3. Copy the contents of the desired `.js` file.
4. Open your browser's Developer Console (usually `F12` or `Ctrl+Shift+I`).
5. Paste the JavaScript code into the console and press `Enter`.

Alternatively, you can inject the script via the URL bar:

1. Prefix the code with `javascript:`. If your script is:
   ```js
   // sample cafe.js code
   for (let i = 0; i < 1000; i++) {
     /* ... */
   }
   ```
2. Convert it to a single-line bookmarklet:
   ```text
   javascript:(function(){/* code here */})();
   ```
3. Paste that entire line into the URL bar and hit `Enter`.

---

## ❓ Why Python and Not Just JavaScript?

- **Cross-Origin Automation**: Python with Selenium can control the browser at a network level, handling redirects and cross-origin requests that browser console scripts may be restricted from due to the same-origin policy.
- **Headless and Batch Runs**: Automated, headless runs with Python allow unattended testing across many SSIDs or portals, whereas JavaScript console injections require manual steps.
- **Parallelization & Scalability**: Python’s threading (or async) libraries let you spawn multiple browser instances to test many login codes simultaneously.

---

## 🔄 Multithreading & Time Complexity

Captive portals often use numeric PINs or codes of length _n_. A brute‑force approach must try up to \(10^n\) combinations. As _n_ increases, the total attempts grow exponentially:

- 4-digit PIN: \(10^4 = 10{,}000\) possibilities
- 6-digit PIN: \(10^6 = 1{,}000{,}000\) possibilities

Serially trying each code would take too long. By using multiple threads (e.g., `THREAD_COUNT = 15`), we distribute the workload across concurrent browser instances, roughly reducing the total wall‑clock time by a factor close to the number of threads (barring network and CPU limits).

---

## 📜 License

MIT License. See `LICENSE` for details.

