# Комментарии по тесту и по коду в файле README.md

import sys
import pytest
from mrfix.mrfix import MrFixUI as MrUI
from conftest import browser, add_logger, log_file_name
from selenium.webdriver.common.by import By
import allure
import pathlib
import datetime



class Data:

    Rep = pathlib.Path.cwd()
    Repoz = str(Rep)
    screen_catalog = Repoz + '/screenshot/'
    prefix_screen_name = 'screen_'

    # Страница 1
    start_url = 'https://old.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/'
    price = '5000'
    start_data = '08.02.2024'
    stop_data = '08.02.2025'

    # Страница 2
    fio = 'Румпельштильцхен Сигизмунд Вольфрамович'
    birthday = '22112001'
    passport_number = '6307289754'
    passport_date = '13012024'
    address = 'д. Простоквашино, ул. Шарика Матроскина, д.1'
    phone_number = '9099073250'
    email = 'sigizmund@mail.ru'
    in_url_3_page = '--------securepayments.tinkoff.ru'

class Xpath:

    # Страница 1
    check_box2_xpath = '/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[1]/label[2]/span'
    price_xpath = '//*[@id="price"]'
    start_data_xpath = '//*[@id="dateStart"]'
    stop_data_xpath = '//*[@id="dateEnd"]'
    check_box3_xpath = '/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[1]/label[3]/span'
    continue_button_xpath = '//*[@type="submit"]'
    continue_span_xpath = '/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[1]/div[8]/button/span'

    # Строаница 2
    fio_xpath = '//*[@id="name"]'
    birthday_xpath = '//*[@id="dateBirth"]'
    passport_number_xpath = '//*[@id="id"]'
    passport_date_xpath = '//*[@id="idDate"]'
    address_xpath = '//*[@id="address"]'
    phone_number_xpath = '//*[@id="phone"]'
    email_xpath = '//*[@id="email"]'
    go_to_pay_button_xpath = '//*[text()="Перейти к оплате"]'

    # Страница 3
    tinkoff_kassa_xpath = '//*[@xmlns="http://www.w3.org/2000/svg"]'


