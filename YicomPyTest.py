import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

expected_title = "Login | YICOM"
expected_message = "Please enter a valid email address."
expected_header_texts = ['Login','登錄', '登录'] 
signupexpected_title = "Registration | YICOM"
email = "maerryjoylicup@gmail.com"
password = "Password@123"
regemail = "wobime6308@proexbol.com"
signupGivenname = "Ted Kuhic"
signupSurname = "Alcantara"
signuoCompanyName = "TOA"
signupEmail = "nathaniel@test.com"
signupPhonenumber = "123456789"
languages = ["UK", "HK", "CN"]

    
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_change_languages(driver):
    # Opening of web app
    driver.get("https://dev.app.yicom.xyz/")

   

    wait = WebDriverWait(driver, 10)

    for i in range(1, 4):
        language_btn = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div/div/div/div/div[3]/div/div[{i}]")))
        language_btn.click()
        actual_header_text = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/h1"))).get_attribute("innerHTML")
        assert actual_header_text == expected_header_texts[i-1], f"{languages[i-1]} language does not match"

    Ukbtn = driver.find_element("xpath", "/html/body/div/div/div/div/div/div[3]/div/div[1]").click()


def test_login(driver):
    # Opening of web app
    
    wait = WebDriverWait(driver, 10)

    # Fill in login form
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/form/div/div/div[1]/div/div/div/input")))
    email_input.send_keys(email)
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/form/div/div/div[2]/div/div/div/div/input")))
    password_input.send_keys(password)

    # Submit login form
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/div[1]/button")))
    login_button.click()

    # Check if login successful
    actual_title = driver.title
    assert actual_title == expected_title, "Actual title does not match expected title"
    print("Test Passed: Actual title matches expected title")

#forgot password
def test_forgot_password(driver):
    # Click on forgot password button
    forgot_password_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/a").click()

    # Find the email field, enter the registered email address, and submit the form
    email_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/form/div/div/div/div/div/div/input")
    email_field.send_keys(regemail)
    send_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/button")
    send_button.click()

    # Wait for the password reset confirmation message to appear
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/p"))).get_attribute(
        "innerHTML")

    # Verify confirmation message
    
    assert confirmation_message == expected_message, "Test Failed: Actual confirmation does not match"
    print("Test Passed: Actual confirmation matched")

#sign-up

def test_signup_form(driver):
    # Click on back button
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/p").click()

    # Click on signup button
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div/div[2]/a").click()

    # Fill up the form fields
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[5]/form/div/div/div[1]/div/div/div/input").send_keys(signupGivenname)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[5]/form/div/div/div[2]/div/div/div/input").send_keys(signupSurname)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[5]/form/div/div/div[3]/div/div/div/input").send_keys(signuoCompanyName)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[5]/form/div/div/div[4]/div/div/div/input").send_keys(signupEmail)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[5]/form/div/div/div[5]/div/div/input").send_keys(signupPhonenumber)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[6]/div[1]/span/input").click()  # Click on the checkbox
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[6]/button").click()  # Click on the get access button

    signupactual_title = driver.title
    assert signupactual_title== signupexpected_title, "Actual sign up title does not match expected title"
    print("Test Passed: Actual sign up title matches expected title")
# #Close the browser
# driver.quit()
                            