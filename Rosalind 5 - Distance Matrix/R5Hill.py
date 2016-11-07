def R5Hill(seq_1,seq_2):
    d = 0

    for i,j in zip(seq_1,seq_2):
        if i !=j:
            d += 1

    return d

    # http://stackoverflow.com/questions/1663807/how-can-i-iterate-through-two-lists-in-parallel-in-python