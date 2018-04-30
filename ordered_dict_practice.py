from collections import OrderedDict

d = {'banana':3, 'apple':4, 'pear':1, 'orange':2}
print d.keys()
print d.items()
print d.values()
new_d = OrderedDict(sorted(d.items(), key=lambda k: k['value']))
#new_d = OrderedDict(sorted(d.items()))
print new_d

#OrderedDict(sorted(a_dict.items(), key=lambda (k, (v1, v2)): v2))

# concept_sort = sorted(d, key=lambda k: k['value'])
# print concept_sort


# for item in d.items():
#     OrderedDict()