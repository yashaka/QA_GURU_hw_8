import os
from selene.support.shared import browser

'''Определяем функции '''


# Функция загрузки файлов
def upload_file(element, file):
    browser.element(element).set_value(os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, file)))
