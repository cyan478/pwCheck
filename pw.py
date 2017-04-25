def pwCheck(pw):
	cap = [i for i in pw if i.isupper()]
	low = [i for i in pw if i.islower()]
	num = [i for i in pw if i.isdigit()]
	return len(cap) > 0 and len(low) > 0 and len(num) > 0

def pwStrength(pw):
  if pwCheck(pw) and len(pw) < 5:
    return 1
  elif pwCheck(pw) and len(pw) < 6:
    return 2
  elif pwCheck(pw) and len(pw) < 8 and not(pw[len(pw)-1].isdigit()):
    pw1 = [i for i in pw if i.isupper() or i.islower()]
    low = pw1[0].islower()
    for i in pw1[1:]:
      if i.islower() != low:
        low = not(low)
      else:
        return 3
    return 4
  elif pwCheck(pw) and len(pw) < 8 and pw[0].islower():
    return 3
  elif pwCheck(pw) and len(pw) >= 8 and not(pw[len(pw)-1].isdigit()):
    return 5
  else:
    return 0
    
'''tests:
print pwStrength("1lS")
print pwStrength("1sfeK")
print pwStrength("aBS32s")
print pwStrength("aDe5FlM")
print pwStrength("as85SJKjsNo")
'''