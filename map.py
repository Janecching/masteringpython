"""hashmap - insert/remove/search O(1)"""
hmap = {"a":1, "b":2}
hmap["a"]=3
print(len(hmap))
print("a" in hmap)
hmap.pop("a")
max(hmap.values) #get largest from hmap values
hmap = {i:2*i for i in range(3)} #for graph, adj list
for k in hmap: print(k, hmap[k])
for v in hmap.values(): print(v)
for k,v in hmap.items(): print(k,v)
pmap = {c:p.count(c) for c in set(p)}
d[key] = d.setdefault(key, 0) + 1
