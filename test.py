from appium import webdriver
from time import sleep

# 设置 Desired Capabilities
desired_caps = {
    'platformName': 'Android',  # 平台设置为 Android
    'platformVersion': '16',    # Android 模拟器的版本，根据你使用的模拟器版本调整
    'deviceName': 'pixel_6',  # 模拟器设备名称，可以通过 adb devices 确认设备名称
    'appPackage': 'com.android.calculator2',  # 設置需要啟動的應用包名（計算機應用）
    'appActivity': 'com.android.calculator2.Calculator',  # 設置應用的啟動 Activity
    'noReset': True  # 不重置應用狀態
}
# 建立 WebDriver 連接到 Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待應用啟動
sleep(3)

# 在計算機應用中執行簡單的操作，例如計算 2 + 3
driver.find_element_by_id('com.android.calculator2:id/digit_2').click()  # 點擊數字 2
driver.find_element_by_id('com.android.calculator2:id/op_add').click()  # 點擊加號
driver.find_element_by_id('com.android.calculator2:id/digit_3').click()  # 點擊數字 3
driver.find_element_by_id('com.android.calculator2:id/eq').click()  # 點擊等號

# 等待結果顯示
sleep(3)

# 確認結果是否顯示為 5
result = driver.find_element_by_id('com.android.calculator2:id/result').text
print(f'計算結果是: {result}')  # 應該顯示 5

# 關閉應用
driver.quit()