# SauceDemo UI Test Automation

Automated UI tests for [Swag Labs (SauceDemo)](https://www.saucedemo.com/) that we previously did manual tests for, written with **Python, Selenium WebDriver and pytest**.

The tests cover the main shopping flow: login, product browsing, sorting, cart and checkout.

## Tech stack

- Python 3
- Selenium WebDriver (Chrome)
- pytest (including parametrized tests)

## Project structure

```
SauceDemo_Automation_tester/
├── conftest.py            # `driver` fixture (starts and closes Chrome)
├── tests/
│   ├── test_login.py
│   ├── test_product.py
│   ├── test_sorting.py
│   ├── test_cart.py
│   └── test_checkout.py
└── README.md
```

## What is tested

| File | Area | Tests |
|---|---|---|
| `test_login.py` | Login | Successful login, invalid login, password field is masked, 6 parametrized credential combinations (valid, invalid user, wrong password, blank values) |
| `test_product.py` | Product details | Clicking a product opens its detail card and the image loads; "Back to products" returns to the inventory page |
| `test_sorting.py` | Sorting | Name A to Z, Z to A, price low to high, price high to low |
| `test_cart.py` | Cart | Add a product (badge shows 1), remove a product, product description matches between the inventory and cart pages |
| `test_checkout.py` | Checkout | Full checkout to the order-complete page, cancel from the overview page, cancel buttons, checkout form validation (valid data and 4 missing-field cases) |


## Running the tests

Run everything:

```
python -m pytest tests -v
```

Run one file:

```
python -m pytest tests/test_checkout.py -v
```

Run one test:

```
python -m pytest tests/test_checkout.py::test_checkout -v -s
```

## Author

Anika Afsara Suzana ([@ssuzana44](https://github.com/ssuzana44))