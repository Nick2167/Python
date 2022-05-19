def tryagain(): #this function will redirect the user to the beginning of the main function in case of any error
    input('\nInvalid input. Press ENTER to restart the program.\n\n')
    main()

def yardservice(): #this function is the yard service pricing options
    #request user input
        service_choice = input('Which service would you like?\nPlease input mowing, edging, OR pruning (case sensitive).\n')
        if service_choice == 'mowing':
            smowing = 300 #setting the pricing for small, medium, and large 
            mmowing = 1000
            lmowing = 3000
            print('Mowing Service Pricing\nSmall Yard (10,000 square feet and below) = $300\nMedium Yard Pricing (10,001 - 39,999 square feet) = $1,000\nLarge Yard Pricing (40,000 square feet and above) = $3,000\n')
            yard_size = eval(input('Enter yard square footage: \n'))
            if yard_size >= 43000: #large yard 1 acre+:
                total = lmowing
                print('Your total service cost is: ', total, 'dollars.')
                age = eval(input('Seniors Save 10%! Please input your age: '))
                if age >= 65:
                    print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                else:
                    print('You do not qualify for the senior discount.')
            else:
                if yard_size <= 39999 and yard_size >=10001: #setting the parameters of what is small, medium, or large
                    total = mmowing
                    print('Your total service cost is: ', total, 'dollars.')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')
                else:
                    if yard_size <= 10000:
                        total = smowing
                        print('Your total service cost is: ', total, 'dollars.')
                        age = eval(input('Seniors Save 10%! Please input your age: ')) #senior discount requests age of user, if 65 and older, the discount is applied and a new total is presented to the user
                        if age >= 65:
                            print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                        else:
                            print('You do not qualify for the senior discount.') #if user does not qualify, the program will proceed as normal
                    else:
                        tryagain()
        else:
            if service_choice == 'edging':
                sedging = 150
                medging = 500
                ledging = 1000
                print('Edging Service Pricing\nSmall Edges (149 linear feet and below) = $150\nMedium Edges (150-250 linear feet) = $500\nLarge Edges (251 linear feet and above) = $1000\n')
                edge_size = eval(input('Enter the linear footage of the yard edges: \n'))
                if edge_size > 250:
                    total = ledging
                    print('Your total service cost is: ', total, 'dollars.')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')                      
                else:
                    if edge_size <= 250 and edge_size >= 150:
                        total = medging
                        print('Your total service cost is: ', total, 'dollars.')
                        age = eval(input('Seniors Save 10%! Please input your age: '))
                        if age >= 65:
                            print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                        else:
                            print('You do not qualify for the senior discount.')                        
                    else:
                        if edge_size < 150:
                            total = sedging
                            print('Your total service cost is: ', total, 'dollars.')
                            age = eval(input('Seniors Save 10%! Please input your age: '))
                            if age >= 65:
                                print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                            else:
                                print('You do not qualify for the senior discount.')
                        else:
                            tryagain()               
                    
            else:
                spruning = 200
                mpruning = 500
                lpruning = 700
                print('Shrub Pruning Service Pricing\nSmall amount (5 and below) = $200\nMedium Amount (6-10) = $500\nLarge Amount (11+) = $700')
                shrub_amount = eval(input('Enter the amount of shrubs: \n'))
                if shrub_amount > 10: 
                    total = lpruning
                    print('Your total service cost is: ', total, 'dollars.\n')
                    print('That is ', total / shrub_amount , ' dollars per shrub.')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        ntotal = total * .9
                        print('You qualify for the senior discount!\nYour new total is: ', ntotal, ' dollars.\n')
                        print('That is ', ntotal/shrub_amount , ' dollars per shrub.')
                    else:
                        print('You do not qualify for the senior discount.')                     
                else:
                    if shrub_amount <= 10 and shrub_amount >= 6:
                        total = mpruning
                        print('Your total service cost is: ', total, 'dollars.\n')
                        print('That is ', total / shrub_amount , ' dollars per shrub.')
                        age = eval(input('Seniors Save 10%! Please input your age: '))
                        if age >= 65:
                            ntotal = total * .9
                            print('You qualify for the senior discount!\nYour new total is: ', ntotal, ' dollars.\n')
                            print('That is ', ntotal/shrub_amount , ' dollars per shrub.')
                        else:
                            print('You do not qualify for the senior discount.')                          
                    else:
                        if shrub_amount <= 5:
                            total = spruning
                            print('Your total service cost is: ', total, 'dollars.\n')
                            print('That is ', total / shrub_amount , ' dollars per shrub.')
                            age = eval(input('Seniors Save 10%! Please input your age: '))
                            if age >= 65:
                                ntotal = total * .9
                                print('You qualify for the senior discount!\nYour new total is: ', ntotal, ' dollars.\n')
                                print('That is ', ntotal/shrub_amount , ' dollars per shrub.')
                            else:
                                print('You do not qualify for the senior discount.')
                        else:
                            tryagain() 
        return total

