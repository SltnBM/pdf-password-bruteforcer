import pikepdf

def brute_force_pdf(pdf_path, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            passwords = file.read().splitlines()

        for password in passwords:
            try:
                with pikepdf.open(pdf_path, password=password):
                    print(f"[+] Password found: {password}")
                    return password
            except pikepdf.PasswordError:
                print(f"[-] Incorrect password: {password}")
        print("[-] Password not found in the wordlist.")
    except FileNotFoundError:
        print("PDF file or wordlist file not found.")

if __name__ == "__main__":
    pdf_path = input("Enter PDF file path: ")
    wordlist_path = input("Enter wordlist file path: ")
    brute_force_pdf(pdf_path, wordlist_path)
