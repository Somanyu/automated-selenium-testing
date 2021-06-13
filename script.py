from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome("Python/testing/chromedriver.exe")
driver.maximize_window()

def main_page():
    driver.get("https://www.thesparksfoundationsingapore.org/")

    try:
        title = driver.find_element_by_class_name("col-md-6")
        print("Test 1 PASSED!!")
    except NoSuchElementException as exception:
        print("Element not found, test FAILED!!")

    try:
        button_one = driver.find_element_by_class_name("button-w3layouts")
        button_one.click()
        wait = WebDriverWait(driver, 5)
        print("Test 2 PASSED!!")
    except NoSuchElementException as exception:
        print("Element not found, Test FAILED!!")
    except ElementClickInterceptedException:
        print("Button not functioning, Test FAILED!!")


def policy_page():
    driver.get("https://www.thesparksfoundationsingapore.org/policies-and-code/policies/")

    try:
        heading = driver.find_element_by_class_name("inner-tittle-w3layouts")
        print("Test 3 PASSED!!")
    except NoSuchElementException as exception:
        print("Element not found, Test FAILED!!")
    
    try:
        button_two = driver.find_element_by_class_name("button-w3layouts")
        button_two.click()
        wait = WebDriverWait(driver, 5)
        print("Test 4 PASSED!!")
    except NoSuchElementException as exception:
        print("Element not found, Test FAILED!!")
    except ElementClickInterceptedException:
        print("Button not functioning, Test FAILED!!")


def scholarship_page():
    driver.get("https://www.thesparksfoundationsingapore.org/programs/student-scholarship-program/")

    try:
        quote = driver.find_element_by_class_name("para-w3-agile")
        print("Test 5 PASSED!!")
    except NoSuchElementException as exception:
        print("Element not found, Test FAILED!!")
    
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    driver.execute_script("window.scroll(0, 0);")
    sleep(5)
    print("Test 6 PASSED!!")


def joinus_page():
    driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/")

    full_name = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]")
    email = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]")
    role = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select")

    full_name.send_keys("Somanyu Samal")
    sleep(2)
    email.send_keys("example@mail.com")
    sleep(2)
    drop = Select(role)
    drop.select_by_visible_text("Student")
    print("Test 7 PASSED!!")

    sleep(4)

    submit_button = driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]")[0]
    submit_button.click()
    wait = WebDriverWait(driver, 5)
    sleep(4)
    print("Test 8 PASSED!!")
        

def contactus_page():
    driver.get("https://www.thesparksfoundationsingapore.org/contact-us/")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    scroll_btn = driver.find_element_by_id("toTopHover")
    scroll_btn.click()
    sleep(3)
    print("Test 9 PASSED!!")

    driver.execute_script("window.scroll(0, 0);")

    action = ActionChains(driver)
    link1 = driver.find_element_by_link_text("GRIP (Internship)")
    link2 = driver.find_element_by_link_text("Student Scholarship Program")

    action.move_to_element(link1).perform()
    action.move_to_element(link2).perform()
    print("Test 10 PASSED!!")



main_page()
policy_page()
scholarship_page()
joinus_page()
contactus_page()
