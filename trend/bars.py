import matplotlib.pyplot as p
import numpy as n

def bars_plot(hash_tag,count):
    m=n.max(count)
    i=0
    while(m!=0):
        m=m/10
        i=i+1
    #fig,ax = p.subplots()
    bar_width = 4.0/i
    bar_locations = n.arange(len(hash_tag))
    p.xticks(bar_locations,hash_tag)
    p.yticks(n.linspace(0,m+(10**i),100))
    p.bar(bar_locations,count,bar_width)
    p.title("Hash_tag popularity analysis")
    p.xlabel("(Hash_Tags)")
    p.ylabel("(No of shares * %d)" % (10**(i-1)))
    p.legend(["Popular_hash_tag :%s"%hash_tag[count.index(n.max(count))]])
    p.show()
