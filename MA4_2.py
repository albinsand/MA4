#!/usr/bin/env python3.9

from time import perf_counter as pc
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
	
nn = 47
print('N: ', nn)
start = pc()
f = Person(nn)
f.fib()
end = pc()
print('fibc: ', end - start)

start = pc()
fib_numb(nn)
end = pc()
print('fib_numb: ', end - start)

x = range(30, 46)
y_py = []
y_numba = []
y_c = []


for n in x:
	print('N: ', n)
	start = pc()
	fib_py(n)
	end = pc()
	y_py.append(end-start)
	print('fib_py: ', end-start)
	start = pc()
	fib_numb(n)
	end = pc()
	y_numba.append(end - start)
	print('fib_numba: ', end-start)
	start = pc()
	f = Person(n)
	f.fib()
	end = pc()
	y_c.append(end - start)
	print('fibc: ', end-start)

#plt.plot(x, y_py, label='Python')
#plt.plot(x, y_numba, label='Numba')
#plt.plot(x, y_c, label='C++')
#plt.savefig('plot_MA42.png')

if __name__ == '__main__':
	main()

