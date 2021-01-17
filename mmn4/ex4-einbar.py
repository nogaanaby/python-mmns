"""
Student: Ein-Bar Surie
ID: 316011683
Assignment no. 4
Program: vigenere.py
"""
# sum the new value of latin letters
def add_letters(str1: str , str2 : str):
    
    if len(str1) != 1 or len(str2) != 1:
        return None
    
    if not (str1.isalpha and str2.isalpha): #de morgan's laws
        return None
    
    str1 = str1.lower()
    str2 = str2.lower()
    c = ord('a')
    #set a new value for the letters with ASCII
    return chr((((ord(str1[0]) - c) + (ord(str2[0]) - c)) % 26) + c)

# marge 2 strings to one that sum all the values  
def add_string(str1 : str, str2 :str):      
    if not (str1.isalpha and str2.isalpha): #de morgan's laws
        return None
    n_str = ''
    for i in range(min(len(str1), len(str2))):
        c = add_letters(str1[i], str2[i])
        if c == None: 
            return None
        n_str += c
    return n_str

def vigenere_encrypt(s: str, k: str):  
    if not k.isalpha(): #why not false
        return None
    n_s = [c for c in s if c.isalpha()]
    s = ''.join([str(c) for c in n_s])
    n = ((len(s)//len(k))+1)
    t = str(k*n)
    return add_string(s, t)

def vigenere_decrypt(w: str, k: str):
    n = ((len(w)//len(k))+1)
    t = str(k*n)
    a = ord('a')
    t = [chr(( ((ord(c) - a) * -1) + 26) + a ) for c in t]
    t = ''.join([str(c) for c in t])
    return add_string(w,t)
    
def main():
    r1 = (input('Please choose - e or d ? '))
    key = (input('Enter your key: '))
    fileName = (input('Enter the file name: '))

    if r1 == 'e':
        with open (f'{fileName}.txt', 'r') as rf:
            s = rf.read()
            encrypt = vigenere_encrypt(s, key)
            
        with open (f'{fileName}.vig', 'w') as wf:
            wf.write(encrypt)

    elif r1 == 'd':
        with open(f'{fileName}.vig', 'r') as rf:
            s = rf.read()
            decrypt = vigenere_decrypt(s, key)
            print(decrypt)
main()

    