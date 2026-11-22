"""
Page Object for the Sauce Demo inventory (post-login) page.
"""
from playwright.sync_api import Page


class InventoryPage:
    """Represents the inventory page shown after a successful login."""

    INVENTORY_LIST = "[data-test='inventory-container']"
    INVENTORY_ITEM = "[data-test='inventory-item']"
    PAGE_TITLE = ".title"

    def __init__(self, page: Page):
        self.page = page

    def is_loaded(self) -> bool:
        """Return True if the inventory page is fully loaded."""
        inventory_list = self.page.locator(self.INVENTORY_LIST)
        inventory_list.wait_for(state="visible")
        return inventory_list.is_visible()

    def item_count(self) -> int:
        """Return the number of products on the page."""
        self.page.locator(self.INVENTORY_LIST).wait_for(state="visible")
        return self.page.locator(self.INVENTORY_ITEM).count()

    def title_text(self) -> str:
        """Return the page-title text (should be 'Products')."""
        return self.page.inner_text(self.PAGE_TITLE)
