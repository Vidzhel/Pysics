class A:
	pass


class B(A):
	pass


objB = B()
objA = A()

print(isinstance(objB, A))
print(isinstance(objA, type(A)))
