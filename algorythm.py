
#!/usr/bin/env python

# for the input part don't export output to an external file
# instead download BLENDER 2.7 for windows and run it in blender

#import sys

#sys.stdout = open( 'd:\\Projects BLENDER\\Project 23 Picka Python 1\\result_output.txt', 'w')


# this is a comment

def odd(x,y):
    return (x+y)%2

def domino(x,y):
    output = 0
    i = 5
    j = 0
    while (i>=0):
        output += (2**j) * odd(x[i],y[i])
        i = i-1
        j = j+1
    return output
        


node1 = 1
node2 = 1
good = 0
bad = 0
very_bad = 0

while (node2 <= 32):
    instr1 = '{0:06b}'.format(node1)
    instr2 = '{0:06b}'.format(node2)
 
    inArray1 = [0,0,0,0,0,0]
    inArray2 = [0,0,0,0,0,0]

    inArray1[0] = int(instr1[0])
    inArray1[1] = int(instr1[1])
    inArray1[2] = int(instr1[2])
    inArray1[3] = int(instr1[3])
    inArray1[4] = int(instr1[4])
    inArray1[5] = int(instr1[5])
    inArray2[0] = int(instr2[0])
    inArray2[1] = int(instr2[1])
    inArray2[2] = int(instr2[2])
    inArray2[3] = int(instr2[3])
    inArray2[4] = int(instr2[4])
    inArray2[5] = int(instr2[5])
    
    result = domino(inArray1,inArray2)
    if (node1 == node2):
        print( str(node1) + " (*?*) " + str(node2) + " = " + str(result) + "  : FAIL false"  )
        very_bad += 1
    if (result == node1) or (result == node2):
        #print( str(node1) + " (*?*) " + str(node2) + " = " + str(result) + "  : FAIL false"  )
        bad += 1
    if (node1 != node2) and (result != node1) and (result != node2):
        #print( str(node1) + " (*?*) " + str(node2) + " = " + str(result) + "  : GOOD true"  )
        good += 1
    node1 += 1
    if (node1 > 32):
        node1 = 1
        node2 += 1

print("Good = " + str(good))
print("Bad = " +  str(bad))
print("Very Bad = " + str(very_bad))
