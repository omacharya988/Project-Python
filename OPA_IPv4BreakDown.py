print("IPv4 Break Down Program")
#Asks the user for an IP Address with the subnet prefix.
#Check for that there are no spaces " " in the input string.
#If any of the information is incorrect loop back and ask for the input again.
while True:
    add = input("Please enter an IPv4 Address and prefix (#.#.#.#/Prefix): ")
    if " " in add:
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Prefix")
        print("- Example: 192.168.2.1/24 (no spaces)")
        print()
        continue
    else:
        break
       
       
            
            
    
#Break the input string into IP and Prefix (using "/" to split)
#Break the IP (from above) into a list of octets (using "." to split)
    
break_add = add.split("/")

prefix = int(break_add[1])

My_ip = break_add[0].split(".")

My_ip = [ int(x) for x in My_ip ]

My_join_ip = My_ip
My_join_ip = [str(x) for x in My_join_ip]
My_join_ip = ".".join(My_join_ip)
#You must use Separate Lists to store all the Addresses. (~7 List Variables for IP Address, Network Address,
#Subnet Mask, Wildcard Mask, Network Broadcast Address, Minimum Host IP, and Maximum Host IP)
#for subnet mask in decimal
num = [128,64,32,16,8,4,2,1]
subnet_mask = [255,255,255,255]
if prefix == 8:
    subnet_mask[1]=0
    subnet_mask[2]=0
    subnet_mask[3]=0
elif prefix > 8 and prefix < 16 :
    a = 32-prefix
    c = 24 - a
    d = 0
    for i in num[:c]:
        d = d + i
    subnet_mask[1] = d
    subnet_mask[2] = 0
    subnet_mask[3] = 0
elif prefix == 16:
    subnet_mask[2] = 0
    subnet_mask[3] = 0
elif prefix > 16 and prefix < 24 :
    a = 32 - prefix
    c = 16 - a
    d = 0
    for i in num[:c]:
        d = d +i
    subnet_mask[2] = d
    subnet_mask[3] = 0
elif prefix == 24:
    subnet_mask[3] = 0
elif prefix > 24 and prefix < 32:
    a = 32 - prefix
    c = 8 - a
    d = 0
    for i in num[:c]:
        d = d + i
    subnet_mask[3] = d

join_subnet = subnet_mask
join_subnet = [str(x) for x in join_subnet]
join_subnet = ".".join(join_subnet)


#for wildcard in decimal
wildcard = []
sub = [255,255,255,255]
for i in range(0,4,1):
    wildcard.append(int(subnet_mask[i])^int(sub[i]))

join_wildcard = wildcard
join_wildcard = [str(x) for x in join_wildcard]
join_wildcard = ".".join(join_wildcard)


#for Network add in decimal
Network_add = []
for i in range(4):
    Network_add.append(My_ip[i] & subnet_mask[i])

join_network = Network_add
join_network = [str(x) for x in join_network]
join_network = ".".join(join_network)


#for Broadcast add in decimal
Broadcast = []
for i in range(4):
    Broadcast.append(Network_add[i] | wildcard[i])

join_broadcast = Broadcast
join_broadcast = [str(x) for x in join_broadcast]
join_broadcast = ".".join(join_broadcast)


#for Minimum Host
Min_add = []
for i in range(4):
    if i == 3:
        Min_add.append(Network_add[i]+1)
    else:
        Min_add.append(Network_add[i])

join_mini = Min_add
join_mini = [str(x) for x in join_mini]
join_mini = ".".join(join_mini)


#for maximun host
Max_add = []
for i in range(4):
    if i == 3:
        Max_add.append(Broadcast[i]-1)
    else:
        Max_add.append(Broadcast[i])


join_max = Max_add
join_max = [str(x) for x in join_max]
join_max = ".".join(join_max)


#for Host number
Host = (2 ** (32-prefix))-2


#for My_ip in binary
My_ip_binary = []
a = 0
for i in range(4):
    a = bin(My_ip[i])
    My_ip_binary.append(str(a))
   

#for ip bin to len 8 without Ob

a = My_ip_binary[0]
a = str(a[2:])
for i in range(8):
    if len(a) == 8:
        break
    else:
        a = "0" + a

b = My_ip_binary[1]
b = str(b[2:])
for i in range(8):
    if len(b) == 8:
        break
    else:
        b = "0" + b

c = My_ip_binary[2]
c = str(c[2:])
for i in range(8):
    if len(c) == 8:
        break
    else:
        c = "0" + c

d = My_ip_binary[3]
d = str(d[2:])
for i in range(8):
    if len(d) == 8:
        break
    else:
        d = "0" + d

ip_binary = [ a,b,c,d ]
ip_binary = [str(x) for x in ip_binary]
ip_binary = ".".join(ip_binary)


#for subnet mask in binary



subnet_binary = [ ]
z = 0
for i in range (4):
    z = bin(subnet_mask[i])
    subnet_binary.append(z)

#for removing 0b and making its length 8
a = subnet_binary[0]
a = str(a[2:])
for i in range(8):
        if len(a) == 8:
            break
        else:
            a = "0" + a

b = subnet_binary[1]
b = str(b[2:])
for i in range(8):
        if len(b) == 8:
            break
        else:
            b = "0" + b

c = subnet_binary[2]
c = str(c[2:])
for i in range(8):
        if len(c) == 8:
            break
        else:
            c = "0" + c

