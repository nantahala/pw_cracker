#Author: Jay
#Purpose: to crack passwords and password hashes on Unix based systems
import crypt
import sys
import argparse

def parse_args():
    parser.add_argument('-f', help='file containing hashes', dest='file')

#Takes the encrypted password as a parameter and returns either after finding the password or exahausting the words in th dictionary.
def testPass(cryptPass):
    salt = cryptPass[0:2]
    #replace with userinput /path/to/file
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+ word +"\n"
            return
    print "[-] Password Not Found.\n"
    return
def main():
    #replace this with user input /path/to/file
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(":")[1].strip(' ')
            print "[*] Cracking Password For: "+ user
            testPass(cryptPass)
if __name__== "__main__":
    main()