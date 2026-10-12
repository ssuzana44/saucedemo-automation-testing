from selenium.webdriver.common.by import By

def test_add_product_to_cart(driver):
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

def test_remove_product_from_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add the backpack to the cart
    driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
    assert cart_badge.text == "1"
    # Remove the backpack from the cart
    driver.find_element(
        By.ID, "remove-sauce-labs-backpack"
    ).click()

    # Verify the cart is empty
    cart_badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert cart_badge.text == "0"


def test_product_description_matches_in_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Capture product description on inventory page
    product = driver.find_element(
        By.ID, "item_4_title_link"
    ).find_element(By.XPATH, "..")

    inventory_description = product.find_element(
        By.CLASS_NAME, "inventory_item_desc"
    ).text

    # Add the product to cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Capture description in cart
    cart_description = driver.find_element(
        By.CLASS_NAME, "inventory_item_desc"
    ).text

    # Compare both descriptions
    assert cart_description == inventory_description
