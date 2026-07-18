# . What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

print(len(s))
#why? because 20 and 20.0 are considered the same in python so we have to count only one of them
