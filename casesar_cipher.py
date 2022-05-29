#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 16:09:29 2022

@author: aoli
"""
plainText = input("Secret message: ")
shift = int(input("Shift: "))

def caesar_cipher(plainText, shift): 
  cipherText = ""
  for c in plainText:
    print(c+" ," )
    #ch.isalpha（）：字符是否由字母组成
    if c.isalpha():
        # ord()字符对应的 ASCII数值:a = 97, A = 65
      cipherNumber = ord(c) + (shift % 26)
          
      """chr (number)
          number: 字符值的ASCII码
          str: 返回的字符，比如'A'
          
          
      """
      transforChar = chr(cipherNumber)
      
      cipherText += transforChar
      
  print("final cihper text is: " + cipherText)
  return cipherText

caesar_cipher(plainText, shift)