def housecleaning(): #this function is for regular cleaning pricing options
    #request user input

    rooms = eval(input('Enter total rooms in house: '))

    # establishing conditions to determine what pricing to display

    if rooms >= 6: #large houses 6+ rooms
        floors_cost = 200 #dollars 

        bathrooms_cost = 250

        windows_cost = 175
        
        #using user input to print correct pricing data
        
        print('Large House Pricing\nFloors = $200 per room\nBathrooms = $250 per room\nWindows = $175 per room\n')
        
        cleaning_choice = input('What would you like cleaned?\nPlease input floors, bathrooms, OR windows (case sensitive).\n')
        if cleaning_choice == 'floors':
                total = floors_cost * rooms
                print('Your total cleaning cost would be $', total,'\n')
                age = eval(input('Seniors Save 10%! Please input your age: '))
                if age >= 65:
                    print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                else:
                    print('You do not qualify for the senior discount.')
        else:
            if cleaning_choice == 'bathrooms':
                brooms = eval(input('How many bathrooms do you have?'))
                total = bathrooms_cost * brooms
                print('Your total cleaning cost would be $', total, '\n')
                age = eval(input('Seniors Save 10%! Please input your age: '))
                if age >= 65:
                    print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                else:
                    print('You do not qualify for the senior discount.')
            else:
                total = windows_cost * rooms
                print('Your total cleaning cost would be $',total,'\n')
                age = eval(input('Seniors Save 10%! Please input your age: '))
                if age >= 65:
                    print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                else:
                    print('You do not qualify for the senior discount.')
    else:
        if rooms >= 4: #medium houses 4-5 rooms
            
            floors_cost = 150 

            bathrooms_cost = 200

            windows_cost = 125
            
            print('Medium House Pricing\nFloors = $150 per room\nBathrooms = $200 per room\nWindows = $125 per room\n')
            cleaning_choice = input('What would you like cleaned?\nPlease input floors, bathrooms, OR windows (case sensitive).\n')
            if cleaning_choice == 'floors':
                    total = floors_cost * rooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')
            else:
                if cleaning_choice == 'bathrooms':
                    brooms = eval(input('How many bathrooms do you have?'))
                    total = bathrooms_cost * brooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')
                else:
                    total = windows_cost * rooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')
                
            
            
        else: #small houses 1-3 rooms 
                floors_cost = 100 

                bathrooms_cost = 150

                windows_cost = 75
                
                print('Small House Pricing\nFloors = $100 per room\nBathrooms = $150 per room\nWindows = $75 per room\n')
                cleaning_choice = input('What would you like cleaned?\nPlease input floors, bathrooms, OR windows (case sensitive).\n')
                if cleaning_choice == 'floors':
                    total = floors_cost * rooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')                             
                else:
                    if cleaning_choice == 'bathrooms':                        
                        brooms = eval(input('How many bathrooms do you have?'))
                        total = bathrooms_cost * brooms
                        print('Your total cleaning cost would be $', total)
                        age = eval(input('Seniors Save 10%! Please input your age: '))
                        if age >= 65:
                            print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                        else:
                            print('You do not qualify for the senior discount.')                        
                    else:
                        total = windows_cost * rooms
                        print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')



