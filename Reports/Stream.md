# Stream Cipher

## Theory

&ensp;&ensp;&ensp; A stream cipher is a symmetric key cipher where plaintext digits are combined with a pseudorandom cipher digit stream (keystream). In a stream cipher, each plaintext digit is encrypted one at a time with the corresponding digit of the keystream, to give a digit of the ciphertext stream. Since encryption of each digit is dependent on the current state of the cipher, it is also known as state cipher. In practice, a digit is typically a bit and the combining operation is an exclusive-or (XOR).

## Implementation

&ensp;&ensp;&ensp; This is a simple stream cipher, which uses LCG pseudo random number algorithm

### Initial Steps:

&ensp;&ensp;&ensp; For start we use the random key generator, which performs on the basis of a LCG random number algorithm.

```
def randomKey(): #random key generator
    alphaCollection = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'?!@#$%^&*()~" #ascii collection
    a = random.randint(1,9) #random multiplier
    c = random.randint(1,9) #random counter
    s = 1
    m = int(len(alphaCollection)) #modulo the length of alphaCollection
    result = "" #store the new key

    for i in range(s, 9):
        randomNum = (s*a+c) % m
        s = randomNum
        result += alphaCollection[s]
    return result
```

### Encryption

&ensp;&ensp;&ensp; In the encryption part we use the new key and index position of each character. With that we add all characters together and do modulo the length of alphaCollection. Afterwards, just add the characters from alphacollection based on the new index.

```
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
```

### Decryption

&ensp;&ensp;&ensp; Same as encryption. Only difference is that we perform a backwards operation in newLetterindex.

```
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
```

## Screenshots

![](https://github.com/CodeWay07/CS_Laboratories/blob/main/Resources/stream.png)
