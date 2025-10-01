This repository contains a comprehensive automation testing framework developed during a QA course. It includes tests for UI, API, and database layers, using Pytest, Selenium, and the Page Object Model architecture.

Technologies Used:

    Python 3.12
    Pytest — test framework
    Selenium — UI automation
    Requests — API testing
    SQLite / PostgreSQL — database layer
    Page Object Model — UI architecture
    webdriver-manager — driver handling


Project Structure:

    config/: Centralized configuration management.

    modules/: Main source code for automation logic:
        api/clients/: API client implementations.
        common/database.py: Database access and utility functions.
        ui/page_objects/: Page Object Model classes for UI automation.

    tests/: Test suites organized by domain:
        api/: API tests.
        database/: Database tests.
        ui/: UI tests.
        ui1/: Tests for UI by Page Object Model

    become_qa_auto.db: SQLite database used for database testing.

    conftest.py: Shared pytest fixtures and hooks.
    
    pytest.ini: Pytest configuration and custom markers for test categorization.


Developer Workflows

    Run all tests:

        pytest

    Run a specific test suite:

        pytest -m {mark}

    All available marks can be found in pytest.ini.

    Debugging: Use print() or logging in test files and modules. Pytest captures output unless run with -s.

    Database: The SQLite database is stored in become_qa_auto.db. Use helpers in modules/common/database.py.


Patterns & Conventions

    Page Object Model: All UI automation uses page objects in modules/ui/page_objects/. Each class encapsulates selectors and actions for a specific page.
    API Clients: API interactions are implemented in modules/api/clients/. Each client is a separate file/class.
    Fixtures: Shared pytest fixtures are defined in conftest.py and reused across test suites.
    Test Naming: Test files and functions use descriptive names (e.g., test_github_api.py, test_database.py).
