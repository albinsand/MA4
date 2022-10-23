#include <cstdlib>
// Person class 
// fib är lik get

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib();
	private:
		int age;
		int fibn(int);
		
	};
 
Person::Person(int n){
	age = n;
	}
 
 void Person::set(int n){
	age = n;
	}

int Person::get(){
	return age;
	}

int Person::fib(){
	return fibn(age);
	}

int Person::fibn(int n){
	if (n <= 1){
		return (n);
	} else {
		return (fibn(n-1) + fibn(n-2));
	}
}




extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	int fib(Person* person) {return person->get();}	
	}