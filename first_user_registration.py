import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class First_user_registration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_first_user_registration(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        self.assertIn("My Store", driver.title)

        driver.find_element(By.LINK_TEXT, "Sign in").click()
        print("Navigating to Next Page")
        time.sleep(10)

        driver.find_element(
            By.XPATH, '//*[@id="email_create"]').send_keys("ananya.ritu2@bracu.ac.bd")
        driver.find_element(By.ID, "SubmitCreate").click()
        time.sleep(10)

        driver.find_element(
            By.XPATH, '//*[@id="customer_firstname"]').send_keys("anaya")

        driver.find_element(
            By.XPATH, '//*[@id="customer_lastname"]').send_keys("ritu")

        driver.find_element(
            By.XPATH, '//*[@id="passwd"]').send_keys("ananya@12345")

        driver.find_element(
            By.XPATH, '//*[@id="address1"]').send_keys("Mohakhali")

        driver.find_element(
            By.XPATH, '//*[@id="city"]').send_keys("Kansas City")

        state_select = Select(driver.find_element_by_id('id_state'))

        # select by visible text
        state_select.select_by_visible_text('Kansas')

        driver.find_element(
            By.XPATH, '//*[@id="postcode"]').send_keys("64030")

        driver.find_element(
            By.XPATH, '//*[@id="phone_mobile"]').send_keys("01859586213")

        time.sleep(10)

        driver.find_element(
            By.XPATH, '//*[@id="submitAccount"]').click()

        time.sleep(10)

        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
