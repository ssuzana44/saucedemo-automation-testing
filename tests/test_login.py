import pytest
from selenium.webdriver.common.by import By


def test_successful_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    assert error.is_displayed()

def test_password_is_masked(driver):
    driver.get("https://www.saucedemo.com/")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    field_type = password_field.get_attribute("type")

    assert field_type == "password"

@pytest.mark.parametrize("username,password,should_login", [
    ("standard_user", "secret_sauce", True),
    ("invalid_user", "wrong_password", False),
    ("standard_user", "wrong_password", False),
    (" ", " ", False),
    (" ", "secret_sauce", False),
    ("standard_user", " ", False)
])
def test_login_with_multiple_credentials(
    driver, username, password, should_login
):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if should_login:
        assert "inventory" in driver.current_url
    else:
        error = driver.find_element(
            By.CSS_SELECTOR, '[data-test="error"]'
        )
        assert error.is_displayed()
