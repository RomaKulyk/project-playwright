import re
from playwright.sync_api import Page, expect


def test_categories_links(page: Page):
    """
    Test that the main category links are present and lead to the correct pages.
    """
    page.goto("https://www.leyven.com.ua/")

    categories_links = [
                        "Годування",
                        "Здоров'я",
                        "Іграшки",
                        "Амуніція"
    ]

    page_titles = [
        "Годування домашніх тварин і птахів | Лейвен",
        "Ветеринарні засоби та препарати | Лейвен",
        "Товари для комфорту домашніх тварин | Лейвен",
        "Товари для прогулянок і подорожей з тваринами | Лейвен"
    ]


    for i in range(len(categories_links)):
        # Click the link.
        page.get_by_role("link", name=categories_links[i]).click()
        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile(page_titles[i]))
        page.wait_for_timeout(2000)  # Wait for 2000 ms (2 seconds)

        # Click the "Лейвен логотип" main logo.
        page.get_by_alt_text('Лейвен логотип').nth(1).click()
        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Інтернет-зоомагазин Лейвен ✅"))