**Overview**

For this project, I have decided to use Python with Selenium and Pytest. To run the code, you must have a clean Python installation, preferably using Python 3.11.5 (**does not work with Python 3.12**). If you are cloning the repository from Git, then follow step 1 onwards, however if you are downloading the project from the uploaded zip file, then you can move onto step 2. Here are the steps to set up and run the code:

1. **Clone the Repository:**

   Clone the repository to your local machine:
    ```
    bash
   git clone https://github.com/samarth-bajaj/Hudl.git
   cd Hudl
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

    While it's optional, it's a good practice to create a virtual environment to isolate project dependencies:

    ```
    python -m venv venv  # Create a virtual environment
    source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
    venv\Scripts\activate  # Activate the virtual environment (Windows)
    ```
    
3. **Install Required Dependencies:**
Navigate to the project's `tests` folder and install the required dependencies using the provided `requirements.txt` file:
    ```
    cd tests
    pip install -r requirements.txt
    ```
4. **Run the Code:**
Execute the code by simply using the command pytest
    ```
    C:\..\..\Hudl\tests>pytest
    ````

5. **About the Code:**

	I have included a few comments in the code where necessary to explain my thought process behind the tests. I have a separate folder inside the `ui_tests` folder which includes all of the fixtures used. There are a few changes I would do if this code was implemented in a work environment.

* Creating an encrypted credentials file that can be used by decrypting it each time instead of one with the email and password written in plaintext as it is not very secure. This file would be included in the .gitignore file so each member of the team will have a copy of this file stored locally.
* I tried creating test cases for the different sign in methods (Facebook, Google and Apple) however I needed accounts for these platforms and was not entirely sure if that was along the lines of testing the login functionality of the website.
* I also tried implementing a test case for the 'Forgot Password' button however this sends an email to my personal email which is not ideal when doing these tests. In a work environment, I would have used Mailtrap to test this functionality along with reading any emails sent and using the links in those emails to reset the password.
* Finally, I would have liked to create API tests as they are usually a lot faster than UI tests, however I could not find suitable API's to use.
