import pytest
from playwright.sync_api import Browser, BrowserContext, Page

@pytest.fixture(scope="function")
def set_up(page: Page):
    """
    This fixture runs before every test.
    It provides the 'page' object and handles cleanup automatically.
    """
    # Pre-test logic (e.g., resizing window)
    page.set_viewport_size({"width": 1280, "height": 720})
    
    yield page  # This is where the test happens
    
    # Post-test logic (e.g., taking a screenshot if you wanted)
    print("\nTest completed. Cleaning up...")