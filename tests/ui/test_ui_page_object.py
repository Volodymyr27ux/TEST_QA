from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui1
def test_check_incorrect_username_page_object():
    # creating object to manage the browser
    sign_in_page = SignInPage()

    # open the page https://github.com/login 
    sign_in_page.go_to()

    # attempting to log in to GitHub system
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Checking that the page title is as expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # closing the browser
    sign_in_page.close()