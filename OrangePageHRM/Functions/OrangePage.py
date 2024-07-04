from Functions.OrangeFunctions import funcionesGlobales

class paginaLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        driver = self.driver
        gf = funcionesGlobales(driver)
        gf.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Capturar usuario y contraseña
        username = gf.captureUser("//p[normalize-space()='Username : Admin']")
        password = gf.capturePassword("//input[@id='txtPassword']")  # Asumiendo que la contraseña está en un campo de entrada

        # Mostrar los valores capturados (solo para verificar)
        print(f"El nombre de usuario es: {username}")
        print(f"La contraseña de usuario es: {password}")

        # Setear el nombre de usuario en el campo de entrada
        username_input = gf.globalInput("//input[@placeholder='Username']")
        if username_input:
            username_input.send_keys(username)

        # Realizar otras operaciones si es necesario
        gf.globalInput("//input[@id='txtUsername']")
