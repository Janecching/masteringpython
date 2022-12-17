#OPERATIONS
s="abc"
print(s[0:2])
s+="def" #creates new string
s=["x","y","z"]
print("".join(s))

#EDGE CASES
s="" #empty str
s="a" #str with 1 or 2 char
s="aa" #str with repeated char
s="ab" #str with only distinct char

#COMPLEXITY
print(s[0:1])   # access	O(1)
print('a' in s) # Search	O(n)
# Insert	O(n)
# Remove	O(n)
# Find substring	O(n.m)
# Concatenating strings	O(n + m)	
# Slice	O(m)	
# Split (by token)	O(n + m)	
# Strip (remove leading and trailing whitespaces)	O(n)

#TECHNIQUES
