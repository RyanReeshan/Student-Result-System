# CW_part 01
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution. 
# Student ID : 20211192 / w1898892    
# Date : 16/04/2022

progress_count, trailer_count, retriever_count, excluded_count = 0,0,0,0     

print('\n','.' * 109,'\n')
print('\t\t\t\t\t\tWELCOME !')
print('\n','.' * 109)

def all_counts(progress_count, trailer_count, retriever_count, excluded_count):
    try:
#..........................................................................Menue...................................................................................
        academic = int(input('\nPlease Enter (1) for STUDENT LOGIN or Please Enter (2) for STAFF LOGIN : '))   
        while True:
            if academic == 1:
#.....................................................................STUDENT VERSION..............................................................................
                print('\nWelcome to the STUDENT VERSION !')   
                while True:
                    while True:
                        try:
                            credit_pass = int(input('\nPlease enter your credit at pass  : '))   
                            if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:            
                                break                                                       
                            else:
                                print('Out of range.')
                        except ValueError:       
                            print('Integer required.')

                    while True:
                        try:
                            credit_defer = int(input('Please enter your credit at defer : '))   
                            if 0 <= credit_defer <= 120 and credit_defer % 20 == 0:             
                                break
                            else:
                                print('Out of range.')
                        except ValueError:
                            print('Integer required.')

                    while True:
                        try:
                            credit_fail = int(input('Please enter your credit at fail  : '))     
                            if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:          
                                break
                            else:
                                print('Out of range.')
                        except ValueError:
                            print('Integer required.')

                    while True:
                        total_credits = credit_pass + credit_defer + credit_fail 
                        if total_credits != 120:
                            print('Total incorrect.')
                            break
                        elif credit_pass == 120:
                            print('Progress.')
                        elif credit_pass == 100:
                            print('Progress (module trailer).')
                        elif 0 <= credit_pass <= 80 and 0 <= credit_defer <= 120 and 0 <= credit_fail <= 60:
                            print('Do not progress - module retriever.')
                        else:
                            print('Exclude.')
                        import sys
                        sys.exit()

            elif academic == 2:
#.......................................................................STAFF VERSION..........................................................................
                print('\nWelcome to the STAFF VERSION with HISTOGRAM !')    
                while True:
                    while True:
                        try:
                            credit_pass = int(input('\nPlease enter your credit at pass  : '))    
                            if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:              
                                break
                            else:
                                print('Out of range.')
                        except ValueError:             
                            print('Integer required.')

                    while True:
                        try:
                            credit_defer = int(input('Please enter your credit at defer : '))
                            if 0 <= credit_defer <= 120 and credit_defer % 20 == 0:
                                break
                            else:
                                print('Out of range.')
                        except ValueError:
                            print('Integer required.')

                    while True:
                        try:
                            credit_fail = int(input('Please enter your credit at fail  : '))
                            if 0 <= credit_fail <= 120 and credit_fail % 20 == 0:
                                break
                            else:
                                print('Out of range.')
                        except ValueError:
                            print('Integer required.')

                    while True:
                        total_credits = credit_pass + credit_defer + credit_fail 
                        if total_credits != 120:
                            print('Total incorrect.')
                            break
                        elif credit_pass == 120:
                            print('Progress.')
                            progress_count += 1
                            break
                        elif credit_pass == 100:
                            print('Progress (module trailer).')
                            trailer_count += 1
                            break
                        elif 0 <= credit_pass <= 80 and 0 <= credit_defer <= 120 and 0 <= credit_fail <= 60:
                            print('Do not progress - module retriever.')
                            retriever_count += 1
                            break
                        else:
                            print('Exclude.')
                            excluded_count += 1
                            break

                    while True:
                        print('\nWould you like to enter another set of data?')         
                        answer = input("Enter 'y' for yes or 'q' to quit and view results : ")
                        answer = answer.lower()    

                        if answer == 'y':
                            break
                        elif answer == 'q':
                            print('.' * 109 )    
#....................................................................Horizontal Histogram.......................................................................                   
                            print('\nHorizontal Histogram')
                            print('\nProgress   ', progress_count, ':', '*' * progress_count)                     
                            print('Trailer    ', trailer_count, ':', '*' * trailer_count)
                            print('Retriever  ', retriever_count, ':', '*' * retriever_count)
                            print('Excluded   ', excluded_count, ':', '*' * excluded_count)
                            print('\n',progress_count + trailer_count + retriever_count + excluded_count, 'Outcomes in total.')
                            print('.' * 109 )
                            import sys
                            sys.exit()
                        else:
                            print('You Typed an Invalid Choice !')

            else:
                print('Please Follow the Correct Instructions !')
                academic = int(input('\nPlease Enter (1) for STUDENT LOGIN or Please Enter (2) for STAFF LOGIN : '))   
                
    except ValueError:                                                                                                              
        print('Please Follow the Correct Instructions !')   
        all_counts(progress_count, trailer_count, retriever_count, excluded_count)

all_counts(progress_count, trailer_count, retriever_count, excluded_count)

                        








