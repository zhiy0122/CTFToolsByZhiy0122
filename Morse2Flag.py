# !/usr/bin/python
# -*-coding:UTF-8-*-
# Author:zhiy0122
import time

message='''
|------------------------前言------------------------------------|
本脚本用于解答XCTF攻防世界Misc题目stegano                           
                                                               
输入AB组成的密文即可转换为摩斯密码并解码为flag                   
                                                               
作者：zhiy0122                                                 
                                                               
github地址：https://github.com/zhiy0122/MiscToolsByZhiy0122.git 
---------------------------------------------------------------|
'''

print(message)

time.sleep(2)

str = input("请输入AB密文:")

def replaceAll(input,ireplace,replaceWith):
    while(input.find(ireplace) > -1):
        input = input.replace(ireplace,replaceWith)
    return input

str1 = replaceAll(str,"A",".")

str1 = replaceAll(str1,"B","-")

print("摩斯密码为：")
print(str1)

time.sleep(2)

s = str1.split(" ")

dict = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---':'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.',
        '--..--':',',
        '---...':':'
        };

print("Flag信息为：")

for item in s:
    print(dict[item],end=' ')

