from locators import LocatorsPage


class TestConstructor:

    # Проверка перехода в раздел «Булки»
    def test_go_to_the_buns_section(self, driver):
        driver.find_element(*LocatorsPage.filling_constructor).click()
        driver.find_element(*LocatorsPage.bread_constructor).click()
        assert driver.find_element(*LocatorsPage.select_tab_constructor).text == driver.find_element(
            *LocatorsPage.header_bread_constructor).text
        driver.quit()


    # Проверка перехода в раздел «Соусы»
    def test_go_to_the_sauces_section(self, driver):
        driver.find_element(*LocatorsPage.filling_constructor).click()
        driver.find_element(*LocatorsPage.sauce_constructor).click()
        assert driver.find_element(*LocatorsPage.select_tab_constructor).text == driver.find_element(
            *LocatorsPage.header_sauce_constructor).text
        driver.quit()


    # Проверка перехода в раздел «Начинки»
    def test_go_to_the_filling_section(self, driver):
        driver.find_element(*LocatorsPage.sauce_constructor).click()
        driver.find_element(*LocatorsPage.filling_constructor).click()
        assert driver.find_element(*LocatorsPage.select_tab_constructor).text == driver.find_element(
            *LocatorsPage.header_filling_constructor).text
        driver.quit()

