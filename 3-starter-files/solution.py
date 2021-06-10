# CMSC389O Spring 2020
# HW3: Searching & Sorting -- Implement Natural Logarithm

# Description:
# Implement the ln() function, but don't use the library log functions or integration functions.
# Other library functions are fine
# Solutions should be within 1e-6 of the actual value (i.e. |student_ln(x) - ln(x)| < 1e-6)

# Hints:
# - This is for the sorting and searching section of the course. Don't use integration or bit manipulation.
# - What if you were given a sorted list of values where at least one of them were guaranteed to be acceptable?
# - ln() is (strictly) monotonically increasing -- i.e. for x < y in the domain, ln(x) < ln(y)

# Examples:
# 2.718281828459045 -> 1 (or anything within 1e-6 of 1)
# 20.085536923187668 -> 3 (or anything within 1e-6 of 3)

# Edge cases:
# ln(0) should return the floating point negative infinity float('-inf')
# ln(x) for negative x should raise ValueError (it's an invalid input)

# Running the public tests:
# python3 PublicTests.py

# Submit server notes:
# 2 of the release tests (9 and 10) are performance tests.
# Failing either of the last 2 tests (red box) is probably not due to
# correctness issues if you are passing the other tests.

# for student use
from math import exp, factorial
EPSILON: float = 1e-6

def student_ln(x: float) -> float:
    y = x
    upperBound: float
    lowerBound: float
    if (y == 0):
        return float('-inf')
    if (y < 0): 
        raise ValueError()
    
    if (y < 1) :
        
        point = 0.0
        counter = 0.0

        while(exp(counter) - x > 0) :
            lowerBound = counter
            counter -= 1
            upperBound = counter
            point = (lowerBound + upperBound)/2
        
        while (abs(exp(point) - x) > EPSILON*x) :
            
            if ((exp(point) - x) < 0) :
                upperBound = point
                point = (upperBound + lowerBound)/2
                
            elif ((exp(point) - x) > 0) :
                lowerBound = point
                point = (upperBound + lowerBound)/2
                
        y = point
            
        

    if (y >= 1) :
        
        point = 0.0
        counter = 0.0

        while(exp(counter) - x < 0) :
            lowerBound = counter
            counter += 1
            upperBound = counter
            point = (lowerBound + upperBound)/2
            
        
        while (abs(exp(point) - x) > EPSILON) :
            if((exp(point) - x) > 0):
                upperBound = point
                point = (lowerBound + upperBound)/2
            elif((exp(point) - x) < 0):
                lowerBound = point
                point = (lowerBound + upperBound)/2

        y = point

        
    return y





    
  



