# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd, Contact(name="Azat", middle="R", last_name="Zakuanov", home_phone="3107552233"))
        self.submit(wd)
        self.logout(wd)

    def test_test_add_second_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd, Contact(name="Azot", middle="XXX", last_name="ZakaZaka", home_phone="XXX-777-77-XX"))
        self.submit(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def submit(self, wd):
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def create_new_contact(self, wd, contact):
        # add new contact
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_link_text("add new").click()
        # fill in the form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        # fill in middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle)
        # fill in last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)


    def login(self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("//form[@id='LoginForm']//label[.='Password:']").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
