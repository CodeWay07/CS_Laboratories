# Cryptography & Security Laboratory Work 3

### University: _Technical University of Moldova_

### Faculty: _Computers, Informatics and Microelectronics_

### Department: _Software Engineering and Automatics_

### Author: _Maxim Bugăescu_

---

## Theory

&ensp;&ensp;&ensp;     Asymmetric Cryptography (a.k.a. Public-Key Cryptography)deals with the encryption of plain text when having 2 keys, one being public and the other one private. The keys form a pair and despite being different they are related.

&ensp;&ensp;&ensp; As the name implies, the public key is available to the public but the private one is available only to the authenticated recipients.

&ensp;&ensp;&ensp; A popular use case of the asymmetric encryption is in SSL/TLS certificates along side symmetric encryption mechanisms. It is necessary to use both types of encryption because asymmetric ciphers are computationally expensive, so these are usually used for the communication initiation and key exchange, or sometimes called handshake. The messages after that are encrypted with symmetric ciphers.

## Objectives

1. Get familiar with the asymmetric cryptography mechanisms.

2. Implement an example of an asymmetric cipher.

3. As in the previous task, please use a client class or test classes to showcase the execution of your programs.

## Implementations

1. [RSA Cipher](https://github.com/CodeWay07/CS_Laboratories/blob/main/Reports/RSA.md)
