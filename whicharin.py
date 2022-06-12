a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = [] 


for first in a1:
    for second in a2:        
        try: 
            if second.index(first) >= 0 and not first in r:
                r.append(first)
        except:
	        pass            
print(sorted(r))