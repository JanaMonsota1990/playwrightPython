from framework.browser import playwright_instance


def test_playwright_framework_bootstraps():
    manager = playwright_instance()
    assert hasattr(manager, "__enter__")
    assert hasattr(manager, "__exit__")
