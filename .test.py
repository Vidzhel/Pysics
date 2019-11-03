class A:
	raise NotImplemented()


class B(A):
	raise NotImplemented()


objB = B()
objA = A()

print(isinstance(objB, A))
print(isinstance(objA, type(A)))
