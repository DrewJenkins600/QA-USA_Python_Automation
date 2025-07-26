import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Addresses
    from_field_locater = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Tarrif and call button
    supportive_plan_card = (By.XPATH, '//div[contains(text(), "supportive")}')
    supportive_plan_card_parent = (By.XPATH, '//div[contains(text(), "supportive")]//..')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title]')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Add"]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@style="margin-bottom: 30px;"]')
    blanket_and_handkerchiefs_selector = (By.XPATH, "//div[contains(text(), 'Blanket')]")
    message_for_driver = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label')
    order_requirements = (By.XPATH, "//div[contains(text(), 'Order Requirements')]")

    # Phone number

    def __init__(self, driver):
        self.ice_cream_count = None
        self.tab_locator = None
        self.card_number = None
        self.add_card_locator = None
        self.comment_field_locator = None
        self.add_blanket_and_handkerchiefs_locator = None
        self.click_payment_method_locator = None
        self.call_taxi_button_locator = None
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field_locater).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field_locater).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        time.sleep(5)
        self.click_taxi_button()

    def select_supportive_plan(self):
        self.driver.find_element(*self.supportive_plan_card_parent).click()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.supportive_plan_card_parent).get_property('value')

    def set_phone(self, phone_number):
        return self.driver.find_element(*self.supportive_plan_card_parent).send_keys(phone_number)

    def get_phone(self):
        return self.driver.find_element(*self.supportive_plan_card_parent).get_property('value')

    def click_call_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button_locator).click()

    def click_payment_method(self):
        self.driver.find_element(*self.click_payment_method_locator).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card_locator).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.card_number).send_keys(card_number)

    def enter_card_code(self, card_code):
        self.driver.find_element(*self.card_number).send_keys(card_code)

    def click_tab(self):
        self.driver.find_element(*self.tab_locator).click()

    def get_comment_field(self):
        return self.driver.find_element(*self.comment_field_locator).get_property('value')

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.message_for_driver).click()
        self.driver.find_element(*self.message_for_driver).send_keys(message)


    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver).get_property('value')

    def click_add_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.add_blanket_and_handkerchiefs_locator).click()

    def is_blanket_and_handkerchiefs_selected(self):
        pass

    def order_ice_cream(self, param):
        pass

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_count).get_property('value')

    def click_order_requirement(self):
        self.driver.find_element(*self.order_requirements).click()

