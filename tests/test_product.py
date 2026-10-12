from selenium.webdriver.common.by import By

def test_click_on_product_shows_product_card(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Click on the backpack product
    driver.find_element(
        By.ID, "item_4_title_link"
    ).click()
    # Verify that the product card is displayed
    product_card = driver.find_element(
        By.CLASS_NAME, "inventory_details"
    )
    assert product_card.is_displayed()
    # Verify product image is displayed
    product_image = driver.find_element(
        By.CLASS_NAME, "inventory_details_img"
    )
    assert product_image.is_displayed()
    assert product_image.get_attribute("src")
    assert product_image.get_property("complete")
    assert product_image.get_property("naturalWidth") > 0
    
def test_back_to_products_button_navigates_back(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Click on the backpack product
    driver.find_element(
        By.ID, "item_4_title_link"
    ).click()

    # Click on the "Back to products" button
    driver.find_element(
        By.ID, "back-to-products"
    ).click()

    # Verify that the user is navigated back to the inventory page
    assert "inventory" in driver.current_url

