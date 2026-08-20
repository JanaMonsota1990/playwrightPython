from playwright.sync_api import sync_playwright


def playwright_instance():
    """Return a sync Playwright context manager for tests and framework code."""
    return sync_playwright()