def premium_costs(): #this function is for the premium cleaning pricing options
    #request user input

    rooms = eval(input('There will be an additional $100 surcharge for premium cleaning.\nEnter total rooms in house: '))

    # establishing conditions to determine what pricing to display

    if rooms >= 6: #large houses 6+ rooms
        floors_cost = 300 #dollars 

        bathrooms_cost = 350

        windows_cost = 275
        
        #using user input to print correct pricing data
        
        print('Large House Pricing\nFloors = $300 per room\nBathrooms = $350 per room\nWindows = $275 per room\n')
        
        cleaning_choice = input('What would you like cleaned?\nPlease input floors, bathrooms, OR windows (case sensitive).\n')
        if cleaning_choice == 'floors':
                total = floors_cost * rooms
                print('Your total cleaning cost would be $', total,'\n')
                age = eval(input('Seniors Save 10%! Please input your age: '))
                if age >= 65:
                    print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                else:
                    print('You do not qualify for the senior discount.')
        else:
            if cleaning_choice == 'bathrooms':
                brooms = eval(input('How many bathrooms do you have?'))
                total = bathrooms_cost * brooms
                print('Your total cleaning cost would be $', total, '\n')
                age = eval(input('Seniors Save 10%! Please input your age: '))
                if age >= 65:
                    print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                else:
                    print('You do not qualify for the senior discount.')
            else:
                total = windows_cost * rooms
                print('Your total cleaning cost would be $',total,'\n')
                age = eval(input('Seniors Save 10%! Please input your age: '))
                if age >= 65:
                    print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                else:
                    print('You do not qualify for the senior discount.')
    else:
        if rooms >= 4: #medium houses 4-5 rooms
            
            floors_cost = 250 

            bathrooms_cost = 300

            windows_cost = 225
            
            print('Medium House Pricing\nFloors = $250 per room\nBathrooms = $300 per room\nWindows = $225 per room\n')
            cleaning_choice = input('What would you like cleaned?\nPlease input floors, bathrooms, OR windows (case sensitive).\n')
            if cleaning_choice == 'floors':
                    total = floors_cost * rooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')
            else:
                if cleaning_choice == 'bathrooms':
                    brooms = eval(input('How many bathrooms do you have?'))
                    total = bathrooms_cost * brooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')
                else:
                    total = windows_cost * rooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')
                
            
            
        else: #small houses 1-3 rooms 
                floors_cost = 200 

                bathrooms_cost = 250

                windows_cost = 175
                
                print('Small House Pricing\nFloors = $200 per room\nBathrooms = $250 per room\nWindows = $175 per room\n')
                cleaning_choice = input('What would you like cleaned?\nPlease input floors, bathrooms, OR windows (case sensitive).\n')
                if cleaning_choice == 'floors':
                    total = floors_cost * rooms
                    print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')                             
                else:
                    if cleaning_choice == 'bathrooms':                        
                        brooms = eval(input('How many bathrooms do you have?'))
                        total = bathrooms_cost * brooms
                        print('Your total cleaning cost would be $', total)
                        age = eval(input('Seniors Save 10%! Please input your age: '))
                        if age >= 65:
                            print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                        else:
                            print('You do not qualify for the senior discount.')                        
                    else:
                        total = windows_cost * rooms
                        print('Your total cleaning cost would be $', total,'\n')
                    age = eval(input('Seniors Save 10%! Please input your age: '))
                    if age >= 65:
                        print('You qualify for the senior discount!\nYour new total is: ', total * .9, ' dollars.')
                    else:
                        print('You do not qualify for the senior discount.')


def main(): #this is the main function that will be calling all other functions
    print('Welcome to the House Cleaning and Yard Service Cost Program') #title
    choice = input('House Cleaning (H) or Yard Service (Y)? (Case sensitive)') #user input to determine which functions to call
    if choice == 'H':
        cleantype = input('Deep Premium Clean (P) or Regular Clean (R)? (case sensitive)')
        if cleantype == 'R':
            housecleaning() #call this function if user inputs 'R'
        else:
            if cleantype == 'P':
                premium_costs() #call this function if user unputs 'P'
            else:
                tryagain() #if criteria is not met, users will be looped to the beginning of the program
    else:
        if choice == 'Y':
            yardservice() #call this function if user inputs 'Y'
        else:
            tryagain()


main() #main function to start the program

#thank user, terminate program
            
print('\nThank you for testing my program!\nNicholas Kalargyros\n')

input('Press ENTER to close')

