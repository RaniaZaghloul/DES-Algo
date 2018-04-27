plaintext_list = []
key_list = []
ciphertext_list = []
IP_list = []
pc1_list = []
shift1 = []
shift2 = []
key2_list = []
pc2_list = []
L_list =[]
R_list = []
S_Box_list1=[]
S_Box_list =[]
swapped_list = []
IIP_list = []
PC=[]
Key_list = []
def padhexa(s):
    return  s[2:].zfill(16)

def PC1(key_list):
    pc1_list = [ key_list [56] ,key_list [48] ,key_list [40] ,key_list [32] ,key_list [24] ,key_list [16] ,key_list [8] ,key_list [0] ,key_list [57] ,key_list [49] ,key_list [41] ,key_list [33] ,key_list [25] ,key_list [17] ,key_list [9] ,key_list [1] ,key_list [58] ,key_list [50] ,key_list [42] ,key_list [34] ,key_list [26] ,key_list [18] ,key_list [10] ,key_list [2] ,key_list [59] ,key_list [51] ,key_list [43] ,key_list [35] ,key_list [62] ,key_list [54] ,key_list [46] ,key_list [38] ,key_list [30] ,key_list [22] ,key_list [14] ,key_list [6] ,key_list [61] ,key_list [53] ,key_list [45] ,key_list [37] ,key_list [29] ,key_list [21] ,key_list [13] ,key_list [5] ,key_list [60] ,key_list [52] ,key_list [44] ,key_list [36] ,key_list [28] ,key_list [20] ,key_list [12] ,key_list [4] ,key_list [27] ,key_list [19],key_list [11] ,key_list [3]]
    return pc1_list

def Shift1(pc1_list):
    shift1 =[pc1_list[27],pc1_list[0],pc1_list[1],pc1_list[2],pc1_list[3],pc1_list[4],pc1_list[5],pc1_list[6],pc1_list[7],pc1_list[8],pc1_list[9],pc1_list[10],pc1_list[11],pc1_list[12],pc1_list[13],pc1_list[14],pc1_list[15],pc1_list[16],pc1_list[17],pc1_list[18],pc1_list[19],pc1_list[20],pc1_list[21],pc1_list[22],pc1_list[23],pc1_list[24],pc1_list[25],pc1_list[26],pc1_list[55],pc1_list[28],pc1_list[29],pc1_list[30],pc1_list[31],pc1_list[32],pc1_list[33],pc1_list[34],pc1_list[35],pc1_list[36],pc1_list[37],pc1_list[38],pc1_list[39],pc1_list[40],pc1_list[41],pc1_list[42],pc1_list[43],pc1_list[44],pc1_list[45],pc1_list[46],pc1_list[47],pc1_list[48],pc1_list[49],pc1_list[50],pc1_list[51],pc1_list[52],pc1_list[53],pc1_list[54]]
    return shift1

def Shift2(pc1_list):
    shift2 =[pc1_list[26],pc1_list[27],pc1_list[0],pc1_list[1],pc1_list[2],pc1_list[3],pc1_list[4],pc1_list[5],pc1_list[6],pc1_list[7],pc1_list[8],pc1_list[9],pc1_list[10],pc1_list[11],pc1_list[12],pc1_list[13],pc1_list[14],pc1_list[15],pc1_list[16],pc1_list[17],pc1_list[18],pc1_list[19],pc1_list[20],pc1_list[21],pc1_list[22],pc1_list[23],pc1_list[24],pc1_list[25],pc1_list[54],pc1_list[55],pc1_list[28],pc1_list[29],pc1_list[30],pc1_list[31],pc1_list[32],pc1_list[33],pc1_list[34],pc1_list[35],pc1_list[36],pc1_list[37],pc1_list[38],pc1_list[39],pc1_list[40],pc1_list[41],pc1_list[42],pc1_list[43],pc1_list[44],pc1_list[45],pc1_list[46],pc1_list[47],pc1_list[48],pc1_list[49],pc1_list[50],pc1_list[51],pc1_list[52],pc1_list[53]]
    return shift2
