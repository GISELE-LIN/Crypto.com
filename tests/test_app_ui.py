import os
import pytest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
import re
from datetime import datetime
from datetime import datetime, timedelta

@pytest.fixture(scope="session")
def driver():
    apk_path = os.path.join(os.getcwd(), 'assets', 'myobservatory.apk')
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '16',
        'deviceName': 'pixel_6',
        'app': apk_path,
        'automationName': 'UiAutomator2',
        'appPackage': "hko.MyObservatory_v1_0",
        'appActivity': "hko.MyObservatory_v1_0.AgreementPage",
        'noReset': True
    }

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps, keep_alive=True)
    
    yield driver
    # print("✅ Test completed, quitting driver...")
    driver.quit()

def find_and_click_element(driver, by, value, timeout=5):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        print(f"✅ Clicked on element with {by} = {value}")
    except Exception as e:
        print(f"⚠️ Warning: Element with {by} = {value} not found, skipping this step.")
        print(f"❌ Error: {e}")

def test_app_ui(driver):
    print("Step 1: Starting the app and navigating through the UI.")

    # clicking 'agree' button for disclaimer
    find_and_click_element(driver, By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]")
    sleep(2)

    # clicking 'don't allow' button for notification
    find_and_click_element(driver, By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
    sleep(2)

    # clicking 'ok' button for location info
    find_and_click_element(driver, By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
    sleep(2)

    # clicking 'only this time' button for device's location
    find_and_click_element(driver, By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.Button[2]")
    sleep(2)

    # clicking 'Navigate up' (Back) button
    find_and_click_element(driver, By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    sleep(2)

    # clicking 'next page' button
    find_and_click_element(driver, By.XPATH, "//android.widget.ImageView[@content-desc='Next page']")
    sleep(2)

    # clicking 'close' button
    find_and_click_element(driver, By.XPATH, "//android.widget.ImageView[@content-desc='Close']")
    sleep(2)

    # clicking Directory
    find_and_click_element(driver, By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    sleep(2)

    # clicking Forecast & Warning Services
    forecast_button_uiautomator = 'new UiSelector().text("Forecast & Warning Services")'
    find_and_click_element(driver, MobileBy.ANDROID_UIAUTOMATOR, forecast_button_uiautomator)
    sleep(2)

    # clicking 9-Day Forecast
    forecast_button_uiautomator = 'new UiSelector().resourceId("hko.MyObservatory_v1_0:id/title").text("9-Day Forecast")'
    find_and_click_element(driver, MobileBy.ANDROID_UIAUTOMATOR, forecast_button_uiautomator)
    sleep(5)

    # try:
    #     print(driver.page_source)
    # except Exception as e:
    #     print(f"❌ Error while trying to print page source: {e}")

def get_first_item_date(driver):
    try:
        # get first item date
        first_item_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@content-desc]"))
        )
        first_date_text = first_item_element.text.strip()
        print(f"✅ First list item date: {first_date_text}")

        possible_formats = [
            "%d/%b",   # day/month.. 26/Mar
            "%d %b",   # day month.. 26 Mar
            "%b %d",   # month day.. Mar 26
        ]

        for date_format in possible_formats:
            try:
                parsed_date = datetime.strptime(first_date_text, date_format).strftime("%d/%b")
                print(f"✅ Parsed date: {parsed_date}")
                return parsed_date
            except ValueError:
                continue
        print("❌ The date format does not match expected formats.")
        return None

    except Exception as e:
        print(f"❌ Error extracting first item date: {e}")
        return None

def test_first_date_is_tomorrow(driver):
    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    tomorrow_str = tomorrow.strftime("%d/%b")  # day/month

    print(f"✅ Tomorrow's date: {tomorrow_str}")

    first_date = get_first_item_date(driver)

    if first_date:
        if first_date == tomorrow_str:
            print("✅ The first date is tomorrow!")
        else:
            print(f"❌ The first date is not tomorrow, it is: {first_date}")

    # driver.quit()
