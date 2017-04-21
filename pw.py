def pwCheck(pw):
	List = [ord(i) for i in pw]
	cap = false
	low = false
	num = false
	for a in List:
		if a >= 65  and a <= 90:
			cap = true
		if a >= 97  and a <= 122:
			low = true
		if a >= 48  and a <= 57:
			num = true
	if cap and low and num:
		print "Passed"
		return true
	else:
		print "Failed"
		return false	

