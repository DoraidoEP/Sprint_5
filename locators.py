from selenium.webdriver.common.by import By


class LocatorsPage:

    account_butt = (By.XPATH, "//a[@href = '/account']")  # кнопка "Личный кабинет"

    registerate = (By.XPATH, "//a[@href = '/register']")  # кнопка "Зарегистрироваться"

    button_register = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться" на странице регистрации

    name = (By.XPATH, './/input[@name="name"]')  # поле "Имя"

    input_email = (By.XPATH, ".//*[text()='Email']/following-sibling::input")  # поле "Email"

    input_password = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")  # поле "Пароль"

    button_log_in_account = (By.XPATH, './/button[contains(text(),"Войти в аккаунт")]')  # кнопка "Войти в аккаунт" на главной странице

    log_in_text = (By.XPATH, ".// h2[text() = 'Вход']")  # заголовок страницы входа в личный кабинет

    button_exit = (By.XPATH, "//button[contains(text(),'Выход')]")  # кнопка "Выход" в личном кабинете

    error_field_password = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')  # "Некорректный пароль" на странице Входа

    construction_butt = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # кнопка "Конструктор" в шапке

    input_enter_pass = (By.XPATH, './/input[@name="Пароль"]')  # инпат поля "Пароль"

    button_log_in = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти" на странице входа в аккаунт

    butt_log_in_pass = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль"

    butt_in_enter = (By.XPATH, "//a[@href = '/login']")  # кнопка "Войти" на странице восстановления пароля

    logo_page = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')  # лого сайта "Stellar burgers"

    bread_constructor = (By.XPATH, "//span[text()='Булки']")  # кнопка "Булки" на главной странице

    sauce_constructor = (By.XPATH, "//span[text()='Соусы']")  # кнопка "Сойсы" на главней странцие

    filling_constructor = (By.XPATH, "//span[text()='Начинки']")  # кнопка "Начинки" на главной странице

    header_bread_constructor = (By.XPATH, "//h2[text()='Булки']")  # текст кнопки "Булки"

    header_sauce_constructor = (By.XPATH, "//h2[text()='Соусы']")  # текст кнопки "Соусы"

    header_filling_constructor = (By.XPATH, "//h2[text()='Начинки']")  # текст кнопки "Начинки"

    select_tab_constructor = (By.XPATH, ".//div[contains(@class, 'current')]/span")  # выбранная опция в конструкторе

