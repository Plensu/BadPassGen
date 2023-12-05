import argparse
import string

from Crypto.Hash import MD4
from functools import reduce
from itertools import product


def makeHash(password):
    hash = MD4.new(password.encode('utf-16le')).hexdigest().upper()
    return hash

# This function takes the mask (Exmaple: password/d/d) and returns a list of every location an argument exists.
# For example, the list should be [8, 10] since the first /d starts at position 8 and the second /d starts at position 10.

def getMaskArgsIndices(mask):
    margIndices = []
    maskArgs = ['/d','/l','/u','/s','/a']
    for marg in maskArgs:
        j = 0
        for i in range(len(mask)):
            margindex = mask.find(marg, j)
            if margindex != -1:
                margIndices.append(margindex)
                j = margindex + 1
    return(margIndices)

# This function takes the mask. the order of arguments, and the mutation as arguments to then create and return the passwword.
# Example: mask=password/d/s/u
# maskArgs = ['/d','/s','/u']
# mutation = ['7','%','I']
# password = password7%I

def passReplacer(mask, maskArgs, mutation):
    password = mask
    for x in range(len(maskArgs)):
        password = password.replace(maskArgs[x], mutation[x], 1)
    return password
    
# This function takes the mask and the mask argument positions to create the possible mutations.

def generateMutations(margIndices, mask):
    listOfLists = []
    argOrder = []
    for i in margIndices:
        if mask[i:i+2] == '/d':
            listOfLists.append(list(string.digits))
            argOrder.append('/d')
        elif mask[i:i+2] == '/l':
            listOfLists.append(list(string.ascii_lowercase))
            argOrder.append('/l')
        elif mask[i:i+2] == '/u':
            listOfLists.append(list(string.ascii_uppercase))
            argOrder.append('/u')
        elif mask[i:i+2] == '/s':
            listOfLists.append(list(string.punctuation))
            argOrder.append('/s')
        elif mask[i:i+2] == '/a':
            everything = string.ascii_letters + string.digits + string.punctuation
            listOfLists.append(list(everything))
            argOrder.append('/a')
    mutations = list(reduce(lambda a,b: [(*p[0], p[1]) for p in product(a,b)], listOfLists))
    return mutations, argOrder

# This function takes the mask and generates a list of possible passwords

def passwordGenerator(mask):
    passwordList = []
    margPositions = getMaskArgsIndices(mask)
    mutations, argOrder = generateMutations(margPositions, mask)
    for x in mutations:
        password = passReplacer(mask, argOrder, x)
        passwordList.append(password)
    return passwordList

# Custom help is the best help.

def help():
    customHelp = """usage: Bad Password Generator [-h] [-o OUTFILE] [--ntlm] [--both] mask

Generate a list of bad passwords or NTLM hashes.

positional arguments:
mask                    The password mask to use.

options:
-h, --help              Show this help message and exit.
-o OUTFILE, --outfile OUTFILE
                        Write output to a file.
--ntlm                  Output only NTLM.
--both                  Output both clear text and NTLM.

Password Mask Options:
    /d for digits
    /l for lowercase
    /u for uppercase
    /s for special characters
    /a for all of the previous options"""
    print(customHelp)

# Are you still reading my comments?

def main():
    parser = argparse.ArgumentParser(prog='Bad Password Generator', description='Generate a list of bad password or NTLM hashes.', add_help=False)
    parser.add_argument('mask')
    parser.add_argument('-o', '--outfile')
    parser.add_argument('--ntlm', action='store_true')
    parser.add_argument('--both', action='store_true')
    parser.add_argument('-h', '--help', action='store_true')

    args = parser.parse_args()
    if args.help:
        help()

    elif args.ntlm:
        hashList = []
        passwordList = passwordGenerator(args.mask)
        for password in passwordList:
            hash = makeHash(password)
            hashList.append(hash)
            print(hash)
        if args.outfile:
            with open(args.outfile, 'w') as file:
                file.writelines('\n'.join(hashList))

    elif args.both:
        bothList = []
        passwordList = passwordGenerator(args.mask)
        for password in passwordList:
            hash = makeHash(password)
            passHash = password +':' + hash
            bothList.append(passHash)
            print(passHash)
        if args.outfile:
            with open(args.outfile, 'w') as file:
                file.writelines('\n'.join(bothList))

    else:
        passwordList = passwordGenerator(args.mask)
        for password in passwordList:
            print(password)
        if args.outfile:
            with open(args.outfile, 'w') as file:
                file.writelines('\n'.join(passwordList))

if __name__ == '__main__':
    main()