from selene.support.conditions import be, have
from selene.support.shared import browser

from QA_GURU_hw_8.modules.controls import select_dropdown

'''Определяем функции'''


# Функция открытия страницы (масштаб задан для возможности клика на кнопку 'submit')
def open_page(page):
    browser.open(page)
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.4)"')


# Функция ввода данных
def type_info(option, value):
    browser.element(option).should(be.blank).type(value)


# Функция выбора изучаемого предмета
def select_subject(element, subject):
    browser.element(element).send_keys(subject).press_enter()


# Функция выбора штата
def select_state(value):
    select_dropdown('#state', text=value)


# Функция выбора города
def select_city(value):
    select_dropdown('#city', text=value)


# Функция проверка информации
def check_info(element, values):
    browser.all(element).should(have.texts(values))
