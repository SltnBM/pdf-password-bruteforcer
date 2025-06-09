import argparse
import pikepdf

def brute_force_pdf(pdf_path, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist_path}")
        return
    
    try:
        with pikepdf.open(pdf_path):
            print("[*] PDF is not password protected.")
            return
    except FileNotFoundError:
        print(f"[!] PDF file not found: {pdf_path}")
        return
    except pikepdf.PasswordError:
        pass
    
    for password in passwords:
        try:
            with pikepdf.open(pdf_path, password=password):
                print(f"[+] Password found: {password}")
                return password
        except pikepdf.PasswordError:
            print(f"[-] Incorrect password: {password}")
    print("[-] Password not found in the wordlist.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF brute force script")
    parser.add_argument('pdf_path', nargs='?', help='Path to the PDF file')
    parser.add_argument('wordlist_path', nargs='?', help='Path to the password wordlist')
    
    args = parser.parse_args()

    if args.pdf_path and args.wordlist_path:
        pdf_path = args.pdf_path
        wordlist_path = args.wordlist_path
    else:
        pdf_path = input("Enter PDF file path: ")
        wordlist_path = input("Enter wordlist file path: ")

    brute_force_pdf(pdf_path, wordlist_path)
