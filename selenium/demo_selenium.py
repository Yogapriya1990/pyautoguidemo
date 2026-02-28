from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

service = Service()
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.maximize_window()

try:
    # ===============================
    # FEATURE 1: Title validation
    # ===============================
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title
    print("✅ Feature 1 Passed: Title verified")

    # ===============================
    # FEATURE 2: Login
    # ===============================
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "You logged into a secure area!" in flash
    print("✅ Feature 2 Passed: Login successful")

    # ===============================
    # FEATURE 3: Dropdown (FIXED)
    # ===============================
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = wait.until(
        EC.element_to_be_clickable((By.ID, "dropdown"))
    )

    select = Select(dropdown_element)
    select.select_by_visible_text("Option 1")

    selected = select.first_selected_option.text
    assert selected == "Option 1"
    print("✅ Feature 3 Passed: Dropdown selected")

    # ===============================
    # FEATURE 4: Checkbox
    # ===============================
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']"))
    )

    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    wait.until(lambda d: checkboxes[0].is_selected())
    assert checkboxes[0].is_selected()
    print("✅ Feature 4 Passed: Checkbox selected")

    # ===============================
    # FEATURE 5: Alert
    # ===============================
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = wait.until(EC.alert_is_present())
    alert.accept()

    result = driver.find_element(By.ID, "result").text
    assert "successfully clicked" in result
    print("✅ Feature 5 Passed: Alert handled")

finally:
    time.sleep(2)
    driver.quit()
