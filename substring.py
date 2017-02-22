# find a repeated substring that can be appended to the end of the str and have it repeat without any inconsistencies
# EX: str = 'ababa' will return True with substring "ab"
# EX: str = 'aba' will return False since "a" and "b" can't be appended to the end


def substring(str):
	for i in range(1, len(str)/2+1):
		if len(str)%str.count(str[:i])==0 and len(str)/len(str[:i]) == str.count(str[:i]):
			return True
	return False

str = 'abcabcabc'
print substring(str)