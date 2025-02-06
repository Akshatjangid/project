class A:
    varA="first class"

class B:
    varB=" second class"

class C(A,B):
    varC=" third class"

s1=C()
print(s1.varA)
print(s1.varB)
print(s1.varC)
    