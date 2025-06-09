# PDF Password Bruteforcer
A simple Python script to brute-force password-protected PDF files using a wordlist.  

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
python pdf_bruteforcer.py file_protected.pdf wordlist.txt
```

Option 2: Interactive mode
If no arguments are provided, the script will ask for input:
```bash
python pdf_bruteforcer.py
```
Example:
```bash
Enter PDF file path: file_protected.pdf
Enter wordlist file path: wordlist.txt
[-] Incorrect password: 1234
[-] Incorrect password: admin
[-] Incorrect password: password
[+] Password found: secret
```