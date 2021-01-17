# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 4
Program: vigenere.py

This program encrypt and decrypt text files by a given key
"""

def split(word): 
    """ utility function: return a splited string into a list of characters """
    return [char for char in word]


LATINE_LETTERS=split("abcdefghijklmnopqrstuvwxyz")


def compileTxt(s):
    """ utility function: return a string that includes only the latine letters from 
    the given s string parameter """
    st=""
    #loop throght all the s string characters and include only the latine letters
    for i in s:
        if i.isalpha():
            st+=i.lower()
    return st


def add_letters(str1,str2):
    """ return a character which indexed by the sum of the two give strings indexes """
    if len(str1)==1 and len(str2)==1 and str1.isalpha() and str2.isalpha():
        str1l=str1.lower()
        str2l=str2.lower()
        res=LATINE_LETTERS.index(str1l)+LATINE_LETTERS.index(str2l)
        if(res>25):
            res=res%26
        return LATINE_LETTERS[res]
    else:
        return 'None'


def decrypt_letters(charKey, charRes):
    """ return the origin character from the result letter encryption with the given character key """
    originIndex=LATINE_LETTERS.index(charRes)-LATINE_LETTERS.index(charKey)
    if(originIndex<0):
      originIndex=LATINE_LETTERS.index(charRes)+26-LATINE_LETTERS.index(charKey)
    return LATINE_LETTERS[originIndex]
  

def add_strings(str1,str2):
    """ return a string which was the result of 
    adding each letter latine index (on the LATINE_LETTERS list) on str1 
    with the index of letter from str2 in the same position"""
    length=min(len(str1),len(str2))
    res=""
    #loop as the shortest string length and add to the result the correct letter from the calculation    
    for i in range(length):
        combine=add_letters(str1[i],str2[i])
        if combine!="None":
            res+=combine
        else:
            return "None"   
    return res


def decrypt_string(key,res):
    """ return the compiled origin string which was the input that was encrypted
    with the given key """
    originSt=""
    #loop as the res string length and decrypt every letter
    for i in range(len(res)):
       originSt+= decrypt_letters(key[i], res[i])
    return originSt


def vigenere_encrypt(s,k):
    """ return the encrypted text with the given key (k) from the given content (s) """
    t=""
    st=compileTxt(s)
    #multiple the key to have at least the length of the given content (s)
    for i in range(0,len(st),len(k)):
        t+=k
    return add_strings(t,st)

def vigenere_decrypt(k,res):
    """ return the compiled origin string which was the input that was encrypted
    with the given key (k)"""
    t=""
    #multiple the key to have at least the length of the result encrypted text (res)
    for i in range(0,len(res),len(k)):
        t+=k
    return decrypt_string(t,res)
     

def test_encryption(filename,encryptext):
    """ utility function: return True if my encryption gave the same result as the example vig and False otherwize """
    output_ex_vig = open(filename+"_correct.vig",'r')
    ex = output_ex_vig.read()
    print(ex==encryptext)
            
        
def test_decryption(filename,decryptext):
    """ utility function: return True if my decryption gave the same result as the compiled origin text and False otherwize """    
    txtFile = open(filename+".txt",'r')
    ex = txtFile.read()                
    print(compileTxt(ex)==decryptext)


def ui(action,filename,key):
    """ encrypt or decrypt the given file (filename) with the given key,
    as you asked: the encryption creates new vig file with the result text 
    and the decryption print the compiled text to the console"""
    if(action=="e"):
        suffix=".txt"
    elif(action=="d"):
        suffix=".vig"
    else:
        return
    
    try:
        f = open(filename+suffix,'r')
        s = f.read()
        if(action=="e"):
            encryptFile = open(filename+".vig", "w")
            encrypt=vigenere_encrypt(s,key)
            encryptFile.write(encrypt)
            #test_encryption(filename,encrypt)
        elif(action=="d"):
            decrypt=vigenere_decrypt(key,s)
            print(decrypt)
            #test_decryption(filename,decrypt)
        f.close()
    except IOError:
        print("File not accessible")

     
def main():
    userChoise=input("for encrypt type 'e', for dycrypt type 'd': ")
    filename=input("please type the name of the file: ")
    key=input("please type a key to encrypt: ")
    ui(userChoise,filename,key)

        
main()

