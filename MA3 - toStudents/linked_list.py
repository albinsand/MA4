""" linked_list.py

Student: Albin Sand 
Mail: hansalbinsand@gmail.com
Reviewed by: David Meadon
Date reviewed: 2022 -10 -04
"""


from calendar import c
from pickle import FALSE


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        summa = 0
        if self.first == None:
            return 0
        else:
            f = self.first
            while f != None:
                summa += 1
                f = f.succ
        return summa
        

    def mean(self):               # Optional
        if self.first == None:
            return 0
        else:
            summa = 0
            f = self.first
            while f != None:
                summa += f.data
                f = f.succ
         
        return summa/LinkedList.length(self)  
        

    def remove_last(self):        # Optional
        f = self.first
        if f == None:
            return None
        
        elif f.succ == None:
            b = f.data
            self.first = None
            return b

        else:           
            while f.succ.succ != None:
                                
                f = f.succ            
            
            a = f.succ
            c = a.data
            f.succ = None
        return c
        
 
    def remove(self, x):          # Compulsory

        f = self.first
        if f == None:
            return False 

        elif f.succ == None:
            if x == f.data:
                self.first = None
                return True
            else:
                return False

        else:
            if f.data == x:
                self.first = f.succ
                return True       
            while f.succ and f.succ.data != x:
                f = f.succ
            if f.succ == None:
                return False
            else:
                f.succ = f.succ.succ
                return True
            
          

    def count(self, x):           # Optional
        return self._count(x, self.first)

    def _count(self , x, f):
        
        if f == None:
            return 0
        elif f.succ == None and x == f.data:            
            return 1
        elif f.succ == None and x != f.data:
            return 0

        elif x == f.data:
            return 1 + self._count(x, f.succ)
        else:
            return self._count(x, f.succ)

        

    def to_list(self):            # Compulsory
        return self._to_list(self.first)
    
    def _to_list(self, f):
        
        if f == None:
            return []
        elif f.succ == None: # do we need this case?
            return [f.data]    
        else: 
            return [f.data] + self._to_list(f.succ)


    def remove_all(self, x):      # Compulsory
        return self._remove_all(x,self.first)
    
    def _remove_all(self,x,f):

        if f.succ == None and f.data == x: 
            self.remove_last()
            return self
        if f.data == x:
            f.data = f.succ.data
            f.succ = f.succ.succ
            return self._remove_all(x,f)
        if f.succ != None:
            return self._remove_all(x,f.succ)
                      

    def __str__(self):            # Compulsary

        if self.first == None:
            return '()'
        a = ''
        for x in self:
            a += str(x) + ', '
        return '(' + a[:-2] + ')'


 #   def copy(self):               # Compulsary
 #       result = LinkedList()
 #       for x in self:
 #           result.insert(x)
 #       return result
    ''' Complexity for this implementation: 
    n ^ 2 eftersom vi anänder oss av insert så måste varje nytt element 
    gå igenom hela listan vilket medför:

    (operationer)
    1+2+3+......+n = n^2
    '''

    def copy(self):               # Compulsary (Should be more efficient)

        result = LinkedList()
        f = self.first
        result.first = self.Node(f.data,f.succ)
        while f.succ != None:
            result.succ = f.succ
            f = f.succ

        return result

    ''' Complexity for this implementation:

    Genom att inte använda insert utan istället skapa en ny linkedlist genom att skapa nya noder
    så får man bort komplexiteten från insert och komplexitet blir istället O(n)

    '''

    def __getitem__(self, ind):   # Compulsory
        idx = 0 
        for x in self:
            if ind == idx:
                return x
            else:
                idx += 1
        return None
        
#-----------------------------------------------------------------
class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __it__(self,els): #sort after name
        if self.name < els.name:
            return True
        else:
            return False

    def __le__(self,els):
        if self.name <= els.name:
            return True
        else:
            return False

    def __ge__(self,els):
        if self.name >= els.name:
            return True
        else:
            return False

    def __gt__(self,els):
        if self.name > els.name:
            return True
        else:
            return False

    def __eq__(self,els):
        if self.name == els.name and self.pnr == els.pnr:
            return True
        else: 
            False

    def __ne__(self,els):
        if self == els:
            return False
        else:
            return True
#-----------------------------------------------------------------
def main():

    lst = LinkedList()
    for x in [5,2,8,7,1,4]:
        lst.insert(x)
        
#    print(lst)       #demonstration för __str()__

 #   lst.print()

    # Test code:

# Length

#    le = lst.length()
#    print(le)

# Mean

#    lst1 = lst.mean()
#    print(lst1)

# Remove_Last

#    lst2= lst.remove_last()
#    print(lst2)

# Remove
#    print(lst)
#    lst.remove(1)
#    print(lst)

# Count

#    lst1 = lst.count(3)
#    print(lst1)

# to_list

#    lst1 = lst.to_list()
#    print(lst1)

# remove_all

#    lst1 = lst.remove_all(5)
#    print(lst1)

# getitem

#    lst1 = lst.__getitem__(6)
#    print(lst1)

if __name__ == '__main__':
    main()
