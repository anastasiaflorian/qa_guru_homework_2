from selene.support.shared import browser
from selene import be, have

def test_search_1():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser ...'))


def test_search_2():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('serdtfyguhijnokmljnkml').press_enter()
    browser.element('[id="search"]').should(have.text('Результатов: примерно 0'))