from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

#Opening of web app
driver.get("https://dev.app.yicom.xyz/")

#region VARIABLE
expected_title = "homepage"
email = "maerryjoylicup@gmail.com"
password = "Password@123"
regemail = "wobime6308@proexbol.com"
expectedmessage = "Please enter a valid email address."
expected_header_text = "登录"
signupGivenname = "Nathaniel"
signupSurname= "Alcantara"
signuoCompanyName = "TOA"
signupEmail = "nathaniel@test.com"
signupPhonenumber = "123456789"
languages = ["UK","HK","CN"]
#endregion

wait = WebDriverWait(driver, 10)
 
#region CHANGE LANGUAGES

for i in range(1, 4):
    hkbtn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/div[" + str(i) + "]"))).click()
    actual_header_text = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/h1"))).get_attribute("innerHTML")
    if actual_header_text == expected_header_text:
        print(f"Test Passed: {languages[i-1]} language matched")
    else:
        print(f"Test Failed: {languages[i-1]} language does not match")

Ukbtn = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[3]/div/div[1]").click()
#endregion 

#region LOG IN

driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/form/div/div/div[1]/div/div/div/input").send_keys(email)
driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/form/div/div/div[2]/div/div/div/div/input").send_keys(password)

# Submit the login form
login_button = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[2]/div[1]/div/div[1]/button").click()
actual_title = driver.title
if actual_title == expected_title:
    print("Test Passed: Actual title matches expected title")
else:
    print("Test Failed: Actual title does not match expected title")
#endregion

#region FORGOT PASSWORD
forgot_password_button = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[2]/div[1]/div/a").click()


# Find the email field, enter the registered email address, and submit the form
email_field = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[2]/form/div/div/div/div/div/div/input").send_keys(regemail)
sendbutton = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[2]/div[2]/button").click()


# Wait for the password reset confirmation message to appear
confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/p"))).get_attribute("innerHTML")
#confirmation_message = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[2]/div[2]/p").text
#print(confirmation_message)
if confirmation_message == expectedmessage:
    print("Test Passed: Actual confirmation matched")
else:
    print("Test Failed:  Actual confirmation does not match")
#endregion


#region SIGN UP
back_button = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[1]/p").click()
signup_button = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[2]/div[1]/div/div[2]/a").click()
given_name = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[5]/form/div/div/div[1]/div/div/div/input").send_keys(signupGivenname)
surname = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[5]/form/div/div/div[2]/div/div/div/input").send_keys(signupSurname)
company_name = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[5]/form/div/div/div[3]/div/div/div/input").send_keys(signuoCompanyName)
signup_email = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[5]/form/div/div/div[4]/div/div/div/input").send_keys(signupEmail)
signup_phone = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[5]/form/div/div/div[5]/div/div/input").send_keys(signupPhonenumber)
checkbox = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[6]/div[1]/span/input").click()
get_access_button = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[6]/button").click()

print ("Sign up successfully")
#endregion

#Close the browser
driver.quit()