# CW_part 04
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution. 
# Student ID : 20211192 / w1898892    
# Date : 16/04/2022

progress_count, trailer_count, retriever_count, excluded_count = 0,0,0,0     

print('\n','.' * 109,'\n')
print('\t\t\t\t\t\tWELCOME !')
print('\n','.' * 109)

empty_list = []
#...........................................................................STAFF VERSION........................................................................
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
            tempstring = "Progress         - {}, {}, {}\n".format(credit_pass,credit_defer,credit_fail)
            empty_list.append(tempstring)
            break
        elif credit_pass == 100:
            print('Progress (module trailer).')
            trailer_count += 1
            tempstring = "Module trailer   - {}, {}, {}\n".format(credit_pass,credit_defer,credit_fail)
            empty_list.append(tempstring)
            break
        elif 0 <= credit_pass <= 80 and 0 <= credit_defer <= 120 and 0 <= credit_fail <= 60:
            print('Do not progress (module retriever).')
            retriever_count += 1
            tempstring = "Module retriever - {}, {}, {}\n".format(credit_pass,credit_defer,credit_fail)
            empty_list.append(tempstring)
            break
        else:
            print('Exclude.')
            excluded_count += 1
            tempstring = "Exclude          - {}, {}, {}\n".format(credit_pass,credit_defer,credit_fail)
            empty_list.append(tempstring)
            break

    while True:
        print('\nWould you like to enter another set of data?')        
        answer = input("Enter 'y' for yes or 'q' to quit and view results : ")
        answer = answer.lower()    

        if answer == 'y':
            break
        elif answer == 'q':
            print('.' * 109 ) 
#................................................................Horizontal Histogram............................................................................                                
            print('\nHorizontal Histogram')     
            print('\nProgress   ', progress_count, ':' , '*' * progress_count)                     
            print('Trailer    ', trailer_count, ':' , '*' * trailer_count)
            print('Retriever  ', retriever_count, ':' , '*' * retriever_count)
            print('Excluded   ', excluded_count, ':' , '*' * excluded_count)
            print('\n',progress_count + trailer_count + retriever_count + excluded_count, 'Outcomes in total.')
            print('.' * 109 )
#...............................................................Vertical Histogram................................................................................
            print('\nVertical Histogram') 
            print('\nProgress {}| Trailing {}| Retriever {}| Exclude {}'.format(progress_count,trailer_count,retriever_count,excluded_count))

            for i in range(max(progress_count,trailer_count,retriever_count,excluded_count)):

                print( "     {0}          {1}          {2}           {3} ".format(

                    '*' if i < progress_count else ' ',
                    '*' if i < trailer_count else ' ',
                    '*' if i < retriever_count else ' ',
                    '*' if i < excluded_count else ' '))
                    
            print('\n',progress_count + trailer_count + retriever_count + excluded_count, 'Outcomes in total.')
            print('-'*109)
#......................................................................Lists.......................................................................................
            for i in (empty_list):
                print('\n',i)
                
            print('-' * 109)
#......................................................................file........................................................................................
            data_file = open('my.txt','w')    
            for i in (empty_list):
                data_file.write(i)
            data_file.close()
            print('\t')

            data_file = open('my.txt','r')
            print(data_file.read())
            data_file.close()
            print('-' * 109)
            import sys
            sys.exit()
        else:
            print('You Typed an Invalid Choice !')
