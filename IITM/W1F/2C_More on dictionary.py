#Dictionary: 
#d={'key':'value'}
#key = unique= immutable and hashable
#key can be str or boolean value but special case characters are not allowed. 
#value= Duplication is allowed= Can be anything= No restriction on it|| int, str, float

#how to iterate over the dictionary:

d={0:0,1:1,2:4,3:9,4:16}
print(d,type(d))
for key in d:
  print(key, d[key])

#dictionary specific methods:

print(d.keys())
print(d.values())
print(d.items()) #Will give you tuple