def PC2(key2_list):
    pc2_list = [key2_list[13],key2_list[16],key2_list[10],key2_list[23],key2_list[0],key2_list[4],key2_list[2],key2_list[27],key2_list[14],key2_list[5],key2_list[20],key2_list[9],key2_list[22],key2_list[18],key2_list[11],key2_list[3],key2_list[25],key2_list[7],key2_list[15],key2_list[6],key2_list[26],key2_list[19],key2_list[12],key2_list[1],key2_list[40],key2_list[51],key2_list[30],key2_list[36],key2_list[46],key2_list[54],key2_list[29],key2_list[39],key2_list[50],key2_list[44],key2_list[32],key2_list[47],key2_list[43],key2_list[48],key2_list[38],key2_list[55],key2_list[33],key2_list[52],key2_list[45],key2_list[41],key2_list[49],key2_list[35],key2_list[28],key2_list[31]]
    return pc2_list

def IP(plaintext_list):
    IP_list=[plaintext_list[57],plaintext_list[49],plaintext_list[41],plaintext_list[33],plaintext_list[25],plaintext_list[17],plaintext_list[9],plaintext_list[1],plaintext_list[59],plaintext_list[51],plaintext_list[43],plaintext_list[35],plaintext_list[27],plaintext_list[19],plaintext_list[11],plaintext_list[3],plaintext_list[61],plaintext_list[53],plaintext_list[45],plaintext_list[37],plaintext_list[29],plaintext_list[21],plaintext_list[13],plaintext_list[5],plaintext_list[63],plaintext_list[55],plaintext_list[47],plaintext_list[39],plaintext_list[31],plaintext_list[23],plaintext_list[15],plaintext_list[7],plaintext_list[56],plaintext_list[48],plaintext_list[40],plaintext_list[32],plaintext_list[24],plaintext_list[16],plaintext_list[8],plaintext_list[0],plaintext_list[58],plaintext_list[50],plaintext_list[42],plaintext_list[34],plaintext_list[26],plaintext_list[18],plaintext_list[10],plaintext_list[2],plaintext_list[60],plaintext_list[52],plaintext_list[44],plaintext_list[36],plaintext_list[28],plaintext_list[20],plaintext_list[12],plaintext_list[4],plaintext_list[62],plaintext_list[54],plaintext_list[46],plaintext_list[38],plaintext_list[30],plaintext_list[22],plaintext_list[14],plaintext_list[6]]
    return IP_list

def Exp_per(R_list):
    E_list = [R_list[31],R_list[0],R_list[1],R_list[2],R_list[3],R_list[4],R_list[3],R_list[4],R_list[5],R_list[6],R_list[7],R_list[8],R_list[7],R_list[8],R_list[9],R_list[10],R_list[11],R_list[12],R_list[11],R_list[12],R_list[13],R_list[14],R_list[15],R_list[16],R_list[15],R_list[16],R_list[17],R_list[18],R_list[19],R_list[20],R_list[19],R_list[20],R_list[21],R_list[22],R_list[23],R_list[24],R_list[23],R_list[24],R_list[25],R_list[26],R_list[27],R_list[28],R_list[27],R_list[28],R_list[29],R_list[30],R_list[31],R_list[0]]
    return E_list

def PL(S_Box_list):
    permntation_list = [ S_Box_list[15],S_Box_list[6],S_Box_list[19],S_Box_list[20],S_Box_list[28],S_Box_list[11],S_Box_list[27],S_Box_list[16],S_Box_list[0],S_Box_list[14],S_Box_list[22],S_Box_list[25],S_Box_list[4],S_Box_list[17],S_Box_list[30],S_Box_list[9],S_Box_list[1],S_Box_list[7],S_Box_list[23],S_Box_list[13],S_Box_list[31],S_Box_list[26],S_Box_list[2],S_Box_list[8],S_Box_list[18],S_Box_list[12],S_Box_list[29],S_Box_list[5],S_Box_list[21],S_Box_list[10],S_Box_list[3],S_Box_list[24]]
    return permntation_list

