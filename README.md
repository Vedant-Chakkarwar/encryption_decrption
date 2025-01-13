# Simple Encryption-Decryption CLI with Authentication
This project is a Python-based Command-Line Interface (CLI) application that allows users to perform text encryption and decryption using a keyword-based substitution cipher. It includes a basic authentication mechanism to secure access to the encryption and decryption functionalities.

## Features
- Authentication: Secure login functionality with username and hashed password storage using bcrypt.
- Keyword-Based Substitution Cipher:
  - Encrypt text using a keyword to generate a custom cipher alphabet.
  - Decrypt text back to its original form using the same keyword.
- User-Friendly Interface:
  - CLI prompts for easy interaction.
  - Retry options for authentication and repeated operations.
## How It Works
### Authentication:
- Predefined username and password are required to access the tool.
- Passwords are securely hashed using bcrypt.
### Encryption and Decryption:
- Users input a keyword to create a custom cipher alphabet.
- Text is encrypted or decrypted based on the substitution cipher created from the keyword.
