import os
from selenium import webdriver
from loguru import logger
import datetime
import pathlib
import pytest


# Добавляем настройки для вебдрайвера
@pytest.fixture
def browser(config_browser='chrome'):
    directory = os.path.abspath(os.curdir)

    global driver

    # Initialize WebDriver
    if config_browser == 'chrome':
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": directory, }
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--allow-insecure-localhost')
        options.add_argument('--window-size=1920,1080')
        options.binary_location = '/opt/google/chrome'
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(15)
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Передача объекта драйвера в тестовую сессию
    yield driver

    # Завершение сессии после выполнения теста
    driver.quit()


# Добавляем дополнительное логирование
log_file_name = ''
@pytest.fixture(autouse=True)
def add_logger():

    # Настройки для логирования
    Rep = pathlib.Path.cwd()
    Repoz = str(Rep)
    logs_catalog = Repoz + '/logs/'
    prefix_name = 'log_'
    today = str(datetime.datetime.today())
    logger.info('# устанавливаем имя файла для логирования')
    global log_file_name
    log_file_name = logs_catalog + prefix_name + today + '.txt'
    logger.remove()
    logger.add(log_file_name, level='INFO', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    logger.info('# Записываем дату и время начала теста: ' + str(datetime.datetime.today().strftime('%d.%m.%Y')))

    logger_instance = logger
    yield logger_instance

    # Дополнительные действия для завершения теста
    pass
