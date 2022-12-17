from selene.support.shared import browser
from selene import be, have

'''Определяем функции'''


# Функция нажатия на выбранный элемент
def select_control(element):
    browser.element(element).click()


# Функция выбора элемента из dropbox'а
def select_dropdown(element, text):
    browser.element(element).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(text)
    ).click()