class TestAbsolut:

    @allure.feature("Пример теста")
    @allure.story("Отправка информации в Allure")
    def test_example(self, browser, add_logger):
        with allure.step("Ищем элемент, который не существует"):
            try:

                # Страница 1
                browser.maximize_window()

                add_logger.info('Заходим на стартовую страницу:')
                browser.get(Data.start_url)

                add_logger.info('Ставим чек-бокс "Подтверждаю, что..."')
                rezult = MrUI.make_displayed_with_arrow_down_and_click(browser, Xpath.check_box2_xpath, 10)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                add_logger.info('Делаем поле с ценой полиса доступным для ввода:')
                element = browser.find_element(By.XPATH, Xpath.price_xpath)
                browser.execute_script("arguments[0].removeAttribute('disabled');", element)

                add_logger.info('Вводим цену полиса:')
                rezult = MrUI. make_displayed_with_arrow_down_and_send(browser, Xpath.price_xpath, Data.price, 5)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                add_logger.info('Делаем поле с начальной датой полиса доступным для ввода:')
                element = browser.find_element(By.XPATH, Xpath.start_data_xpath)
                browser.execute_script("arguments[0].removeAttribute('disabled');", element)

                add_logger.info('Вводим начальную дату полиса:')
                rezult = MrUI. send_text_to_input(browser, Xpath.start_data_xpath, Data.start_data)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                add_logger.info('Делаем поле с конечной датой полиса доступным для ввода:')
                element = browser.find_element(By.XPATH, Xpath.stop_data_xpath)
                browser.execute_script("arguments[0].removeAttribute('disabled');", element)

                add_logger.info('Вводим конечную дату полиса:')
                rezult = MrUI. send_text_to_input(browser, Xpath.stop_data_xpath, Data.stop_data)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                add_logger.info('Ставим чек-бокс "Подтверждаю, что..."')
                rezult = MrUI.make_displayed_with_arrow_down_and_click(browser, Xpath.check_box3_xpath, 10)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                add_logger.info('Делаем кнопку "Продолжить" доступной для ввода:')
                element = browser.find_element(By.XPATH, Xpath.continue_button_xpath)
                browser.execute_script("arguments[0].removeAttribute('disabled');", element)

                add_logger.info('Нажимаем надпись "Продолжить"')
                rezult = MrUI.make_displayed_with_arrow_down_and_click(browser, Xpath.continue_span_xpath, 10)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                # Страница 2
                add_logger.info('Вводим ФИО:')
                rezult = MrUI. make_displayed_with_arrow_up_and_send(browser, Xpath.fio_xpath, Data.fio, 5)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                add_logger.info('Вводим дату рождения:')
                rezult = MrUI.click_element_by_xpath(browser, Xpath.birthday_xpath)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")
                for c in Data.birthday:
                    MrUI.press_char_key(browser, c, 1)
                MrUI.press_enter_key(browser, 1)

                add_logger.info('Вводим серию и номер паспорта:')
                rezult = MrUI.click_element_by_xpath(browser, Xpath.passport_number_xpath)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")
                for c in Data.passport_number:
                    MrUI.press_char_key(browser, c, 1)

                add_logger.info('Вводим дату выдачи паспорта:')
                rezult = MrUI.click_element_by_xpath(browser, Xpath.passport_date_xpath)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")
                for c in Data.passport_date:
                    MrUI.press_char_key(browser, c, 1)

                add_logger.info('Вводим адрес регистрации:')
                rezult = MrUI. send_text_to_input(browser, Xpath.address_xpath, Data.address)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                add_logger.info('Вводим номер телефона:')
                rezult = MrUI.make_displayed_with_arrow_down_and_click(browser, Xpath.phone_number_xpath, 5)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")
                for c in Data.phone_number:
                    MrUI.press_char_key(browser, c, 1)

                add_logger.info('Вводим email:')
                rezult = MrUI. send_text_to_input(browser, Xpath.email_xpath, Data.email)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")
                MrUI.press_tab_key(browser, 1)

                add_logger.info('Нажимаем кнопку "Перейти к оплате":')
                rezult = MrUI.make_displayed_with_arrow_down_and_click(browser, Xpath.go_to_pay_button_xpath, 5)
                add_logger.info(rezult)
                if not rezult:
                    raise Exception("Произошла ошибка")

                # time.sleep(10)
                add_logger.info('Кликаем картинку на странице, чтобы использовать неявное ожидание:')
                rezult = MrUI.click_element_by_xpath(browser, Xpath.tinkoff_kassa_xpath)

                add_logger.info('Проверяем адрес страницы, на которую перешли:')
                current_url = browser.current_url
                if Data.in_url_3_page in current_url:
                    add_logger.info("Перешли на страницу платежа. Тест ОК.")
                else:
                    add_logger.info("НЕ ПЕРЕШЛИ НА СТРАНИЦУ ПЛАТЕЖА. ОШИБКА!")
                    raise Exception("Произошла ошибка")

                # Если тест прошел успешно, отправляем об этом текстовое сообщение в Allure
                allure.attach("Test success", name="Success", attachment_type=allure.attachment_type.TEXT)

            except Exception as e:
                # Если происходит ошибка, делаем и сохраняем скриншот экрана
                today = str(datetime.datetime.today())
                screenshot_file = Data.screen_catalog + Data.prefix_screen_name + today + '.png'
                add_logger.info(f'Сделали скриншот: {screenshot_file}')
                browser.save_screenshot(screenshot_file)

                # отправляем текстовое сообщение в Allure
                allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)

                # Отправляем текстовый лог-файл в Allure
                allure.attach.file(log_file_name, name="Лог теста",
                                   attachment_type=allure.attachment_type.TEXT)

                # Отправляем скриншот в Allure
                allure.attach(screenshot_file, name="Screenshot_with_error",
                              attachment_type=allure.attachment_type.PNG)

                # Помечаем тест как проваленный
                pytest.fail("Тест завершился с ошибкой")

