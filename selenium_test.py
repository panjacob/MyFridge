from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    # Register
    driver.find_element_by_link_text("Login").click()
    time.sleep(2)
    driver.find_element_by_link_text("Create an account").click()
    time.sleep(2)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("daszke2137")
    driver.find_element_by_xpath('//input[@name="password1"]').send_keys("iloveallezon")
    driver.find_element_by_xpath('//input[@name="password2"]').send_keys("iloveallezon")    
    driver.find_element_by_xpath('//button[text()="Register"]').click()
    time.sleep(2)

    # Log in
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("daszke2137")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("iloveallezon")
    driver.find_element_by_xpath('//button[text()="Login"]').click()
    time.sleep(2)

    # /fridge
    driver.find_element_by_link_text("Go to Fridge").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="myInput"]').send_keys("potato, yellow")
    driver.find_element_by_xpath('//p[text()="Potato, Yellow"]/../button').click()
    driver.find_element_by_xpath('//*[@id="myInput"]').clear()
    driver.find_element_by_xpath('//*[@id="myInput"]').send_keys("allspice")
    driver.find_element_by_xpath('//p[text()="Allspice"]/../button').click()
    driver.find_element_by_xpath('//*[@id="recipeSearch"]').click()
    time.sleep(1)

    # /home
    driver.find_element_by_link_text("Go to Home").click()
    time.sleep(2)
    driver.find_element_by_xpath('//p[@class="product_id" and text()="74"]/../button').click()
    driver.find_element_by_xpath('//p[@class="product_id" and text()="110"]/../button').click()
    driver.find_element_by_xpath('//*[@id="recipeSearch"]').click()
    time.sleep(2)

    # /recipe
    driver.find_element_by_xpath('//a[@href="recipe?id=3"]').click()
    time.sleep(2)

    driver.close()


if __name__ == "__main__":
    main()