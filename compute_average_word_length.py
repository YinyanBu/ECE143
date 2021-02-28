def compute_average_word_length(instring,unique=False):
    '''
    compute the average length of the words in the input string
    input:instring
    output:number

    '''
    assert isinstance(instring,str)
    list=instring.split()
    resultlist=[]
    for i in list:
        if unique==False:
            resultlist.append(i)
        elif unique==True:
            if i not in resultlist:
                resultlist.append(i)
    sum=0
    for j in resultlist:
        sum=sum+len(j)
    average=sum/len(resultlist)
    return average
    
