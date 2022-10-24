"""
Solutions to module 1
Student: Albin Sand
Mail: hansalbinsand@gmail.com
Reviewed by: Tom
Reviewed date: 2022-09-06
"""

import random
import time


def power(x, n):         # Optional
    if n==0:
        return 1
    elif n < 0:
        return 1./power(x,-n)
    else:
        return x * power(x,n-1)
    
    pass
# print(power(2,-2))



def multiply(m, n):      # Compulsory
   
    if n == 1:
        return m
    elif n == 0:
        return 0       
    else:
        return m + multiply(m, n-1)
    pass

# om koden ska bli mer effektiv kan man lägga in ett fall som kollar vilken av m och n som är störst
# och som medför att den som är minst agerar som antalet den större variabeln ska adderad
# på så sätt blir det färe beräkningar för algoritmen

# print(multiply(1,5))


def divide(t, n):        # Optional
    if n == 1:
        return t
    elif n > t:
        return 0
    elif n == t:
        return 1
    else:
         return 1 + divide(t-n, n) 

    pass

#print(divide(7,6))

def harmonic(n):         # Compulsory
    if n == 1:
        return 1
    else: 
        return 1/n + harmonic(n-1)

    pass
# print(harmonic(2))



def digit_sum(x):        # Optional
    if x < 10:
        return x
    else: 
        return x%10 + digit_sum(x//10)
    
    pass
#print(digit_sum(77))

def get_binary(x):       # Optional
    if x == 0:
        return ''
    else:
        return str(x%2) + str(get_binary(x//2))
    pass

#print(get_binary(15))

def reverse(s):          # Optional

    if len(s) <= 1:
        return s
    else:
        mid = len(s)//2
        return reverse(s[mid:]) + reverse(s[:mid])

    pass

#print(reverse([1,2,3,4,5,4]))


def largest(a):          # Compulsory
    
    if len(a) == 1:
        return a[0] 

    else:

        li = largest(a[1:])

        if li > a[0]:
            return li
        else: 
            return a[0]
    
    pass

#print(largest([1,2,3,4,9,5,3,10]))
#print(largest(['9','22']))


def count(x, s):         # Compulsory
    if s == []:
        return 0
    elif type(s[0]) == list:
        if s[0] == x:
            return 1 + count(x,s[0]) + count(x,s[1:]) 
        else:
            return count(x,s[0]) + count(x,s[1:]) 
    else:
        return 1 + count(x,s[1:]) if  s[0] == x else count(x,s[1:])     
    pass

#print(count(4,[[4],4,[4,[4,[4,4,[4,4]]],4,1]]))


def zippa(l1, l2):       # Compulsory

    if len(l1) == 0:
        return l2

    elif len(l2) == 0:
        return l1

    else: 
        return [l1[0]] + zippa(l2,l1[1:]) 
  
    pass
#print(zippa([1,2,3],[3,2,1,1,1]))


def bricklek(f, t, h, n): # Compulsory

    if n == 1: 

        return [f'{f}->{t}']
    return bricklek(f, h, t, n-1) + bricklek(f, t, h, 1) + bricklek(h,t,f,n-1)
    
    pass

#print(bricklek('f','t','h',3))


def fib(n):
    
    memory = {0:0, 1:1}

    def fib_mem (n):
        if n not in memory :
            memory [n] = fib_mem (n-1) + fib_mem (n-2)
        return memory [n]
    return fib_mem (n)


def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  Genom att bryta ner problemet med n brickor till att flytta n-1 brickor till "hjälp platsen" och sedan 
  flytta den sörsta brickan till "mål platsen". Sedan ska n-1 brickor flttas till "mål platsen". Genom
  att expandera detta ges en geometrisk summa som blir följande. (antar att det tar 1 sek att flytta en bricka)
  
  2^n - 1

  n = 50 ger ungerfär: 
   1.2589 ^ 15 [sek] = 35.7 *10 ^6 [år]
  
  
  Exercise 17: Time for Fibonacci:
  
  a)
 n : tid
 0 : 5.266 * 10^-4
 1 : 5.861 * 10^-4 
 2 : 6.402 * 10^-4
 3 : 6.105 * 10^-4
 5 : 6.059 * 10^-4
 10: 7.204 * 10^-4
 15: 7.235 * 10^-4
  
 ungefär  1.618^n * 10^-4

  b)

 fib(50) = 4714.5 [sek] = 1.31 [h]
 fib(100) = 1.325 * 10^14 = 4.2 * 10^8 [år] = 420 M år 

 (känns mycket, gjorde jag på det andra sättet blev det 25 M år på fib(100))
  
  Exercise 20: Comparison sorting methods:
  
  Från uppgiftsbeskrivningen kan konstanterna för de två metoderna beräknas: 

  c_merge = 1 / 3000         c_inst = 10^-6

  n = 10^6 ger:

  Merge : 2000 sek = 33.33 minuter
  inst  : 10^6 sek = 11.57 dagar

  n = 10^9 ger:

  Merge : 3 * 10^6 sek = 34.72 dagar
  inst  : 10^12 sek = 31 688 år
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  Från uppgiftsbeskrivningen kan följande beräknas:  c = 1 / 10
  Genom att sätta:                                   n/10 * log(n) = n
  Ges att dessa är lika då:                          n = 10^10
  Alltså är A snabbare än B då:                      n > 10^10
  

"""