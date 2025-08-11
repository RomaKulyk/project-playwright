import re
from playwright.sync_api import Page, expect


def test_main_categories(page: Page):
    """
    Test that the main categories are loaded and lead to the correct pages.
    """
    page.goto("https://www.leyven.com.ua/")

    main_categories_links = ["🐕 Собакам",
                             "🐈 Котам",
                             "🍖 Корми",
                             "💊 Сімпаріка",
                             "🏭 Бренди",
                             "📒 Блог",
                             "🛏️ Лежаки",
                             "✨ Новинки"
    ]

    page_titles = [
        "Собаки | Лейвен",
        "Коти | Лейвен",
        "Сухий корм | Лейвен",
        "Сімпаріка | Інтернет-зоомагазин Лейвен",
        "Бренди | Лейвен - Інтернет-зоомагазин",
        "Лейвен Блог",
        "Будиночки, лежанки, м'які місця | Лейвен",
        "Новинки | Інтернет-зоомагазин Лейвен"
    ]

    for i in range(len(main_categories_links)):
        
        expect(page.get_by_text(main_categories_links[i])).to_be_visible()
        # Click the link.
        page.get_by_text(main_categories_links[i]).click()
        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile(page_titles[i]))
        page.wait_for_timeout(2000)
