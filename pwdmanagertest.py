import argparse
import sys
import getopt

'''
Asks the user for their name and password
returns a tuple 
python3 pwdmanagertest.py -u royos -p royos2
('royos','royos2')
'''
def SayHello(username,password):

   # userName = input("Please give me a username: ").strip()
    #Password = input("Please give me a password: ").strip()
   #this is tuple
    return username , password

'''
stores the username and password from SayHello
'''
def storeCreds(*args):
    for i in args:
        print("printing out the arguments",i)
    print(type(args))

def main():

   # SayHello(args.username,args.password)
    parser = argparse.ArgumentParser(description='username and password for manager')
    parser.add_argument('-u', '--username', type=str, help='The username for the account')
    parser.add_argument('-p', '--password', type=str, help='The password for the account')
    args = parser.parse_args()
    print(SayHello(args.username, args.password))
    storeCreds(SayHello(args.username,args.password))

if __name__=="__main__":
    main()