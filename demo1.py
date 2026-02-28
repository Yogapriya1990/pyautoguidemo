import pyautogui
import time
import pygetwindow as gw

# Give you time to switch to desktop
time.sleep(2)

# Open browser using Windows search
pyautogui.press('win')
time.sleep(1)
pyautogui.write('chrome')   # or 'edge' / 'firefox'
time.sleep(1)
pyautogui.press('enter')

# Wait for browser to open
time.sleep(5)

# Maximize browser window
browser = gw.getActiveWindow()
browser.maximize()

# Click address bar
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)

# Type Google search
search_query = "south africa vs australia score"
pyautogui.write(search_query, interval=0.05)
pyautogui.press('enter')

# Wait for search results
time.sleep(5)

# Click first result (adjust coordinates if needed)
# These coordinates work for most 1080p screens
pyautogui.moveTo(450, 350, duration=1)
pyautogui.click()

print("Done ✅ Opened first search result")
