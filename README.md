
# Ecommerce QA Automation Project

This is an end-to-end automation testing project built for [automationexercise.com](https://automationexercise.com), a mock e-commerce website used for QA practice and UI validation. This project was created as part of my hands-on experience with Selenium, Pytest, and GitHub.

The goal is to simulate real-world QA testing tasks using Python-based tools and frameworks.

---

## 🚀 Tech Stack

- Python 3.10+
- Selenium WebDriver
- Pytest
- Allure Reports (optional)
- Git + GitHub

---

## 📦 Project Structure

```
ecommerce_qa_automation/
├── tests/                # Pytest test cases
│   ├── test_smoke.py     # Basic homepage load test
│   └── test_login.py     # Login with valid credentials
├── pages/                # (Page Objects – to be added later)
├── utils/                # Driver factory & helper files
├── conftest.py           # Pytest fixtures for browser setup
├── requirements.txt      # Project dependencies
└── README.md             # Project overview and usage
```

---

## ✅ Test Scenarios Implemented

- **Smoke Test** – Opens homepage and checks page title  
- **Login Test** – Enters test credentials, logs in, and validates successful login message

---

## 🛠️ Installation

1. **Clone this repo:**

```bash
git clone https://github.com/Cheezhy/ecommerce-qa-automation-python.git
cd ecommerce-qa-automation-python
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run tests:**

```bash
pytest tests/test_smoke.py
pytest tests/test_login.py
```

---

## 🔐 Credentials Used

This is a public test site. The test uses the following dummy credentials:

- **Email:** `automationtestuser@example.com`  
- **Password:** `test123`

---

## 🎯 Future Improvements

- Add Page Object Model (POM) structure  
- Integrate with GitHub Actions for CI  
- Expand test coverage: Signup, Add to Cart, Checkout  
- Include visual test reporting (Allure)

---

## 👋 Author

Built by **Cheezhy**  
GitHub: [Cheezhy](https://github.com/Cheezhy)

This project is part of my QA automation learning journey — feedback is welcome!
