from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
def test_checkout(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add the backpack to the cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    # Verify the cart badge
    cart_badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert cart_badge.text == "1"

    # Click on the cart icon
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    #Click on checkout button
    driver.find_element(By.ID, "checkout").click()
    #check if the form opens
    assert driver.find_element(By.ID, "first-name").is_displayed()
    assert driver.find_element(By.ID, "last-name").is_displayed()
    assert driver.find_element(By.ID, "postal-code").is_displayed()

    #check if the continue button is displayed
    assert driver.find_element(By.ID, "continue").is_displayed()
    #check if correct info provided, the user can continue to the next page
    driver.find_element(By.ID, "first-name").send_keys("John")  
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    #check if the user is navigated to the overview page
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("checkout-step-two"))
    driver.find_element(By.ID, "finish").click()
    #check if the user is navigated to the complete page
    wait.until(EC.url_contains("checkout-complete"))
    #check if the order complete message is displayed
    assert driver.find_element(By.CLASS_NAME, "complete-header").is_displayed()

def test_cancel_within_checkout(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add the backpack to the cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    # Verify the cart badge
    cart_badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert cart_badge.text == "1"

    # Click on the cart icon
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    #Click on checkout button
    driver.find_element(By.ID, "checkout").click()
    #check if the form opens
    assert driver.find_element(By.ID, "first-name").is_displayed()
    assert driver.find_element(By.ID, "last-name").is_displayed()
    assert driver.find_element(By.ID, "postal-code").is_displayed()

    #check if the continue button is displayed
    assert driver.find_element(By.ID, "continue").is_displayed()
    #check if correct info provided, the user can continue to the next page
    driver.find_element(By.ID, "first-name").send_keys("John")  
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    #check if the user is navigated to the overview page
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("checkout-step-two"))
    driver.find_element(By.ID, "cancel").click()
    #check if the user is navigated to the inventory page
    assert "inventory" in driver.current_url

def test_cancel_buttons(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    if cart_badge := driver.find_elements(By.CLASS_NAME, "shopping_cart_badge"):
        if int(cart_badge[0].text) > 0:
            # Click on the cart icon
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            # Click on checkout button
            driver.find_element(By.ID, "checkout").click()
            # Click on cancel button
            driver.find_element(By.ID, "cancel").click()
            # Verify that the user is navigated back to the inventory page
            assert "inventory" in driver.current_url
        else:
            # Add the backpack to the cart
            driver.find_element(
                By.ID, "add-to-cart-sauce-labs-backpack"
            ).click()
            # Click on the cart icon
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            # Click on checkout button
            driver.find_element(By.ID, "checkout_button").click()
            # Click on cancel button
            driver.find_element(By.ID, "cancel").click()
            # Verify that the user is navigated back to the inventory page
            assert "inventory" in driver.current_url

@pytest.mark.parametrize("first_name,last_name,postal_code,should_continue", [
    ("John", "Doe", "12345", True),
    ("", "Doe", "12345", False),
    ("John", "", "12345", False),
    ("John", "Doe", "", False),
    ("", "", "", False),
])        
def test_checkout_form_validation(driver, first_name, last_name, postal_code, should_continue):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    if cart_badge := driver.find_elements(By.CLASS_NAME, "shopping_cart_badge"):
            if int(cart_badge[0].text) > 0:
                # Click on the cart icon
                driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
                # Click on checkout button
                driver.find_element(By.ID, "checkout_button").click()
                # Click on cancel button
                driver.find_element(By.ID, "cancel").click()
                # Verify that the user is navigated back to the inventory page
                assert "inventory" in driver.current_url
            else:
                # Add the backpack to the cart
                driver.find_element(
                    By.ID, "add-to-cart-sauce-labs-backpack"
                ).click()
                # Click on the cart icon
                driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
                # Click on checkout button
                driver.find_element(By.ID, "checkout_button").click()
                #check if the form opens
                if should_continue:
                    driver.find_element(By.ID, "first-name").send_keys(first_name)  
                    driver.find_element(By.ID, "last-name").send_keys(last_name)
                    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
                    driver.find_element(By.ID, "continue").click()
                    #check if the user is navigated to the overview page
                    assert "checkout-step-two" in driver.current_url
                else:
                        error = driver.find_element(
                            By.CSS_SELECTOR, '[data-test="error"]'
                        )
                        assert error.is_displayed()