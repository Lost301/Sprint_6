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
