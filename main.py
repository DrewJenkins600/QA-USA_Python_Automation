import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("connected to the Urban Routes server")
        else:
            print("cannot connect to the Urban Routes server. Check the server is on and still running.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO


    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        assert routes_page.get_current_selected_plan() == 'supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        phone_number = data.PHONE_NUMBER
        routes_page.set_phone(phone_number)
        assert routes_page.get_phone() == phone_number

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        phone_number = data.PHONE_NUMBER
        routes_page.set_phone(phone_number)
        routes_page.click_add_card()
        routes_page.enter_card_number(data.CARD_NUMBER)
        routes_page.enter_card_code(data.CARD_CODE)
        routes_page.select_supportive_plan()
        routes_page.click_tab()
        routes_page.click_payment_method()
        assert routes_page.click_payment_method() == "card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.click_add_blanket_and_handkerchiefs()
        routes_page.click_order_requirement()
        assert routes_page.is_blanket_and_handkerchiefs_seleected()

    def test_order_2_ice_creams(self):
        for i in range(2):
            self.driver.get(data.URBAN_ROUTES_URL)
            routes_page = UrbanRoutesPage(self.driver)
            routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
            routes_page.select_supportive_plan()
            routes_page.order_ice_cream(2)  # Add the quantity here
            ice_cream_count = routes_page.get_ice_cream_count()
            assert ice_cream_count == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()





