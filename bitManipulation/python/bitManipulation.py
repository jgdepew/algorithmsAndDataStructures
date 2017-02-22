def rAdd(a, b): # recursive
	if b==0:
		return bin(a)
	sum = a ^ b
	carry = (a & b) << 1
	return add(sum, carry)

def add(a, b):
	while b != 0:	
		carry = a & b
		a = a ^ b
		b = carry << 1
	return bin(a)

# print add(0b011, 0b101)

def subtract(a, b): 
	if a < b:
		temp = a
		a = b
		b = temp

	while b != 0:
		borrow = ~a & b
		a = a ^ b
		b = borrow << 1
	return bin(a)

# print subtract(2, 5)

hi = ["hi", "this", "is"]
string = ' '

print string.join(hi)