def DES(key_list,i):
    pc1_list = PC1(key_list)
    PC = pc1_list
    for x in range (i):
        if (x==0):
            shift1 = PC
            pc2_list = PC2(shift1)
            PC =  shift1   
        elif ( x==1 or x==8 or x==15):
            shift1 = Shift1(PC)
            pc2_list = PC2(shift1)
            PC = shift1 
        else :
            shift1 = Shift2(PC)
            pc2_list = PC2(shift1)
            PC = shift1
    Key_list = pc2_list
    return Key_list

def Spliting(IP_list):
    L_list = IP_list [:32]
    R_list = IP_list [32:]
    return L_list, R_list

def XOR (x,y):
    a= "".join(x)
    b= "".join(y)
    y= len(a)
    result = int(a,2) ^ int(b,2)
    result = ('{0:b}'.format(result)).zfill(y)
    return list(str(result))

def S_BOX (First_XOR_list):
    S1 = [['14','4','13','1','2','15','11','8','3','10','6','12','5','9','0','7'],['0','15','7','4','14','2','13','1','10','6','12','11','9','5','3','8'],['4','1','14','8','13','6','2','11','15','12','9','7','3','10','5','0'],['15','12','8','2','4','9','1','7','5','11','3','14','10','0','6','13']]
    S2 = [['15','1','8','14','6','11','3','4','9','7','2','13','12','0','5','10'],['3','13','4','7','15','2','8','14','12','0','1','10','6','9','11','5'],['0','14','7','11','10','4','13','1','5','8','12','6','9','3','2','15'],['13','8','10','1','3','15','4','2','11','6','7','12','0','5','14','9']]
    S3 = [['10','0','9','14','6','3','15','5','1','13','12','7','11','4','2','8'],['13','7','0','9','3','4','6','10','2','8','5','14','12','11','15','1'],['13','6','4','9','8','15','3','0','11','1','2','12','5','10','14','7'],['1','10','13','0','6','9','8','7','4','15','14','3','11','5','2','12']]
    S4 = [['7','13','14','3','0','6','9','10','1','2','8','5','11','12','4','15'],['13','8','11','5','6','15','0','3','4','7','2','12','1','10','14','9'],['10','6','9','0','12','11','7','13','15','1','3','14','5','2','8','4'],['3','15','0','6','10','1','13','8','9','4','5','11','12','7','2','14']]
    S5 = [['2','12','4','1','7','10','11','6','8','5','3','15','13','0','14','9'],['14','11','2','12','4','7','13','1','5','0','15','10','3','9','8','6'],['4','2','1','11','10','13','7','8','15','9','12','5','6','3','0','14'],['11','8','12','7','1','14','2','13','6','15','0','9','10','4','5','3']]
    S6 = [['12','1','10','15','9','2','6','8','0','13','3','4','14','7','5','11'],['10','15','4','2','7','12','9','5','6','1','13','14','0','11','3','8'],['9','14','15','5','2','8','12','3','7','0','4','10','1','13','11','6'],['4','3','2','12','9','5','15','10','11','14','1','7','6','0','8','13']]
    S7 = [['4','11','2','14','15','0','8','13','3','12','9','7','5','10','6','1'],['13','0','11','7','4','9','1','10','14','3','5','12','2','15','8','6'],['1','4','11','13','12','3','7','14','10','15','6','8','0','5','9','2'],['6','11','13','8','1','4','10','7','9','5','0','15','14','2','3','12']]
    S8 = [['13','2','8','4','6','15','11','1','10','9','3','14','5','0','12','7'],['1','15','13','8','10','3','7','4','12','5','6','11','0','14','9','2'],['7','11','4','1','9','12','14','2','0','6','10','13','15','3','5','8'],['2','1','14','7','4','10','8','13','15','12','9','0','3','5','6','11']] 
    L1 = First_XOR_list[:6]
    L2 = First_XOR_list[6:12]
    L3 = First_XOR_list[12:18]
    L4 = First_XOR_list[18:24]
    L5 = First_XOR_list[24:30]
    L6 = First_XOR_list[30:36]
    L7 = First_XOR_list[36:42]
    L8 = First_XOR_list[42:]
    L  = [L1,L2,L3,L4,L5,L6,L7,L8]  
    S  = [S1,S2,S3,S4,S5,S6,S7,S8]
    S_Box_list=""
    for x in range (8):
        s=S[x]
        l=L[x]
        Row    = str(l[0]) + str(l[5])
        Column = str(l[1]) + str(l[2]) + str(l[3]) + str(l[4])          
        row    = int (Row,2)  
        column = int (Column,2)           
        element = s[row][column]          
        New = str(bin(int(element))[2:].zfill(4))            
        #S_Box_list1 = list(New)           
        S_Box_list+=New     #compare    
    return S_Box_list

