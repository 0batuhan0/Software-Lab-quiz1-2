while True:  #I use while true so that the program doesn't end after the serie is written.
    escape = input("Press q to exit (press anything to continue):\n") #I specify which key to exit the program.
    if escape =="q":
        print("Exiting the program...")
        break




    print("1)Arithmetic serie\t2)Geometric serie\t3)Febunicci serie") 
    serie = int(input("Please choose a serie from the above: "))  #I define the value I get that I use for later use.
    if serie !=1 and serie !=2 and serie !=3 :  #I use if to give error message when user doesn't enter 1,2 or 3
        print("\n!!Please enter a valid number!!")

    if serie == 1 :
        art_first = float(input("What is the first element of your serie?: "))  #I take the values needed for my serie and define it.
        constant = float(input("what is the constant difference of your series?: "))
        art_term = float(input("What is the number of terms in your serie?: "))
        arithmetic = [art_first]    #I am creating my arithmatic serie.
    
        for i in arithmetic:     #I am using a for loop to add values ​​continuously.
            arithmetic.append(art_first+constant)    #I add the new term to my serie.
            art_first=art_first+constant
            if len(arithmetic)==art_term:   #I finish the program when the number of terms value I get from the user is equal to the length of the serie.
                print(arithmetic)
                break
            
        
    if serie == 2 :
        geo_first = float(input("What is the first element of your serie?: "))  #I take the values needed for my serie and define it.
        multiplier = float(input("what is the constant multiplier of your series?: "))
        geo_term = float(input("What is the number of terms in your serie?: "))
        geometric = [geo_first]    #I am creating my geometric serie.
         
        for i in geometric:     #I am using a for loop to multiply values ​​continuously.
            geometric.append(geo_first*multiplier)    #I add the new term to my series.
            geo_first=geo_first*multiplier
            if len(geometric)==geo_term:   #I finish the program when the number of terms value I get from the user is equal to the length of the serie.
                print(geometric)
                break
        
    if serie == 3 :
        fibo_first = 1     #I give the value 1 to the first two terms of the serie.
        fibo_second = 1
        fibo_term = int(input("What is the number of terms in your serie? (must be at least 3): "))
        fibonacci = [fibo_first,fibo_second]  #I define the first two numbers that will be at the beginning of the serie.
    
        while(fibo_first<=fibo_second):      #Since I want the while loop to continue until the state I set, 
                            #I set a condition that I know will always be met.
            fibo_first,fibo_second = fibo_second,fibo_first+fibo_second   #I convert fibo_first to fibo_second and fibo_second to fibo_first+fibo_second and ensure the continuation of the serie.
            fibonacci.append(fibo_first+fibo_second)  #I add the new term to my series.
            if len(fibonacci)>=fibo_term:  #I set a condition for the series to continue as much as the value we receive from the user.
                break   #I use break to terminate the program when the condition I mentioned above provides.
        
        if fibo_term<3:        #I create a condition for the user to enter at least 3 numbers.
            print("Please enter valid number. ")
        else:
            print(fibonacci)
        



