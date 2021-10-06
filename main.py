from selenium import webdriver


chrome_web_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_web_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102478259&keywords=python&location=Indonesia")

