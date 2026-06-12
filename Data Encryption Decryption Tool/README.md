# Data Encryption and Decryption Tool

## Project Overview

The Data Encryption and Decryption Tool is a Python-based application that provides secure encryption and decryption of messages using AES and RSA cryptographic algorithms. The project demonstrates practical implementation of symmetric and asymmetric encryption techniques while providing a simple graphical user interface for users.

## Objective

* Implement AES and RSA encryption algorithms.
* Provide encryption and decryption functionalities.
* Compare the efficiency and security of both algorithms.
* Understand the concepts of data confidentiality and integrity.

## Features

* AES Encryption and Decryption
* RSA Encryption and Decryption
* User-Friendly Graphical Interface
* File Loading Support
* Save Output to File
* Encryption Performance Measurement
* Security and Efficiency Comparison

## Technologies Used

* Python 3
* Tkinter (GUI)
* PyCryptodome
* Cryptography Library

## Project Structure

Data_Encryption_Decryption_Tool/
│
├── encryption_tool.py
├── requirements.txt
├── README.md
├── Project_Report.pdf
└── screenshots/

## Installation

Clone the Repository

git clone https://github.com/giona-jasley/Data-Encryption-and-Decryption-Tool/tree/main/Data%20Encryption%20Decryption%20Tool

Install Required Libraries

pip install -r requirements.txt

Running the Application

python encryption_tool.py

AES Encryption

AES (Advanced Encryption Standard) is a symmetric encryption algorithm that uses the same key for encryption and decryption.

Advantages

* Fast encryption speed
* High security
* Suitable for large amounts of data

RSA Encryption

RSA (Rivest-Shamir-Adleman) is an asymmetric encryption algorithm that uses a public key and a private key.

Advantages

* Secure key distribution
* Strong authentication support
* Widely used in secure communication

Performance Comparison

| Feature   | AES             | RSA                   |
| --------- | --------------- | --------------------- |
| Type      | Symmetric       | Asymmetric            |
| Key Usage | Single Key      | Public & Private Keys |
| Speed     | Fast            | Slower                |
| Security  | High            | Very High             |
| Best Use  | Data Encryption | Secure Key Exchange   |


## Learning Outcomes

* Understanding cryptographic algorithms
* Working with AES and RSA
* Implementing encryption and decryption systems
* Comparing security and performance trade-offs
* Developing Python GUI applications

## Future Enhancements

* Hybrid AES-RSA Encryption
* Password-Protected Encryption
* Secure File Encryption
* Digital Signature Support
* Cloud-Based Encryption Services


## Conclusion

This project successfully demonstrates the implementation of AES and RSA cryptographic algorithms using Python. The tool provides secure encryption and decryption capabilities while helping users understand modern cryptographic concepts and their practical applications.


## Author

Giona Jasley
