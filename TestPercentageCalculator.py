import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from HtmlTestRunner import HTMLTestRunner

class TestPercentageCalculator(unittest.TestCase):
    def setUp(self):
        # Configuración: Se ejecuta antes de cada caso de prueba
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.calculator.net/")
        # Hacer clic en Math Calculators
        self.driver.find_element(By.XPATH, "//*[@id='homelistwrap']/div[3]/div[2]/a").click()
        # Hacer clic en Percent Calculator
        self.driver.find_element(By.XPATH, "//*[@id='content']/table[2]/tbody/tr/td/div[3]/a").click()
        # xpath de botones de interaccion
        self.xpath_btn_calculate = "//*[@id='content']/form[1]/table/tbody/tr[2]/td/input[2]"
        self.xpath_result = "//*[@id='content']/p[2]/font/b"

    def tearDown(self):
        # time.sleep(5)
        self.driver.close()

    def test_calculate_percentage_positive_numbers(self):
        # Caso de prueba: Calcular el porcentaje con números positivos
        self.driver.find_element(By.ID, "cpar1").send_keys("10")
        self.driver.find_element(By.ID, "cpar2").send_keys("50")
        self.driver.find_element(By.XPATH, self.xpath_btn_calculate).click()

        result = self.driver.find_element(By.XPATH, self.xpath_result).text
        self.assertEqual(result, "5") # 10% de 50 es 5
    
    def test_calculate_percentage_negative_numbers(self):
        # Caso de prueba: Calcular el porcentaje con números negativos
        self.driver.find_element(By.ID, "cpar1").send_keys("-20")
        self.driver.find_element(By.ID, "cpar2").send_keys("100")
        self.driver.find_element(By.XPATH, self.xpath_btn_calculate).click()

        result = self.driver.find_element(By.XPATH, self.xpath_result).text
        self.assertEqual(result, "-20")  # -20% de 100 es -20

    def test_calculate_percentage_decimal_numbers(self):
        # Caso de prueba: Calcular el porcentaje con números decimales
        self.driver.find_element(By.ID, "cpar1").send_keys("7.5")
        self.driver.find_element(By.ID, "cpar2").send_keys("80.5")
        self.driver.find_element(By.XPATH, self.xpath_btn_calculate).click()

        result = self.driver.find_element(By.XPATH, self.xpath_result).text
        self.assertEqual(result, "6.0375")  # 7.5% de 80.5 es 6.0375
    
    def test_calculate_percentage_with_minimum_value(self):
        # Caso de prueba: Calcular el porcentaje con el valor mínimo permitido
        self.driver.find_element(By.ID, "cpar1").send_keys("-100000000000000")
        self.driver.find_element(By.ID, "cpar2").send_keys("50")
        self.driver.find_element(By.XPATH, self.xpath_btn_calculate).click()

        result = self.driver.find_element(By.XPATH, self.xpath_result).text
        self.assertEqual(result, "-50000000000000")  # -999999999% de 50 es -1999999998

    def test_calculate_percentage_with_maximum_value(self):
        # Caso de prueba: Calcular el porcentaje con el valor máximo permitido
        self.driver.find_element(By.ID, "cpar1").send_keys("100000000000000")
        self.driver.find_element(By.ID, "cpar2").send_keys("50")
        self.driver.find_element(By.XPATH, self.xpath_btn_calculate).click()

        result = self.driver.find_element(By.XPATH, self.xpath_result).text
        self.assertEqual(result, "50000000000000")  # 999999999% de 999999999 es 999999999
    
    def test_calculate_percentage_with_zero(self):
        # Caso de prueba: Calcular el porcentaje con un valor igual a 0
        self.driver.find_element(By.ID, "cpar1").send_keys("0")
        self.driver.find_element(By.ID, "cpar2").send_keys("100")
        self.driver.find_element(By.XPATH, self.xpath_btn_calculate).click()

        result = self.driver.find_element(By.XPATH, self.xpath_result).text
        self.assertEqual(result, "0")  # 0% de 100 es 0

    def test_calculate_percentage_with_both_zeros(self):
        # Caso de prueba: Calcular el porcentaje con ambos valores igual a 0
        self.driver.find_element(By.ID, "cpar1").send_keys("0")
        self.driver.find_element(By.ID, "cpar2").send_keys("0")
        self.driver.find_element(By.XPATH, self.xpath_btn_calculate).click()

        result = self.driver.find_element(By.XPATH, self.xpath_result).text
        self.assertEqual(result, "0")  # 0% de 0 es 0


if __name__ == "__main__":
    report_name = 'reporte_de_pruebas.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPercentageCalculator)

    # Configura HTMLTestRunner con el nombre personalizado
    with open(report_name, 'w') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, report_name="reporte_de_pruebas")
        result = runner.run(suite)
    print(result)
