""" bst.py

Student: Albin Sand    
Mail: hansalbinsand@gmail.com
Reviewed by: David Meadon
Date reviewed: 2022-10-04

"""


from turtle import right
from linked_list import LinkedList
import random
import math

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        
        return self._height(self.root)

    def _height(self, r):         

        if r == None:
            return 0
        else:
            left_tree = self._height(r.left)
            right_tree = self._height(r.right)

            return max(left_tree,right_tree) + 1

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                         # Compulsory
        if r is None:
            return None

        elif k < r.key:
             r.left = self._remove(r.left,k)         #left subtree with k removed
        elif k > r.key:
             r.right = self._remove(r.right,k)       #right subtree with k removed

        else:                                        # This is the key to be removed
            if r.left is None:                       # Easy case
                return r.right
            elif r.right is None:                    # Also easy case
                return r.left
            else:                                    # This is the tricky case.
                
                l = self._get_largest(r.left)        # Find the largest key in the lest subtree
                r.key = l.key                        # Put that key in this node
                r.left = self._remove(r.left,l.key)  # Remove that key from the left subtree
        return r                                     # Remember this! It applies to some of the cases above

    def _get_largest(self,r): 
        if r.right != None:
            return self._get_largest(r.right)
        return r

    def __str__(self):                         # Compulsory
        if self.root == None:
            return '<>'
        a = ''
        for x in self:
            a += str(x) + ', '
        return '<' + a[:-2] + '>'

    def to_list(self):                            # Compulsory

        if self.root == None:
            return []
        a = []
        for x in self:
            a.append(x)
        return a


    def to_LinkedList(self):                      # Compulsory
        
# komplexiteten är n^2 eftersom att itterera igenom listan ger n operationer
# sedan kräver insert n operationer för varje ellment vilket vlir n^2

        res = LinkedList()
        for x in self:
            res.insert(x)
        return res
             

    def ipl(self):                                # Compulsory
        return self._ipl(self.root,1)

    def _ipl(self, r, add): 

        if r == None:
            return 0
        else: 
            return add + self._ipl(r.left,1+add) + self._ipl(r.right,1+add)

def random_tree(n):                               # Useful
    tt = BST()
    for i in range(n):
        tt.insert(random.random())
    return tt

def main():
    t = BST()
    for x in [1,2,4,5,7,5,4,3,5,3,4]:
        t.insert(x)
    t.print()
    print()


    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


#    print(t.height())

#    print(t)
#    t.remove(6)
#    print(t)

# Upg 20

    a = []
    for x in range(1,1000):
        trad = random_tree(x)
        hojd = trad.height()                  # Höjd
        ipl = trad.ipl()                      # intern väglängd
        expext_r =  1.39 * math.log2(x)       # teoretirskt samband
        real_r = ipl / x                      # vrekligt samband
        element = real_r - expext_r           # diff
        a.append(element)    
 #       print(f'n:{x : >2}, R: {real_r: >18}, E: {expext_r : >18}, Height: {hojd : >3}')# ,Koeff: {element :>5}')
 #   print(sum(a)/len(a))


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Ja
2. computing height? Nej
3. contains? Ja
4. insert? Nej 
5. remove? Nej 

En generator går bara igenom element, den har inte koll på vad omgivande element
har för information

Results for ipl of random trees
===============================

n = antal slumptal , R = ipl / n , E = teoretiska förhållandet utan konsant
Height = trädets höjd

konstanten blir ungefär O(1)=-1.855, höjden följer log_2(n) förhållande

n: 1, R:                1.0, E:                0.0, Height:   1
n: 2, R:                1.5, E:               1.39, Height:   2
n: 3, R:                2.0, E: 2.2030978760024067, Height:   3
n: 4, R:                2.0, E:               2.78, Height:   3
n: 5, R:                2.2, E:  3.227480051893433, Height:   3

n:505, R: 10.388118811881188, E: 12.482394012918428, Height:  18
n:506, R:  9.865612648221344, E:  12.48636106882509, Height:  17
n:507, R:  10.77120315581854, E: 12.490320292434644, Height:  19
n:508, R:   9.59251968503937, E: 12.494271714613308, Height:  17
n:509, R: 11.119842829076621, E: 12.498215366045216, Height:  20

"""
