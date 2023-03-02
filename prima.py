def bilangan_prima(n_bilangan):
    """
    Mencari bilangan prima dalam n-bilangan

    parameter:
        n_bilangan (int): banyaknya bilangan

    return:
        bil_prima (list): list bilangan prima
    """
    bil_prima = []

    for num in range(1, n_bilangan+2):
        if num > 1:
            for i in range(2, num):
                if(num%i) == 0:
                    break
            else:
                bil_prima.append(num)
    
    return bil_prima

