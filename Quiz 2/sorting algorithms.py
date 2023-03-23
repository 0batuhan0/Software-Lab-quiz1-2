import random
import heapq as hq
import time

while True:  #I use while true so that the program doesn't end after the arrey is written.
    escape = input("Press q to exit (press anything to continue):\n") #I specify which key to exit the program.
    if escape =="q":
        print("Exiting the program...")
        break


    class timer:
        def start(self):
            self.begin = time.perf_counter()   #I define the start of the timer and count the program.
    
        def finish(self):
            self.end = time.perf_counter()     #I define the end of the timer and finish counting
            dif = (self.end-self.begin)*1000
            print(f"\n{dif} completed in ms.")
    timer = timer()




    arrey = list() 
    terms = int(input("What is the number of terms in your arrey?: ")) #I get how many terms the arrey will have from the user.
    print("\n1)Buble sort\t2)Heap sort\t\t    3)Selection sort  4)Quick sort\t5)Insertion sort\t6)Shell sort ")
    sorting = int(input("Which sorting algorithm will you use?: ")) #We get from the user which algorithm to use for the array.
    i = 0
    while (i<15):
        arrey.append(random.uniform(1,100000)) #we added a random number between 1 and 1000 to our array.
        if(len(arrey)==terms):  #When the number entered by the user was equal to the length of the arrey, our list was created and we would end the program.
            break
    
    

 
    if sorting == 1 :
        timer.start()   #I starting the timer.
        def bubleSort(nums):
      
          for i in range(0,len(nums)):        #We used this for loop to compare all the numbers in our array.
              for j in range(0,len(nums)-1):  #Here, we have included other numbers in the loop except the selected number above.
                 if nums[j] > nums[j+1] :    #Here, the selected number and the number to its right are compared and 
                                             #if the number we choose is larger, it is replaced.
                   nums[j],nums[j+1]=nums[j+1],nums[j]
                 else:
                   continue
          print(nums)
        bubleSort(arrey)
        timer.finish()   #I'm finishing the timer

 


    if sorting == 2 :
        timer.start()   #I starting the timer.
        hq.heapify(arrey)   #This function creates a stack and that's how sorting is performed.
        s_result = [hq.heappop(arrey) for i in range(len(arrey))]
        print(s_result)
        timer.finish()  #I'm finishing the timer




    if sorting == 3 :
        timer.start()  #I starting the timer.
        def selection(Vektor):
            for i in range(len(Vektor)-1): #A number is selected from the array.
                enk = Vektor[i]
                enk_indis = i
                for j in range(i+1, len(Vektor)): #Other numbers in the array are also read with this loop.
                    if Vektor[j] < enk:
                        enk = Vektor[j]           #These values, which are read afterwards, are compared with the number i.
                        enk_indis = j             
                store = Vektor[i]                  #It continues until the smallest number is found, and when the smallest number is found, it comes at the beginning of the arrey.
                Vektor[i] = Vektor[enk_indis]
                Vektor[enk_indis] = store          #After that, the second smallest number is found and comes to the second term of the arrey. It goes on like this.
            print(Vektor)
    
        selection(arrey)
        timer.finish()    #I'm finishing the timer
    
    
    
    
    if sorting == 4 :
        timer.start()  #I starting the timer.
        def smash(arrey,leftIndex,rightIndex):
            i = leftIndex - 1
            pivot = arrey[rightIndex]  #The right index of the array is chosen as the pivot.
            
            for j in range(leftIndex,rightIndex):
                if arrey[j] <= pivot : #If the element in j is less than and equal to the pivot
                    i=i+1              #i is increses by 1.
                    arrey[i],arrey[j] = arrey[j],arrey[i]  #Replaces elements in i and j.
            arrey[i+1],arrey[rightIndex] = arrey[rightIndex],arrey[i+1]   #The new value of the pivot is the element in i+1.
            return i+1
        
        def quickSort(arrey,leftIndex,rightIndex):
            if leftIndex < rightIndex:                #Continues as long as leftIndex is less than rightIndex.
                pivot = smash(arrey, leftIndex, rightIndex)
                quickSort(arrey, leftIndex, pivot -1)    #We select the element to the left of the pivot
                quickSort(arrey, pivot+1, rightIndex)    #We select the element to the right of the pivot
                
        quickSort(arrey,0,len(arrey)-1)    #It takes our array as a parameter.
        print(arrey)
        timer.finish()    #I'm finishing the timer    




    if sorting == 5 :
        timer.start()  #I starting the timer.
        def insertionSort(arrey):
            for i in range(1,len(arrey)):   #The loop starts at 1 and continues for the length of the array.
                key = arrey[i]       #One key is selected.
                j = i - 1           #The element to the left of it is defined.
                
                while j >= 0 and key < arrey[j]:  #j must not be negative and key must be less than array value.
                    arrey[j+1] = arrey[j]          #Scrolling here.
                    j = j-1
                arrey[j+1] = key                  #Our new key will be j+1.
        
        insertionSort(arrey)
        print(arrey)
        timer.finish()    #I'm finishing the timer  
    
    
    
    
    if sorting == 6 :
        timer.start()  #I starting the timer.
        def shellSort(array, n):
    
            gap = n // 2            #We decide that we will create a column with how many numbers with this gap value.
            while gap > 0:
                for i in range(gap, n):      #These columns are sorted among themselves.
                    temp = array[i]          
                    j = i                    #Then these columns are converted back to array
                    while j >= gap and array[j - gap] > temp:   
                        array[j] = array[j - gap]               #Afterwards, this process is repeated with values ​​consisting of 1 column.
                        j -= gap
                                                                #At the end, our array again get formed and sorted.
                    array[j] = temp
                gap //= 2
        
        
        size = len(arrey)
        shellSort(arrey, size)
        print(arrey)
        timer.finish()    #I'm finishing the timer      

