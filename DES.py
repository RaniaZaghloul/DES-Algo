import binascii
pc1_list = []
shift1 = []
shift2 = []
key2_list = []
pc2_list = []

def padhexa(s):
    return  s[2:].zfill(12)

def PC1(key_list):
    pc1_list = [ key_list [56] ,key_list [48] ,key_list [40] ,key_list [32] ,key_list [24] ,key_list [16] ,key_list [8] ,key_list [0] ,key_list [57] ,key_list [49] ,key_list [41] ,key_list [33] ,key_list [25] ,key_list [17] ,key_list [9] ,key_list [1] ,key_list [58] ,key_list [50] ,key_list [42] ,key_list [34] ,key_list [26] ,key_list [18] ,key_list [10] ,key_list [2] ,key_list [59] ,key_list [51] ,key_list [43] ,key_list [35] ,key_list [62] ,key_list [54] ,key_list [46] ,key_list [38] ,key_list [30] ,key_list [22] ,key_list [14] ,key_list [6] ,key_list [61] ,key_list [53] ,key_list [45] ,key_list [37] ,key_list [29] ,key_list [21] ,key_list [13] ,key_list [5] ,key_list [60] ,key_list [52] ,key_list [44] ,key_list [36] ,key_list [28] ,key_list [20] ,key_list [12] ,key_list [4] ,key_list [27] ,key_list [19],key_list [11] ,key_list [3]]
    return pc1_list

def Shift1(pc1_list):
    shift1 =[pc1_list[1],pc1_list[2],pc1_list[3],pc1_list[4],pc1_list[5],pc1_list[6],pc1_list[7],pc1_list[8],pc1_list[9],pc1_list[10],pc1_list[11],pc1_list[12],pc1_list[13],pc1_list[14],pc1_list[15],pc1_list[16],pc1_list[17],pc1_list[18],pc1_list[19],pc1_list[20],pc1_list[21],pc1_list[22],pc1_list[23],pc1_list[24],pc1_list[25],pc1_list[26],pc1_list[27],pc1_list[0],pc1_list[29],pc1_list[30],pc1_list[31],pc1_list[32],pc1_list[33],pc1_list[34],pc1_list[35],pc1_list[36],pc1_list[37],pc1_list[38],pc1_list[39],pc1_list[40],pc1_list[41],pc1_list[42],pc1_list[43],pc1_list[44],pc1_list[45],pc1_list[46],pc1_list[47],pc1_list[48],pc1_list[49],pc1_list[50],pc1_list[51],pc1_list[52],pc1_list[53],pc1_list[54],pc1_list[55],pc1_list[28]]
    return shift1

def Shift2(pc1_list):
    shift2 =[pc1_list[2],pc1_list[3],pc1_list[4],pc1_list[5],pc1_list[6],pc1_list[7],pc1_list[8],pc1_list[9],pc1_list[10],pc1_list[11],pc1_list[12],pc1_list[13],pc1_list[14],pc1_list[15],pc1_list[16],pc1_list[17],pc1_list[18],pc1_list[19],pc1_list[20],pc1_list[21],pc1_list[22],pc1_list[23],pc1_list[24],pc1_list[25],pc1_list[26],pc1_list[27],pc1_list[0],pc1_list[1],pc1_list[30],pc1_list[31],pc1_list[32],pc1_list[33],pc1_list[34],pc1_list[35],pc1_list[36],pc1_list[37],pc1_list[38],pc1_list[39],pc1_list[40],pc1_list[41],pc1_list[42],pc1_list[43],pc1_list[44],pc1_list[45],pc1_list[46],pc1_list[47],pc1_list[48],pc1_list[49],pc1_list[50],pc1_list[51],pc1_list[52],pc1_list[53],pc1_list[54],pc1_list[55],pc1_list[28],pc1_list[29]]
    return shift2
def PC2(key2_list):
    pc2_list = [key2_list[13],key2_list[16],key2_list[10],key2_list[23],key2_list[0],key2_list[4],key2_list[2],key2_list[27],key2_list[14],key2_list[5],key2_list[20],key2_list[9],key2_list[22],key2_list[18],key2_list[11],key2_list[3],key2_list[25],key2_list[7],key2_list[15],key2_list[6],key2_list[26],key2_list[19],key2_list[12],key2_list[1],key2_list[40],key2_list[51],key2_list[30],key2_list[36],key2_list[46],key2_list[54],key2_list[29],key2_list[39],key2_list[50],key2_list[44],key2_list[32],key2_list[47],key2_list[43],key2_list[48],key2_list[38],key2_list[55],key2_list[33],key2_list[52],key2_list[45],key2_list[41],key2_list[49],key2_list[35],key2_list[28],key2_list[31]]
    return pc2_list

key = raw_input()
KEY = bin(int(key,16))[2:].zfill(64)
key_list = list(str(KEY))
pc1_list = PC1(key_list)
PC =pc1_list
for i in range (16):
    if ( i== 0 or i==1 or i==8 or i==15):
        shift1 = Shift1(PC)
        pc2_list = PC2(shift1)
        out1 = "".join(pc2_list)
        out1 = hex(int(out1, 2))
        out1 = padhexa(out1)
        print (out1.upper())
        PC = shift1 
    else :
        shift1 = Shift2(PC)
        pc2_list = PC2(shift1)
        out3 = "".join(pc2_list)
        out3 = hex(int(out3, 2))
        out3 = padhexa(out3)
        print (out3.upper())
        PC = shift1 
    

 







