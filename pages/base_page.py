from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception:
            # Sticky page elements can cover controls in Firefox; the target is
            # already visible and ready, so trigger its native click event.
            self.driver.execute_script("arguments[0].click();", element)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def type_text(self, locator, value):
        field = self.find(locator)
        field.clear()
        field.send_keys(value)

    def dismiss_cookie_banner(self):
        buttons = self.driver.find_elements('xpath', "//button[contains(.,'Да все привыкли')]")
        for button in buttons:
            if button.is_displayed():
                self.driver.execute_script("arguments[0].click();", button)
                return

    def open_url(self, url):
        self.driver.get(url)

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def press_enter(self, locator):
        self.find(locator).send_keys('\ue007')

    def click_visible_text(self, text):
        locator = ('xpath', f"//*[normalize-space()={text!r}]")
        for element in self.driver.find_elements(*locator):
            if element.is_displayed():
                self.js_click(element)
                return
        self.wait.until(lambda driver: False)

    def open_link_in_new_tab(self, locator):
        element = self.find(locator)
        self.driver.execute_script("window.open(arguments[0].href, '_blank');", element)

    def current_url(self):
        return self.driver.current_url

    def current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self, old_handle):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        new_handle = next(handle for handle in self.driver.window_handles if handle != old_handle)
        self.driver.switch_to.window(new_handle)
