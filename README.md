# PDF Password Bruteforcer
A simple Python script to brute-force password-protected PDF files using a wordlist.  

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Requirements](https://img.shields.io/badge/requirements.txt-up%20to%20date-brightgreen)

## Features
- Brute-force PDF passwords using a custom wordlist
- Supports CLI arguments or interactive input
- Simple and lightweight

## Requirements
- Python 3.6+
- [pikepdf](https://pypi.org/project/pikepdf/)

Install dependencies:
```bash
pip install pikepdf
```

## How to Use
1. Make sure you have Python installed (Python 3.6 or higher recommended). Download it from [python.org](https://www.python.org/downloads/).  
2. Clone the repository.
```bash
git clone https://github.com/SltnBM/pdf-password-bruteforcer.git
```
3. Navigate to the project directory.
```bash
cd pdf-password-bruteforcer
```
4. Run the script.
```bash
python pdf_bruteforcer.py
```

## Usage
Option 1: With CLI arguments
```bash
python pdf_bruteforcer.py <path_to_pdf> <path_to_wordlist>
```
Example:
```bash
python pdf_bruteforcer.py secret.pdf wordlist.txt
```

Option 2: Interactive mode
If no arguments are provided, the script will ask for input:
```bash
python pdf_bruteforcer.py
```
Example:
```bash
Enter PDF file path: secret.pdf
Enter wordlist file path: wordlist.txt
[-] Incorrect password: 123456
[-] Incorrect password: password
[+] Password found: letmein123
```

## Disclaimer
This tool is for educational and authorized testing purposes only.
Do not use it on files you do not own or have permission to test.

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

## License
This project is open-source and free to use.