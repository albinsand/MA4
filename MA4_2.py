#!/usr/bin/env python3.9

from time import perf_counter as pc
from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(9)
	print(f.get())

	print(f.fib(10))
	print(f.fib_numb(10))
	print(f.fib_py(10))

if __name__ == '__main__':
	main()


'''	
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
'''

#plt.plot(x, y_py, label='Python')
#plt.plot(x, y_numba, label='Numba')
#plt.plot(x, y_c, label='C++')
#plt.savefig('plot_MA42.png')


