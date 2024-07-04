Sure! Here's the updated README file without the code overview:

---

# OrangeHRM Automation Project

This project automates interactions with the OrangeHRM demo site using Python and Selenium WebDriver. It demonstrates how to perform tasks such as logging in, navigating modules, and extracting data.

## Technologies Used

- Python
- Selenium WebDriver

## Author

Javier Jimenez  
QA Analyst

## Project Structure

The project consists of the following files:

1. **`OrangeFunctions.py`**: Contains global functions for navigation, input handling, and validation.
2. **`OrangePage.py`**: Implements the login page interactions using the global functions.
3. **`test_orange_login.py`**: Contains the test cases for the login process.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/orangehrm-automation.git
    cd orangehrm-automation
    ```

2. **Install the required packages**:
    ```sh
    pip install selenium
    ```

3. **Download the appropriate WebDriver for your browser** and add it to your system's PATH.

## Usage

1. **Run the tests**:
    ```sh
    python test_orange_login.py
    ```

---
