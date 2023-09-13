from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime as dt



chrome_driver_path = YOUR_CHROME_DRIVER_PATH
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

store = driver.find_element(By.ID, "store")

item = {}
store2 = store.text.split("\n")
newlist = []
for i in range(len(store2)):
    if i % 2 == 0:
        newlist.append(store2[i])

for i in newlist:
    newlist = i.split(" - ")
    item[newlist[0]] = int(newlist[1].replace(",", ""))


second = round(dt.datetime.now().timestamp())
diff = round(dt.datetime.now().timestamp()) - second


finish = second + 30


while round(dt.datetime.now().timestamp()) != finish:
    second = round(dt.datetime.now().timestamp())
    diff = round(dt.datetime.now().timestamp()) - second

    while diff != 5:
        diff = round(dt.datetime.now().timestamp()) - second
        cookie.click()


    max = 0
    max_item = ""
    for i in item:
        upgrade = driver.find_element(By.ID, f"buy{i}")
        if max <= item[i] and upgrade.get_attribute("class") != "grayed":
            max = item[i]
            max_item = i

    upgrade = driver.find_element(By.ID, f"buy{max_item}")
    upgrade.click()


print(cookie.find_element(By.XPATH, '//*[@id="cps"]').text)


driver.quit()