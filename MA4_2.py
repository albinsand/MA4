#!/usr/bin/env python3.9

from cProfile import label
from time import perf_counter as pc
from person import Person
from numba import njit
import matplotlib.pyplot as plt


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
	f.set(9)
	print(f.get())

	nn = range(30,46)
	tid_py = []
	tid_numb = []
	tid_fib = []

	for n in nn:
		start = pc()
		print(f.fib(n))
		end = pc()
		t = end - start
		tid_fib.append(t)

	
		start = pc()
		print(fib_numb(n))
		end = pc()
		tt = end - start
		tid_numb.append(tt)

	
		start = pc()
		print(fib_py(n))
		end = pc()
		ttt = end - start
		tid_py.append(ttt)


	a = plt.plot(nn,tid_fib,label ="fib - C++")
	b = plt.plot(nn,tid_numb,label ="fib - numb")
	c = plt.plot(nn,tid_py,label ="fib - python")


	plt.savefig(f'fib-C++-{a}.png')
	plt.savefig(f'fib-numb-{b}.png')
	plt.savefig(f'fib-python-{c}.png')

if __name__ == '__main__':
	main()


