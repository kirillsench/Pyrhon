things = [10, 25, 40, 84, 125, "Phone", True, 10.2]
'''
for i in things:
    print(i)
for i in things:
    print(i)
'''
iter_obj = iter(things)


#    while(True):
 #       print(iter_obj.__next__())
#except StopIteration as si:
#    print("[StopIteration]")
'''
set_items = set()
set_items.add(10)
set_items.add(25)
set_items.add(40)
set_items.add(125)
set_items.add(True)
set_items.add(10.2)
set_items.add("Hello world")
iter_obj = iter(set_items)

'''

from counter import Counter
try:
    lst = [40]#[50, 100]
    ranGe = Counter(lst)
    while(True):
        print(next(ranGe))
except StopIteration:
    print("End sequence")

