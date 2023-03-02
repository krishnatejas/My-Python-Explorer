res = [{'name':'node1','sub':[{'name':'child1','sub':[]},{'name':'child2','sub':[{'name':'child2.1','sub':[]}]}]},
       {'name':'node2','sub':[{'name':'child3','sub':[{'name':'child3.1','sub':[{'name':'child3.1.1','sub':[]}]}]}]},
       {'name':'node3','sub':[]},
       {'name':'node4','sub':[{'name':'child4','sub':[]}]}]
def traverse( item , tab=""):
    print( tab + item["name"] )
    for itm in item['sub']:
        if itm['sub'] == []:
            tab += "\t"
            traverse(itm,tab)
        else:
            tab = "\t"
            traverse(itm,tab)
##            for i in itm['sub']:
##                tab += "\t"
##
    else:
        tab = ""

for itm in res:
    traverse(itm)
