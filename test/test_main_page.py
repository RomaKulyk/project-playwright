import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    """
    Test that the main page is loaded and has the correct title.
    """
    page.goto("https://www.leyven.com.ua/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Інтернет-зоомагазин Лейвен ✅"))