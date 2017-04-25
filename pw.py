def pwCheck(pw):
	cap = [i for i in pw if i.isupper()]
	low = [i for i in pw if i.islower()]
	num = [i for i in pw if i.isdigit()]
	return len(cap) > 0 and len(low) > 0 and len(num) > 0
