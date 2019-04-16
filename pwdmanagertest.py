import argparse
import sys
import getopt
import pwd
import crypt
import getpass
import keyring
import hashlib
import _md5
from getpass import getpass
import sys

parser = argparse.ArgumentParser(description='username and password for manager')
parser.add_argument('-u', '--userId', type=str, help='The username for the account')
parser.add_argument('-p', '--userPassword', type=str, help='The password for the account')
args = parser.parse_args()

def userLogin(userId , userPassword):
    creds= {}
    creds['user'] = userId.strip()
    creds['cred'] = userPassword.strip()
    return creds

def checkUser(**kwargs):
    plainTextUser = kwargs['user']
    hashedUserName = hashlib.md5(plainTextUser.encode('utf-8')).hexdigest()
    #print("Original username hash", hashedUserName)
    plainTextPassword = kwargs['cred']
    hashedPassword = hashlib.md5(plainTextPassword.encode('utf-8')).hexdigest()
    hashComparisonsDict= {}
    hashComparisonsDict['idChallenge'] = hashedUserName
    hashComparisonsDict['secretChallenge'] = hashedPassword
    return hashComparisonsDict

def userChallenge(**loginChallenge):
    challengeUserNameInput = input("Please re-enter your username: ").strip()
    challengeUserPassword = input("Please re-enter your password: ").strip()
    if loginChallenge['idChallenge'] == hashlib.md5(challengeUserNameInput.encode('utf-8')).hexdigest():
        print("The origional username hash " , loginChallenge['idChallenge'])
        print("Your hash ", hashlib.md5(challengeUserNameInput.encode('utf-8')).hexdigest())
        print("hash match!")
    else:
        print("No match try again")
        sys.exit(0)
    if loginChallenge['secretChallenge'] == hashlib.md5(challengeUserPassword.encode('utf-8')).hexdigest():
        print("The origional Password hash " , loginChallenge['secretChallenge'])
        print("Your password hash " , hashlib.md5(challengeUserPassword.encode('utf-8')).hexdigest())
        print("Password hash match")

    else:
        print("No password match try again")
        sys.exit(0)


def main():
    userLogin(args.userId, args.userPassword)
    checkUser(**userLogin(args.userId, args.userPassword))
    userChallenge(**checkUser(**userLogin(args.userId, args.userPassword)))
if __name__=="__main__":
    main()