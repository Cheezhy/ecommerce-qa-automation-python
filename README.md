# Ecommerce QA Automation Project

![Test Status](https://github.com/Cheezhy/ecommerce-qa-automation-python/actions/workflows/python-tests.yml/badge.svg)

This is an end-to-end automation testing project built for [automationexercise.com](https://automationexercise.com), a mock e-commerce website used for QA practice and UI validation. The project simulates real-world QA testing using Selenium, Pytest, and GitHub Actions.

---

## 🚀 Tech Stack

- Python 3.12
- Selenium WebDriver
- Pytest
- Git + GitHub
- GitHub Actions (CI/CD)

---

## 📦 Project Structure

```
ecommerce_qa_automation/
│
├── tests/                  # All test cases
│   ├── test_smoke.py           # Home page load test
│   ├── test_login.py           # Valid login test
│   ├── test_invalid_login.py   # Invalid login error
│   ├── test_logout.py          # Logout after login
│   ├── test_add_to_cart.py     # Add product to cart
│   └── test_checkout.py        # Complete checkout flow
│
├── utils/                 # Helper functions and browser config
│   └── driver_factory.py
│
├── .github/workflows/     # GitHub Actions CI
│   └── python-tests.yml
│
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

---

## ✅ Test Scenarios Implemented

- ✔️ **Smoke Test** – Homepage title validation
- ✔️ **Valid Login** – Login with test credentials
- ✔️ **Invalid Login** – Error for wrong credentials
- ✔️ **Logout** – Logs out after login
- ✔️ **Add to Cart** – Adds item to cart
- ✔️ **Checkout** – Completes checkout with dummy payment

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/Cheezhy/ecommerce-qa-automation-python.git
cd ecommerce-qa-automation-python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run tests

```bash
pytest tests/
```

---

## 👤 Dummy Credentials Used

```text
Email: automationtestuser@example.com
Password: test123
```

---

## 🧪 Continuous Integration

This repo uses **GitHub Actions** to:
- Automatically install Chrome in CI
- Run all tests on each push
- Validate success using Pytest + Selenium

---

## 🙋 Author

Built by Cheezhy  
🔗 [github.com/Cheezhy](https://github.com/Cheezhy)

This was created for QA testing practice and professional portfolio development.