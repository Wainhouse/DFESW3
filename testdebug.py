import pdb


# A function to find the factorial of a number using tail recursion

pdb.set_trace()


def tailRecursion(factorial, result=1):
    if factorial == 1:
        return result
    else:
        tempresult = factorial * result
        return tailRecursion((--factorial, tempresult))
