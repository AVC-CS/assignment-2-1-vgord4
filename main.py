def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    
    total = 100

    num_male = int(input('How many males are in your class? '))
    num_female = int(input('How many females are in your class? '))

    m_perc = (num_male/total) * 100
    f_perc = (num_female/total) * 100
    

    print (f'Total number of students: {total}')
    print (f'Number of Male to Female students: {num_male}, {num_female}')
    print (f'Male and female percentage: {m_perc:.2f}% {f_perc:.2f}%')


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
