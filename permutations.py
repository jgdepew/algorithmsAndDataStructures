# def permutations(s):
# 	arr = []
# 	rpermutations(s, "", arr)
# 	return arr

# def rpermutations(s, prefix, arr):
# 	if len(s) == 0:
# 		arr.append(prefix)
# 	else:
# 		for i in xrange(len(s)):
# 			rem = s[0:i] + s[i+1:]
# 			rpermutations(rem, prefix+s[i], arr)

def permutations(s):
	arr = []
	rpermutations(s, [], arr)
	return arr

def rpermutations(s, prefix, arr):
	if len(s) == 0:
		arr.append(prefix)
	else:
		for i in xrange(len(s)):
			rem = s[0:i] + s[i+1:]
			idx = [s[i]]
			prefix.extend(idx)
			rpermutations(rem, prefix, arr)

print permutations("cat")
