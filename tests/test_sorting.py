from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def sort_products(driver, sort_option, expected_names):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify that login succeeded
    assert "inventory" in driver.current_url, (
    f"Login failed or inventory page did not open. "
    f"Current URL: {driver.current_url}"
    )

    # Find the sorting dropdown
    dropdown = Select(
        driver.find_element(
          By.CLASS_NAME, "product_sort_container"
    )
    )
    dropdown.select_by_value(sort_option)

    # Verify product order
    product_names = [
        item.text
        for item in driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )
    ]
    product_prices = [
        float(item.text.replace("$", ""))
        for item in driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    ]
    if sort_option in ("az", "za"):
       assert product_names == expected_names

    elif sort_option == "lohi":
       assert product_prices == sorted(product_prices)

    elif sort_option == "hilo":
       assert product_prices == sorted(
         product_prices, reverse=True
        )


def test_sort_A_to_Z(driver):
    expected = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)",
    ]

    sort_products(driver, "az", expected)


def test_sort_Z_to_A(driver):
    expected = [
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Onesie",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Bike Light",
        "Sauce Labs Backpack",
    ]

    sort_products(driver, "za", expected)

def test_sort_min_to_max(driver):
    expected = [
        "Sauce Labs Onesie",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Backpack",
        "Sauce Labs Fleece Jacket",
    ]

    sort_products(driver, "lohi", expected)

def test_sort_max_to_min(driver):
    expected = [
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Backpack",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Bike Light",
        "Sauce Labs Onesie",
    ]

    sort_products(driver, "hilo", expected)