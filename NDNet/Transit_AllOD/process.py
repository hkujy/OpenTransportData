"""
    This code is created process the bus network data 
"""
import pandas as pd
import random
num_bus_line = 20
max_bus_stops = 10

class LinkClass:
    def __init__(self,_a,_b,_t):
        self.tail =_a
        self.head =_b
        self.cost =_|   |   |
|---|---|
|   |   |
t
class ODClass:
    def __init__(self,_o,_d,_val):
        self.origin =_o
        self.dest = _d
        self.demand = _val


# Step 1: Read created bus set
bus_stops = []
df = pd.read_csv("BusSet.csv",header=None)
all_bus_stops = []
for b in range(0,num_bus_line):
    stops = []
    for s in range(0,max_bus_stops):
        stops.append(df[s][b])
    bus_stops.append(stops)
    print(bus_stops[-1])

# Step 2: Write Bus Stop 
bus_num = 1
with open("Stops.txt","w") as f:
    for b in range(0, num_bus_line):
        print("{0}".format(bus_num),end=' ',file = f)
        for s in range(0,len(bus_stops[b])-1):
            print("{0}".format(bus_stops[b][s]),end=' ',file=f)
        print("{0}".format(bus_stops[b][-1]),file=f)
        bus_num=bus_num+1
        all_bus_stops.append(bus_stops[b])
    # for b in range(num_bus_line,0,-1):
    #     # print("{0}".format(bus_num),end=' ',file = f)
    #     line = []
    #     line.append(bus_num)
    #     for s in range(len(bus_stops[b-1]),1,-1):
    #         if bus_stops[b-1][s-1]!=0:
    #             line.append(bus_stops[b-1][s-1])
    #     if len(line)<max_bus_stops:
    #         for i in range(0,max_bus_stops-len(line)-1):
    #             line.append(0)
    #     all_bus_stos.append(line)
    #     print(line)
    #     for s in range(0,len(line)-1):
    #         print("{0}".format(line[s]),file=f,end=" ")
    #     print("{0}".format(line[-1]),file=f)
    #     bus_num=bus_num+1

print("**************Chekck all bus stops")
for b in all_bus_stops:
    print(b)
# Step 3 generate leg seg data 
linkid = pd.read_csv("linkdata.txt",header=None,delimiter=r"\s+")

cost =pd.read_csv("t0.txt",header=None)

num_row = linkid.shape[0]
print("num row = {0}".format(num_row))
links = []

for r in range(0,num_row):
    tail = linkid[0][r]
    head = linkid[1][r]
    t = cost[0][r]
    links.append(LinkClass(tail,head,t)) 
for l in links:
    print("{0},{1},{2}".format(l.tail,l.head,l.cost))

print("***************Check Line Seg Data***********")
with open("LineSegData.txt","w") as f:
    LineIndex = 0
    for b in all_bus_stops:
        LineIndex = LineIndex + 1
        seg = 1
        for i in range(0,len(b)-1):
            now = b[i]
            next_stop = b[i+1]
            if now!=0 and next_stop!=0:
                print("now={0},next={1},line={2}".format(now,next_stop,LineIndex))
                x =[c for c in links if c.tail==now and c.head==next_stop]
                tt =  float(x[0].cost[0])
                # print(tt)
                print("{0} {1} {2} {3} 1".format(LineIndex, seg,tt,
                random.random()*tt),file=f)  # the last 1 is fare dummy
                # print("{0}".format(b[0]),end=" ",file=f)
                # print("now={0},next={1}".format(now,next_stop))
                # x =[c for c in links if c.tail==now and c.head==next_stop]
                # print("{0}".format(seg),end=" ",file=f)
                # print("{0}".format(x[0].cost[0]),end=" ",file=f)
                # print("0",end=" ",file=f)  #variance
                # print("1",file=f)    # fare value set to be 1
                seg = seg +1

with open("NumLineStops.txt","w+") as f:
    for b in range(0,len(all_bus_stops)):
        num_stop = 0
        for s in all_bus_stops[b]:
            if s >0 :
                num_stop =  num_stop + 1
        print("{0} {1}".format(b+1,num_stop),file=f)



# I do not think I need the following

# used_nodes =[False]*25
# odf = pd.read_csv("AllOd.txt",header=None,delimiter=r"\s+")
# od = []
# num_row = odf.shape[0]
# for r in range(0, num_row):
#     origin = odf[0][r]
#     dest = odf[1][r]
#     val = odf[2][r]
#     print("Origin = {0}, Dest = {1}, Val = {2}".format(origin,dest,val))
#     od.append(ODClass(origin,dest,val))

# for b in all_bus_stos:
#     for s in range(1,len(b)):
#         if b[s]!=0:
#             used_nodes[b[s]]=True
# for n in range(0,len(used_nodes)):
#     if used_nodes[n]:
#         print(n)
# new_od = []
# for w in od:
#     if used_nodes[w.origin] and used_nodes[w.dest]:
#         new_od.append(ODClass(w.origin,w.dest,w.demand))
    