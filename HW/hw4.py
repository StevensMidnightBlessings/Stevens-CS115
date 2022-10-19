'''
... Created on 9/26/22
... @author:  
... Pledge:  I pledge my honor that I have abided by the Stevens Honor System.
... CS115 - Hw 4
'''
#task 1

def newList(x):
    '''helps pascal row by adding each element and putting them in a temp list.'''
    if x == []:
        return 0
    elif len(x) == 1:
        return [x[0]]
    else:
        return [x[0] + x[1]] + newList(x[1:]) 


def pascal_row(row):
    '''takes an input row(row number) and outputs a list of elements in the row'''
    if row == 0:
        return [1]
    else:
        return [1] + newList(pascal_row(row - 1))

#task 2
def pascal_triangle(n):
    '''takes single int n, returns a list of list containing values of all the
    vlaues of all rows up to and including row n.'''
    if n == 0:
        return [pascal_row(0)]
    else:
        return pascal_triangle(n - 1) + [pascal_row(n)]


#task 3
def test_pascal_row():
    '''test function for pascal row'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(7) == [1,7,21,35,35,21,7,1]
    assert pascal_row(10) == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(50) == [1, 50, 1225, 19600, 230300, 2118760, 15890700, 99884400, 536878650, 2505433700, 10272278170, 37353738800, 121399651100, 354860518600, 937845656300, 2250829575120, 4923689695575, 9847379391150, 18053528883775, 30405943383200, 47129212243960, 67327446062800, 88749815264600, 108043253365600, 121548660036300, 126410606437752, 121548660036300, 108043253365600, 88749815264600, 67327446062800, 47129212243960, 30405943383200, 18053528883775, 9847379391150, 4923689695575, 2250829575120, 937845656300, 354860518600, 121399651100, 37353738800, 10272278170, 2505433700, 536878650, 99884400, 15890700, 2118760, 230300, 19600, 1225, 50, 1]
    assert pascal_row(15) == [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1]

def test_pascal_triangle():
    '''test function for pascal triangle'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1,1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