def Joining (L_list , Second_XOR_list):
    ciphertext_list = L_list + Second_XOR_list 
    return ciphertext_list
def IIP(swapped_list):
    IIP_list = [swapped_list[39], swapped_list[7],swapped_list[47],swapped_list[15],swapped_list[55],swapped_list[23],swapped_list[63],swapped_list[31],swapped_list[38],swapped_list[6],swapped_list[46],swapped_list[14],swapped_list[54],swapped_list[22],swapped_list[62],swapped_list[30],swapped_list[37],swapped_list[5],swapped_list[45],swapped_list[13],swapped_list[53],swapped_list[21],swapped_list[61],swapped_list[29],swapped_list[36],swapped_list[4],swapped_list[44],swapped_list[12],swapped_list[52],swapped_list[20],swapped_list[60],swapped_list[28],swapped_list[35],swapped_list[3],swapped_list[43],swapped_list[11],swapped_list[51],swapped_list[19],swapped_list[59],swapped_list[27],swapped_list[34],swapped_list[2],swapped_list[42],swapped_list[10],swapped_list[50],swapped_list[18],swapped_list[58],swapped_list[26],swapped_list[33],swapped_list[1],swapped_list[41],swapped_list[9],swapped_list[49],swapped_list[17],swapped_list[57],swapped_list[25],swapped_list[32],swapped_list[0],swapped_list[40],swapped_list[8],swapped_list[48],swapped_list[16],swapped_list[56],swapped_list[24]] 
    return IIP_list                                                                                

def Round(IP_list,Key_list):
    L_list,R_list = Spliting(IP_list)
    E_list = Exp_per(R_list)
    First_XOR_list = XOR(E_list,Key_list)   
    S_Box_list = S_BOX (First_XOR_list)
    permntation_list = PL(S_Box_list)
    Second_XOR_list = XOR (permntation_list,L_list)
    ciphertext_list = Joining (R_list , Second_XOR_list)
    return ciphertext_list
   
key = input()
plaintext = input()
looping = input()
KEY = bin(int(key,16))[2:].zfill(64)
PT = bin(int(plaintext, 16))[2:].zfill(64)
key_listo = list(str(KEY))              #compare
plaintext_list = list (str(PT))
IP_list = IP(plaintext_list)
if (int(looping) == 0 ):
    print( plaintext)
else:
    for loop in range (int(looping)):
        for i in range(16): 
            Key_list = DES(key_listo,i+1)       #compare
            ciphertext_list = Round(IP_list,Key_list)
            IP_list = ciphertext_list
        one_list,two_list = Spliting(IP_list)
        swapped_list = Joining (two_list,one_list)
        IIP_list = IIP(swapped_list)
        IP_list = IP(IIP_list)    
    ciphertext = "".join(IIP_list)    
    ciphertext = hex(int(ciphertext, 2))
    ciphertext = padhexa(ciphertext)
    print (ciphertext.upper())

