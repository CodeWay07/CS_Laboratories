import random
from Ciphers.cipher import Cipher
def randomKey():
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~"
    a = random.randint(1,9)
    c = random.randint(1,9)
    s = 1
    m = int(len(alphaCollection))
    result = ""

    for i in range(s, 9):
        randomNum = (s*a+c) % m
        s = randomNum
        result += alphaCollection[s]
    return result

def encrypt(text, key):
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ "
    new_key = key 
    i = 0 
    result = "" 
    while len(new_key) < len(text):   
        new_key = new_key + key[i] 
        i = (i + 1) % len(key) 
    for alpha, alphaKey in zip(text, new_key):
        newLetterindex = (alphaCollection.index(alpha) + alphaCollection.index(alphaKey)) % int(len(alphaCollection))
        result += alphaCollection[newLetterindex]
    return result


def decrypt(text, key):
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~ "
    new_key = key 
    i = 0 
    result = "" 
    while len(new_key) < len(text):
        new_key = new_key + key[i] 
        i = (i + 1) % len(key) 
    for alpha, alphaKey in zip(text, new_key):
        newLetterindex = (alphaCollection.index(alpha) - alphaCollection.index(alphaKey)) % int(len(alphaCollection))
        result += alphaCollection[newLetterindex]
    return result