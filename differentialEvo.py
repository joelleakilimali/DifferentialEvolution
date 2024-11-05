import sys
from constants import row,col,min,max
from utils import *

# step 1 :initialization

initialSolution = generate2DArray(row,col,min,max)

# step 2 :Mutation
mutatedSolution=generate2DArray(row,col,0,0)



with open('output.txt', 'w') as file:
    
    sys.stdout = file

    print('initial solution : \n')
    print("\n")

    for row in initialSolution:
        print(row)

    print("\n")

    print('mutated solution : \n')
    print("\n")

    for row in mutatedSolution:
        print(row)
    print("\n")
    print('Mutation  : \n',)
    print('-' * 80 + '\n')
    
    for i in range(col):

       randPositionList=generateUniqueNumber(i)
      
       print('selected columns',randPositionList[0],randPositionList[1],randPositionList[2])

 
       vector1 = selectVector(randPositionList[0], initialSolution)
       vector2=selectVector(randPositionList[1], initialSolution)
       vector3=selectVector(randPositionList[2], initialSolution)
       print("\n")
    #    print( vector1 )
    #    print("\n")
    #    print( vector2 )
    #    print("\n")
    #    print( vector3 )
       print("Vector 1:\n", vector1, "\nVector 2:\n", vector2, "\nVector 3:\n", vector3, "\n")

       donorVectorToReplace=generateDonorVector(vector1,vector2,vector3)

       print('donor vector at position :', i )
       print("\n")
       print( donorVectorToReplace )
       mutatedSolution=assignDonorVectorToCol(mutatedSolution,donorVectorToReplace,i)

    print('initial solution : \n',)
    print("\n")
    
    for row in initialSolution:
        print(row)
        print("\n")


    print('mutated solution filled : \n',)
    print("\n")
    
    for row in mutatedSolution:
        print(row)
        print("\n") 

    #step3 : Cross over 
    print('Cross over  : \n',)
    print('-' * 80 + '\n')
    crossOver = crossOverComparison(initialSolution,mutatedSolution)

    print('Cross over solution filled : \n',)
    print("\n")

    for row in crossOver:
        print(row)
        
    print('mutated solution filled : \n',)
    
    for row in mutatedSolution:
        print(row)
        print("\n") 
        
    print('initial solution : \n',)
    
    for row in initialSolution:
        print(row)
        print("\n")  
    print('Selection: \n',)
    print('-' * 80 + '\n')
    

    newMatrix = selection(initialSolution,crossOver)    
    for row in newMatrix:
        print(row)
        print("\n")  

        
sys.stdout = sys.__stdout__


