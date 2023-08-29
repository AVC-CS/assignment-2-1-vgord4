def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    total = int(input("How many students are in your class? "))

    num_m = int(input('How many males are in your class? '))
    num_f = int(input('How many females are in your class? '))

    m_perc = (num_m/total) * 100
    f_perc = (num_f/total) * 100
    

    print (f'Total number of students: {total}')
    print (f'Number of Male to Female students: {num_m},  {num_f}')
    print (f'Male percentage: {m_perc:.2f} % ')
    print (f'Female percentage: {f_perc:.2f} % ')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc



if __name__ == '__main__':
    main()
