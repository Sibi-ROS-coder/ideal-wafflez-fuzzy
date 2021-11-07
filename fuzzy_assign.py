import numpy as np

import math
import csv
districts = np.array([[0.1,0.0,0.2,0.8,0.3,0.0,0.5,0.6,0.0,0.1,0.3,0.1,0.2,0.2,0.1,0.2],

                      [0.7,0.5,0.2,0.1,0.0,0.4,0.0,0.3,0.5,0.6,0.2,0.5,0.0,0.6,0.7,0.4],

                      [0.2,0.5,0.2,0.0,0.4,0.0,0.4,0.0,0.1,0.0,0.1,0.4,0.2,0.1,0.1,0.2],

                      [0.0,0.0,0.4,0.1,0.3,0.6,0.1,0.1,0.4,0.3,0.4,0.0,0.6,0.1,0.1,0.2]])

print("Districts",districts.shape)

R = np.zeros([districts.shape[1],districts.shape[1]])

print("R",R.shape)

# int(i);

i = 0 

j  = 0

numerator = 0.0

denominator_1 = 0.0

denominator_2 = 0.0

for i in range(districts.shape[1]):

    for j in range(districts.shape[1]): 

        numerator = abs((districts[0][i] * districts[0][j])+(districts[1][i] * districts[1][j])+(districts[2][i] * districts[2][j])+(districts[3][i] * districts[3][j]) )

        denominator_1 = ((districts[0][i]*districts[0][i])+(districts[1][i]*districts[1][i])+(districts[2][i]*districts[2][i])+(districts[3][i]*districts[3][i]))

        denominator_2 = ((districts[0][j]*districts[0][j])+(districts[1][j]*districts[1][j])+(districts[2][j]*districts[2][j])+(districts[3][j]*districts[3][j]))

        R[i][j] = numerator/math.sqrt((denominator_1*denominator_2))

        numerator = 0.0

        denominator_1 = 0.0

        denominator_2 = 0.0
np.savetxt('R.txt', R)

print("first",R[0])

print("first",R[:][0])



k = 0

for k in range(districts.shape[1]):

    print(R[k][k])

i = 0 

j  = 0

R_1 = np.zeros([districts.shape[1],districts.shape[1]])

# for i in range(districts.shape[1]):

#     for j in range(districts.shape[1]):

#         R_1[i][j] = 

import skfuzzy

# R_1 = skfuzzy.fuzzymath.maxmin_composition(R, R)



a = True

R_tmp = R

count = 0

while(a==True):

    count +=1

    R_tmp = skfuzzy.fuzzymath.maxmin_composition(R_tmp,R_tmp)

    i = 0 

    j = 0

    ac = 0

    for i in range(districts.shape[1]):

        for j in range(districts.shape[1]):

            if(R_tmp[i][j] == R[i][j]):

                ac +=1

                # print("True")

            else:

                ac +=0



    R = R_tmp

    if(ac == 256):

        a = False

        break

print("Count",count)

R_0_4 = np.zeros([districts.shape[1],districts.shape[1]],np.float32)

R_0_8 = np.zeros([districts.shape[1],districts.shape[1]],np.float32)

R_0_85 = np.zeros([districts.shape[1],districts.shape[1]],np.float32)



R_0_4[R_tmp >= 0.4] = 1



R_0_8[R_tmp >= 0.8] = 1

R_0_85[R_tmp >= 0.85] = 1

print("R_tmp",R_tmp)

import cv2

# print("")

# R_0_8.show()



# scale_percent = 10000 # percent of original size

# width = int(R_0_4.shape[1] * scale_percent / 100)

# height = int(R_0_4.shape[0] * scale_percent / 100)

# dim = (width, height)

  

# # resize image

# resized_04 = cv2.resize(R_0_4, dim, interpolation = cv2.INTER_AREA)

# resized_08 = cv2.resize(R_0_8, dim, interpolation = cv2.INTER_AREA)

# resized_085 = cv2.resize(R_0_85, dim, interpolation = cv2.INTER_AREA)





# cv2.imwrite("r_0_4.png",resized_04)

# cv2.imwrite("R_0_8.png",resized_08)

# cv2.imwrite("R_0_85.png",resized_085)



# cv2.imshow("r_0_4.png",R_0_4)

# cv2.imshow("R_0_8.png",R_0_8)

# cv2.imshow("R_0_9",R_0_9)

# cv2.waitKey(0)

# print("R_0_8")

# print(R_0_8)e("r_0_4.png",R_0_4)

# cv2.imwrite

# //To check given Matrix is Symmetric or Not

def Symmetric(a, n):

    for i in range(n):

        for j in range(n):

            if (a[i][j] != a[j][i]):

                return False

    return True


# print("Given matrix: ")

# print(a)

if (Symmetric(R_0_8, 16)):

    print ("Given matrix is symmetric")

else:

    print ("Given matrix is not a symmetrics")
print(R)
# np.savetxt('R.txt', R)
np.savetxt('R_tmp.txt', R_tmp)
np.savetxt('R_0_4.txt', R_0_4)
np.savetxt('R_0_8.txt', R_0_8)
np.savetxt('R_0_85.txt', R_0_85)
