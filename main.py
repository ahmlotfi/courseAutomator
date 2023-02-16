import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 2022-2023 Winter
# Computer Science

email = str(input("Enter your email: "))
password = str(input("Enter your password: "))
year = str(input("Enter the year: "))
subject = str(input("Enter the subject: "))


driver = webdriver.Chrome(r'C:\Users\ahmla\OneDrive\Desktop\MUN\projects\leChcker\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://selfservice.mun.ca/admit/bwskfcls.p_sel_crse_search');
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(email)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

password_field.send_keys(Keys.ENTER)

term = driver.find_element(By.NAME, "p_term")
term.send_keys(year)
#
submit = driver.find_element(By.XPATH, "/html/body/div[4]/form/input[2]")
submit.click()

subjectDriver = driver.find_element(By.ID, "subj_id")
subjectDriver.send_keys(subject)

submit2 = driver.find_element(By.NAME, "SUB_BTN")
submit2.click()

num = 4
for i in range(100):
    try:
        courses = driver.find_element(By.XPATH, ("/html/body/div[4]/table[2]/tbody/tr[" + str(num) + "]/td[3]/form/input[30]"))
        courses.click()
        num += 1
        time.sleep(2)
        driver.back()
        time.sleep(2)
    except:
        break


time.sleep(1000) # Let the user actually see something!
time.sleep(1000) # Let the user actually see something!
driver.quit()
