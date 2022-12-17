from QA_GURU_hw_8.modules.page import *
from QA_GURU_hw_8.modules.controls import *
from QA_GURU_hw_8.modules.utils import *


def test_practice_form(browser_open):
    # Открываем страницу
    open_page('/automation-practice-form')
    # Заполняем данные
    type_info('#firstName', 'Andrew')
    type_info('#lastName', 'Chizh')
    type_info('#userEmail', 'andrechizh8@yandex.ru')
    select_control('[for="gender-radio-1"]')
    type_info('#userNumber', '9183346139')
    select_control('#dateOfBirthInput')
    select_control('.react-datepicker__month-select')
    select_control('[value="11"]')
    select_control('[value="1992"]')
    select_control('.react-datepicker__day--008')
    select_subject('#subjectsInput', 'Physic')
    select_control('[for="hobbies-checkbox-2"]')
    upload_file('#uploadPicture', 'img/pepe.jpg')
    type_info('#currentAddress', 'Krasnodar,Shirokaia 53')
    select_state('Haryana')
    select_city('Panipat')
    select_control('#submit')
    # Проверям данные
    check_info('.table-responsive td:nth-child(2)', (
        'Andrew Chizh',
        'andrechizh8@yandex.ru',
        'Male',
        '9183346139',
        '08 December,1992',
        'Physics',
        'Reading',
        'pepe.jpg',
        'Krasnodar,Shirokaia 53',
        'Haryana Panipat'))
