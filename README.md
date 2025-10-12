CipherSphere: The Modern Encryption Tool
CryptoCraft is a dynamic and highly stylized web application for text encryption, decryption, and hashing. Built with Python and the Streamlit framework, it provides a user-friendly interface for performing cryptographic operations using various algorithms. The application's standout feature is its futuristic, animated UI, crafted with custom CSS to create an engaging "cyber" aesthetic.

(Pro Tip: Take a screenshot of your running app, upload it to a site like Imgur, and paste the link here to show off your UI!)

Features
Multiple Algorithms: Encrypt and decrypt using Caesar Cipher, AES, and Base64 encoding.

Secure Hashing: Generate secure SHA-256 hashes for any text input.

Stunning Animated UI: A fully custom-styled interface with:

Animated background gradients.

Pulsating neon glows on titles and buttons.

Floating "aurora" orbs in the background.

A "breathing" focus effect on text areas.

Intuitive Layout: A clear side-by-side view for plain text and cipher text, matching the project's design sketch.

Organized Codebase: The project is structured into separate files for logic (ciphers.py), UI styling (ui_components.py), and the main application (app.py).

 Tech Stack
Framework: Streamlit

Language: Python

Cryptography Library: PyCryptodome

Styling: Custom CSS injected into Streamlit

 How to Run Locally
Follow these steps to get the application running on your local machine.

1. Clone the Repository

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install all the required libraries from the requirements.txt file.

pip install -r requirements.txt

4. Run the Streamlit App
Execute the following command in your terminal.

streamlit run app.py

The application should automatically open in a new tab in your web browser!

File Structure
The project is organized into the following key files:

app.py: The main application file. It handles the page layout, user inputs, and button logic.

ciphers.py: Contains all the functions for the cryptographic operations (Caesar, AES, Base64, SHA-256).

ui_components.py: Contains a single function to inject all the custom CSS for the animated UI.

requirements.txt: Lists all the Python libraries required to run the project.


---

### How to Upload Your Project to GitHub from PyCharm

This is a detailed, step-by-step guide.

**Step 1: Get Your Project Ready**

1.  **Create `.gitignore`**: This is a very important step to prevent uploading unnecessary files (like your virtual environment).
    * In the PyCharm project panel, right-click your main folder -> **New** -> **File**.
    * Name the file `.gitignore` (the dot at the beginning is crucial).
    * Paste the following content into it:
        ```
        # Virtual Environment
        venv/
        .venv/

        # PyCharm files
        .idea/

        # Python cache
        __pycache__/
        *.pyc
