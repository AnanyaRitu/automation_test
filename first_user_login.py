import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class First_user_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_first_user_login(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        self.assertIn("My Store", driver.title)

        driver.find_element(By.LINK_TEXT, "Sign in").click()
        print("Navigating to Next Page")
        time.sleep(5)

        #login
        driver.find_element(
            By.XPATH, '//*[@id="email"]').send_keys("ananya.ritu@bracu.ac.bd")
        driver.find_element(
            By.XPATH, '//*[@id="passwd"]').send_keys("ananya@12345")
        driver.find_element(By.ID, "SubmitLogin").click()
        time.sleep(5)

        #adding casual dress to cart
        driver.find_element(
            By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, '//*[@id="categories_block_left"]/div/ul/li[1]/a').click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]').click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/span').click()
        time.sleep(5)


        #buying blue tshirt
        driver.find_element(
            By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a').click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, '//*[@id="layered_id_attribute_group_14"]').click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span').click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()
       

        #paying for blue shirt
        time.sleep(3)
        #order summary
        driver.find_element(
            By.XPATH, '//*[@id="center_column"]/p[2]/a[1]').click()
        time.sleep(3)
        #confirm address
        driver.find_element(
            By.XPATH, '//*[@id="center_column"]/form/p/button').click()
        time.sleep(3)
        #aggree to terms and conditions
        driver.find_element(
            By.XPATH, '//*[@id="cgv"]').click()

        time.sleep(3)
        #shipping
        driver.find_element(
            By.XPATH, '//*[@id="form"]/p/button').click()
        time.sleep(3)
        #pay by check
        driver.find_element(
            By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a').click()
        time.sleep(3)
        #confirm order
        driver.find_element(
            By.XPATH, '//*[@id="cart_navigation"]/button').click()
        time.sleep(3)


        #sign out
        driver.find_element(
            By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
