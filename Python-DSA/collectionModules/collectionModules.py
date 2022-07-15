# Python collection module was introduced to improve the functionality of the built-in datatypes. It provides various containers let’s see each one of them in detail.
from collections import Counter,OrderedDict,defaultdict,ChainMap


# Counter
    # subclass of Dictionary -it gives Counter of elements in array in unordered
print(Counter(['B','B','A','B','C','A','B','B','A','C']))


# OrderDict
    #subclass of Dictionary -it gives order in which elememnts are inserted in that particular dictionary
od=OrderedDict()
od['a']=3
od["b"]=2
print(od)

# defaultdict
    # DefaultDict is used to provide some default values for the key that does not exist and never raises a KeyError
d=defaultdict(int)
a=[2,3,4,5,6,7]
for i in a:
    d[i]+=1
print(d)

# chainmap
    #  encapsulates many dictionaries into a single unit and returns a list of dictionaries.