d = subnet_binary[3]
d = str(d[2:])
for i in range(8):
        if len(d) == 8:
            break
        else:
            d = "0" + d

sub_net = [ a,b,c,d]
sub_net = [str(x) for x in sub_net]
sub_net = ".".join(sub_net)

#for wild card in binary

wild_binary = []
r = 0
for i in range(4):
    r = bin(wildcard[i])
    wild_binary.append(str(r))


#for making length 8 of wild_binary
a = wild_binary[0]
a = str(a[2:])
for i in range(8):
        if len(a) == 8:
            break
        else:
            a = "0" + a

b = wild_binary[1]
b = str(b[2:])
for i in range(8):
        if len(b) == 8:
            break
        else:
            b = "0" + b

c = wild_binary[2]
c = str(c[2:])
for i in range(8):
        if len(c) == 8:
            break
        else:
            c = "0" + c


d = wild_binary[3]
d = str(d[2:])
for i in range(8):
        if len(d) == 8:
            break
        else:
            d = "0" + d

wild_card=[a,b,c,d]
wild_card=[str(x) for x in wild_card]
wild_card = ".".join(wild_card)


#for conversion of Network_add in binary

Network_binary = []
q = 0
for i in range(4):
    r = bin(Network_add[i])
    Network_binary.append(str(r))


#for making binary length 8 and remove 0b

a = Network_binary[0]
a = str(a[2:])
for i in range(8):
        if len(a) == 8:
            break
        else:
            a = "0" + a

b = Network_binary[1]
b = str(b[2:])
for i in range(8):
        if len(b) == 8:
            break
        else:
            b = "0" + b

c = Network_binary[2]
c = str(c[2:])
for i in range(8):
        if len(c) == 8:
            break
        else:
            c = "0" + c


d = Network_binary[3]
d = str(d[2:])
for i in range(8):
        if len(d) == 8:
            break
        else:
            d = "0" + d

Net_bin =[a,b,c,d]
Net_bin = [str(x) for x in Net_bin]
Net_bin = ".".join(Net_bin)
#print(Net_bin)

#for Broadcast conversion to binary
broadcast_binary = []
w = 0
for i in range (4):
    w = bin(Broadcast[i])
    broadcast_binary.append(str(w))


# for making its length 8 and remove 0b
a = broadcast_binary[0]
a = str(a[2:])
for i in range(8):
        if len(a) == 8:
            break
        else:
            a = "0" + a

b = broadcast_binary[1]
b = str(b[2:])
for i in range(8):
        if len(b) == 8:
            break
        else:
            b = "0" + b

c = broadcast_binary[2]
c = str(c[2:])
for i in range(8):
        if len(c) == 8:
            break
        else:
            c = "0" + c


d = broadcast_binary[3]
d = str(d[2:])
for i in range(8):
        if len(d) == 8:
            break
        else:
            d = "0" + d


broad_bin = [ a,b,c,d ]
broad_bin = [str(x) for x in broad_bin]
broad_bin = ".".join(broad_bin)


#for Min_add in binary
min_binary = []
p = 0
for i in range(4):
    p = bin(Min_add[i])
    min_binary.append(str(p))


#for removing 0b and make its length 8
a = min_binary[0]
a = str(a[2:])
for i in range(8):
        if len(a) == 8:
            break
        else:
            a = "0" + a

b = min_binary[1]
b = str(b[2:])
for i in range(8):
        if len(b) == 8:
            break
        else:
            b = "0" + b

c = min_binary[2]
c = str(c[2:])
for i in range(8):
        if len(c) == 8:
            break
        else:
            c = "0" + c


d = min_binary[3]
d = str(d[2:])
for i in range(8):
        if len(d) == 8:
            break
        else:
            d = "0" + d

Min = [ a,b,c,d ]
Min = [str(x) for x in Min]
Min = ".".join(Min)


# to convert Max_add in binary
max_binary = []
a = 0
for i in range(4):
    a = bin(Max_add[i])
    max_binary.append(str(a))



#to remove 0b and make its length 8
a = max_binary[0]
a = str(a[2:])
for i in range(8):
        if len(a) == 8:
            break
        else:
            a = "0" + a

b = max_binary[1]
b = str(b[2:])
for i in range(8):
        if len(b) == 8:
            break
        else:
            b = "0" + b

c = max_binary[2]
c = str(c[2:])
for i in range(8):
        if len(c) == 8:
            break
        else:
            c = "0" + c


d = max_binary[3]
d = str(d[2:])
for i in range(8):
        if len(d) == 8:
            break
        else:
            d = "0" + d

Max = [ a,b,c,d ]
Max = [str(x) for x in Max]
Max = ".".join(Max)

print()
print("Address:","\t"+My_join_ip+"\t"+ip_binary)
print("Netmask:","\t"+join_subnet+"\t"+sub_net)
print("Wildcard:","\t"+join_wildcard+"\t"+wild_card)
print("--------------------------------------------------------------------")
print("Network:","\t"+join_network+"\t"+Net_bin)
print("Broadcast:","\t"+join_broadcast+"\t"+broad_bin)
print("HostMin:","\t"+join_mini+"\t"+Min)
print("HostMax:","\t"+join_max+"\t"+Max)
print("Host/Net:","\t",Host)

    
    


    









        
    





    

