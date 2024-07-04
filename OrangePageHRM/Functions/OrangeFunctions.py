from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class funcionesGlobales:
    def __init__(self, driver):
        self.driver = driver

    def navegar(self, url):
        try:
            self.driver.get(url)
            print("Ingreso a URL exitoso")
        except TimeoutException as ex:
            print(ex.msg)
            return False

    def captureUser(self, selector):
        try:
            username_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            return username_element.text.split(":")[-1].strip()
        except TimeoutException as ex:
            print(f"Error al capturar usuario: {ex}")
            return None

    def capturePassword(self, selector):
        try:
            password_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            return password_input.get_attribute("value")
        except TimeoutException as ex:
            print(f"Error al capturar contraseña: {ex}")
            return None

    def globalInput(self, selector):
        try:
            input_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            if input_element.is_enabled():
                print("Este elemento está presente")
                return input_element  # Devuelve el elemento WebElement
            else:
                print("Este elemento NO está presente")
                return None
        except TimeoutException as ex:
            print(f"Timeout al esperar elemento: {ex}")
            return None