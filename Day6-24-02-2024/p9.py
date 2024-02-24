#exception handling
'''
try:
    c=10/2
except:
    print("error occured")
else:
    print(c)
finally:
    print("End")
    '''
#multiple except
'''
try:
    a=int(input())
    c=10//a
except ZeroDivisionError:
    print("cant divide by zero")
except:
    print("error occured")
else:
    print(c)
finally:
    print("End")
'''
# to know the exception i.e, raised
try:
    a=int(input())
    c=10//a
except ZeroDivisionError:
    print("cant divide by zero")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("End")
