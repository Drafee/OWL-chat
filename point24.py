choice1 = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
choice2 = ((0,1),(0,2),(1,2))
choice3 = ((0,1))

def operatechoice():
    n = [0,1,2,3]
    out = []
    for i in range(4):
        outcome1 = []
        outcome1.append(n[i])
        for j in range(4):
            outcome2 = outcome1[:]
            outcome2.append(n[j])
            for k in range(4):
                outcome3 = outcome2[:]
                outcome3.append(n[k])
                out.append(outcome3)
    return out
   

def operate(a,b,i):
    if i == 0:
        outcome = a + b
    elif i == 1:
        outcome = abs(a - b)
    elif i == 2:
        outcome = a * b
    elif i == 3:
        if a*b != 0:
            outcome = max(a/b,b/a)
        else:
            outcome = 0

    return outcome

def intermediate_steps(a,b,i,li,li0):
    if i == 0:
        step = "("+str(a)+ "+"+ str(b)+")"
    elif i == 1:
        if li[li0.index(a)] > li[li0.index(b)]:
            step = "("+str(a)+ "-"+ str(b)+")"
        else:
            step = "("+str(b)+ "-"+ str(a)+")"
    elif i == 2:
        step = "("+str(a)+ "*"+ str(b)+")"
    elif i == 3:
        if li[li0.index(a)] > li[li0.index(b)]:
            step = "("+str(a)+ "/"+ str(b)+")"
        else:
            step = "("+str(b)+ "*"+ str(a)+")"
    return step

def last(li,choice,c1,c2):
    li0 = li[:]

    a = li[c1[0]]
    b = li[c1[1]]
    x = li0[c1[0]]
    y = li0[c1[1]]
    li.append(operate(a,b,choice[0]))
    li0.append(intermediate_steps(x,y,choice[0],li,li0))
    li.remove(a)
    li.remove(b)
    li0.remove(x)
    li0.remove(y)

    a = li[c2[0]]
    b = li[c2[1]]
    x = li0[c2[0]]
    y = li0[c2[1]]
    li.append(operate(a,b,choice[1]))
    li0.append(intermediate_steps(x,y,choice[1],li,li0))
    li.remove(a)
    li.remove(b)
    li0.remove(x)
    li0.remove(y)

    a = li[0]
    b = li[1]
    x = li0[0]
    y = li0[1]
    li.append(operate(a,b,choice[2]))
    li0.append(intermediate_steps(x,y,choice[2],li,li0))
    li.remove(a)
    li.remove(b)
    li0.remove(x)
    li0.remove(y)

    return li[0], li0[0]
    
    
    
    

def dian(problem):
    out=[]
    finalout = ""
    o = operatechoice()
    for choice in o:
        for c1 in choice1:
            for c2 in choice2:
                li = problem[:]
                result, visual= last(li,choice,c1,c2)
                if abs(result - 24) < 0.0001:
                    out.append(visual)
    for visual in out:
        if visual not in finalout:
            finalout += visual+" = 24"+"\n"
    return (finalout.rstrip("\n"))
                    
                




                
                
    
    


        

