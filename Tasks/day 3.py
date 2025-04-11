s = {1, 2, 3}
s.add(4)
print(s) 
s.clear()
print(s)  
s = {1, 2, 3}
new_set = s.copy()
print(new_set)  
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.difference(s2))  
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s1.difference_update(s2)
print(s1)  
s = {1, 2, 3}
s.discard(2)
print(s)  
s.discard(5)  
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.intersection(s2))  
print(s1 & s2)  
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print(s1.issubset(s2))  
print(s1 <= s2)  
s1 = {1, 2, 3, 4}
s2 = {1, 2}
print(s1.issuperset(s2))  
print(s1 >= s2)  
s = {1, 2, 3, 4}
print(s.pop()) 
print(s)  
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))  
print(s1 | s2)  




