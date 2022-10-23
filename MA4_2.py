#!/usr/bin/env python3.9

from person import Person
from numba import njit

@njit
def fib_numb(n):
	if n <= 1:
		return n
	else:
		return(fib_numb(n-1) + fib_numb(n-2))

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	

if __name__ == '__main__':
	main()

