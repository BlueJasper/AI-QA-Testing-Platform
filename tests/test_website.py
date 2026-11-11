
from playwright.sync_api import Page, expect


def test_website(page: Page):
    page.goto("https://example.com")

    # Verify the page title
    expect(page).to_have_title("Example Domain")

    # Verify the main heading appears
    expect(
        page.get_by_role("heading", name="Example Domain")
    ).to_be_visible()
