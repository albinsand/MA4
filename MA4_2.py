#!/usr/bin/env python3.9


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

	start = pc()
	fib_numb(47)
	end = pc()
	print(f"tid for berakning av fib(47) med numba: {round(end - start, 2)} sek")

	start = pc()
	f.fib(47)
	end = pc()
	print(f"tid for berakning av fib(47) med C++: {round(end - start, 2)} sek")


if __name__ == '__main__':
	main()

'''
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

	a = plt.figure()
	plt.plot(nn,tid_fib,label ="C++",color='red')
	plt.plot(nn,tid_numb,label ="numb",color='blue')
	plt.plot(nn,tid_py,label ="python",color='green')
	plt.legend()
	plt.savefig(f'fib test for different methods.png')
'''
###########################################################
'''
	nnn = range(20,31)
	ttid_py = []
	ttid_numb = []

	for n in nnn:
		start = pc()
		print(fib_py(n))
		end = pc()
		t = end - start
		ttid_py.append(t)

	
		start = pc()
		print(fib_numb(n))
		end = pc()
		tt = end - start
		ttid_numb.append(tt)

	aa = plt.figure()
	plt.plot(nnn,ttid_numb,label ="numb - (20 till 30)")
	plt.plot(nnn,ttid_py,label ="python - (20 till 30)")
	plt.legend()
	plt.savefig('fib for numba and python.png')
	
'''
##################################################




