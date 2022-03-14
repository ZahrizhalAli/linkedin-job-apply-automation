from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

YOUR_EMAIL = "zzahrizhal.ali@gmail.com"
YOUR_PASSWORD = "Assalamualaikum29"
YOUR_PHONE_NUMBER = "085xxxxxx"

chrome_web_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_web_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102478259&keywords=python&location=Indonesia") # Link filter pekerjaan pastikan sudah benar.

sign_in_btn = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]") # Pake xpath
sign_in_btn.click()

email = driver.find_element_by_name("session_key")
password = driver.find_element_by_name("session_password")

email.send_keys(YOUR_EMAIL)
password.send_keys(YOUR_PASSWORD)

log_in = driver.find_element_by_css_selector("form button")
log_in.click()

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(YOUR_PHONE_NUMBER)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_xpath('//*[@id="ember411"]')
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            # submit_button.click()
            time.sleep(2)
            driver.quit()
        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
