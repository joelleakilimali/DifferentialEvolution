import array
from constants import row,col,minV,maxV
from colorama import Fore, Style
from utils import *
import sys
import math

# step 1 :initialization

initialSolution = generate2DArray(row,col,minV,maxV)

# step 2 :Mutation
mutatedSolution=generate2DArray(row,col,0,0)




# with open('output2.txt', 'w') as file:
    
#     sys.stdout = file

#     print('initial solution : \n')
#     print("\n")

#     for row in initialSolution:
#         print(row)

#     print("\n")

#     print('mutated solution : \n')
#     print("\n")

#     for row in mutatedSolution:
#         print(row)
#     # print("\n")
#     # print('Mutation  : \n',)
#     # print('-' * 80 + '\n')
    
#     for i in range(col):

#        randPositionList=generateUniqueNumber(i)
      
#        print('selected columns',randPositionList[0],randPositionList[1],randPositionList[2])

 
#        vector1 = selectVector(randPositionList[0], initialSolution)
#        vector2=selectVector(randPositionList[1], initialSolution)
#        vector3=selectVector(randPositionList[2], initialSolution)
#        print("\n")
#        print( vector1 )
#        print("\n")
#        print( vector2 )
#        print("\n")
#        print( vector3 )
#        print("Vector 1:\n", vector1, "\nVector 2:\n", vector2, "\nVector 3:\n", vector3, "\n")

#        donorVectorToReplace=generateDonorVector(vector1,vector2,vector3)

#        print('donor vector at position :', i )
#        print("\n")
#        print( donorVectorToReplace )
#        mutatedSolution=assignDonorVectorToCol(mutatedSolution,donorVectorToReplace,i)

#     print('initial solution : \n',)
#     print("\n")
    
#     for row in initialSolution:
#         print(row)
#         print("\n")


#     print('mutated solution filled : \n',)
#     print("\n")
    
#     for row in mutatedSolution:
#         print(row)
#         print("\n") 

#     # step3 : Cross over 
#     print('Cross over  : \n',)
#     print('-' * 80 + '\n')
#     crossOver = crossOverComparison(initialSolution,mutatedSolution)

#     print('Cross over solution filled : \n',)
#     print("\n")

#     for row in crossOver:
#         print(row)
        
#     print('mutated solution filled : \n',)
    
#     for row in mutatedSolution:
#         print(row)
#         print("\n") 
        
#     print('initial solution : \n',)
    
#     for row in initialSolution:
#         print(row)
#         print("\n")  
#     print('Selection: \n',)
#     print('-' * 80 + '\n')
    

#     newMatrix = selection(initialSolution,crossOver)    
#     for row in newMatrix:
#         print(row)
#         print("\n")  

        
# sys.stdout = sys.__stdout__


def processSolutions(initialSolution, mutatedSolution,c2=None,f2=None):
    c22 = c2 if c2 is not None else None
    f22 = f2 if f2 is not None else None
    
 
    for i in range(col):
        randPositionList = generateUniqueNumber(i)
        
        vector1 = selectVector(randPositionList[0], initialSolution)
        vector2 = selectVector(randPositionList[1], initialSolution)
        vector3 = selectVector(randPositionList[2], initialSolution)
        
        donorVectorToReplace = generateDonorVector(vector1, vector2, vector3,Fprime=f22)
        mutatedSolution = assignDonorVectorToCol(mutatedSolution, donorVectorToReplace, i)

    # Step 3: Crossover process
    crossOver = crossOverComparison(initialSolution, mutatedSolution,CRprime=c22)

    # Step 4: Selection process

    newMatrix = selection(initialSolution, crossOver)

    return newMatrix







with open('selection2.txt', 'w') as file:
    
    sys.stdout = file
    print("differential evolution")
    tab =  [0.0,0.0,0.0,0.0,0.0]
    
    for time in range(5):
        value=0
        
        count=0
        newInitial=initialSolution
                                
        for i in range(1000):
            
            # print(" run :",i)
            # print("\n")            
                    
            selectedMatrice = processSolutions( initialSolution=newInitial,
            mutatedSolution=mutatedSolution,)  
            newInitial=selectedMatrice
                
            if(count==9):
                value=minColumnSum(selectedMatrice)
                
                count=0
            
               
            count = count + 1
        print(" zeu val:", value,time) 
        print("----------------------------------------")
        count=0
        
        tab[time]=value
    print("the tab:",tab)
    
    minimum = 0 
    average=0   
    minimum = min(tab)
    average = math.fsum(tab) / len(tab)
    print("the  min is\n:",minimum)
    print("the average is\n:",average)
    

        
                         
sys.stdout = sys.__stdout__


# with open('tab.txt', 'w') as file:

#     sys.stdout = file
#     CRPrime = [0.1,0.2, 0.3,0.4, 0.5, 0.6, 0.7,0,8]
#     FPrime = [0.4, 0.5, 0.6, 0.7,0,8, 0.9,1.0,1.1]
#     print("here the tab")
    
        


#     # Define the arrays and the function
#     cr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#     f = [4, 5, 6, 7, 8, 9, 10, 11, 12]
#     result_table = npy.empty((len(cr) + 1, len(f) + 1), dtype=object)

#     # Fill the headers
#     result_table[0, 1:] = f  # First row with f values
#     result_table[1:, 0] = cr  # First column with cr values

#     # Calculate sums for each combination and fill the table
#     initialSolution = generate2DArray(row,col,min,max)
#     mutatedSolution=generate2DArray(row,col,0,0)
#     for i, a in enumerate(cr, start=1):  # Loop over rows

#         for j, b in enumerate(f, start=1):  # Loop over columns
#             # Compute resultSol for the current combination
#             selectedMatrice = processSolutions(
#                 initialSolution=initialSolution, 
#                 mutatedSolution=mutatedSolution, 
#                 f2=b,  # Use `b` for the current value from `f`
#                 c2=a   # Use `a` for the current value from `cr`
#             )
#             resultSol = minColumnSum(selectedMatrice)
#             print('--------------->  ',i,j,)
#             print('f,c,min \n',b,a,resultSol)
#             initialSolution = generate2DArray(row,col,min,max)
#             mutatedSolution=generate2DArray(row,col,0,0)            
#             # Store the resultSol in the correct cell
#             result_table[i, j] = resultSol

# # Print the table
#     print("Result Table:")
#     for row in result_table:
#         print("\t".join(map(str,row)))
        
# sys.stdout = sys.__stdout__