import random
from constants import col,F,CR,row
import numpy as npy

def generate2DArray(rows,cols,min,max):
  return [[round(random.uniform(min, max), 2) for _ in range(cols)] for _ in range(rows)]

def generateUniqueNumber(excludedNumber):

  # print('excluded position:',excludedNumber)
  uniqueRandomList = set()

  while len(uniqueRandomList)<3:
    rand_num = random.randint(0, col-1)
    if rand_num !=excludedNumber:
      uniqueRandomList.add(rand_num)
  return list(uniqueRandomList)

def selectVector(columnIndex,initialSolution):
  vectorSelected= [row[columnIndex] for row in initialSolution]
  vectorSelected = npy.array(vectorSelected)
  vectorSelected = vectorSelected.reshape(-1, 1)
  return vectorSelected

def generateDonorVector(vec1,vec2,vec3):
  donorVector = vec1 + F * (vec2-vec3)
  donorVector=donorVector.reshape(-1,1)
  return donorVector

def assignDonorVectorToCol( matrix,vector,index):
  matrix = npy.array(matrix)
  matrix[:, index] = vector.flatten()
  return matrix



def crossOverComparison(matrix1, matrix2):
    matrix1 = npy.array(matrix1)
    matrix2 = npy.array(matrix2)
    row, col = matrix1.shape  
    crossOverGenMatrix = npy.zeros_like(matrix1)  

    for i in range(col):
        initialCol = selectVector(i, matrix1)
        mutatedCol = selectVector(i, matrix2) 
        
        randomNumber = [round(random.uniform(0, 1), 2) for _ in range(row)]  

        # print(f"\nThis is the random number to compare with the CR at column {i}:\n{randomNumber}")

        newCrossOverCol = npy.zeros((row, 1))

        for j in range(row):
            # print(" rand number of comp  with 0.6:",randomNumber[j])
            if randomNumber[j] > CR:
                newCrossOverCol[j] = mutatedCol[j]
            else:
                newCrossOverCol[j] = initialCol[j]

        # print(f"\nVector after comparison at column {i}:\n{newCrossOverCol}")

        crossOverGenMatrix = assignDonorVectorToCol(crossOverGenMatrix, newCrossOverCol, i) 

    return crossOverGenMatrix  
  



def selection(matrix1, matrix2):
    
   
    matrix1 = npy.array(matrix1)
    newInitialSolution = npy.zeros_like(matrix1)

    for column in range(matrix1.shape[1]):
        sum_squares_matrix1 = npy.sum(matrix1[:, column] ** 2)
        sum_squares_matrix2 = npy.sum(matrix2[:, column] ** 2)
        
        # Select the column with the smaller sum of squares and assign it to newInitialSolution
        if sum_squares_matrix1 <= sum_squares_matrix2:
            newInitialSolution[:, column] = matrix1[:, column]
        else:
            newInitialSolution[:, column] = matrix2[:, column]
    
    return newInitialSolution





def minColumnSum(matrix):
    column_sums = npy.sum(matrix ** 2, axis=0)
    
    min_index = npy.argmin(column_sums)
    
    
    minSumVal = column_sums[min_index]
    
    print(f"The column with the minimum sum of squares is column {min_index} with a sum of {minSumVal}")
    return min_index, minSumVal
    
