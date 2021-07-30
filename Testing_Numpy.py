import numpy as np
import sympy as sp

def main():
    '''a,b,c,d = sp.symbols('a,b,c,d')
    A = np.array([[3*a, 0*b, -1*c], [8*a, 0*b, 0*c], [0*a, 2*b, -2*c]])
    b = np.array([0*d, -2*d, -1*d])
    x = np.linalg.solve(A, b)
    print(x)'''
    letter = sp.symbols('a,b,c,d')



    eq1 = sp.Eq(1*letter[0] - 1*letter[2], 0)
    eq2 = sp.Eq(1*letter[0] - 2*letter[3], 0)
    eq3 = sp.Eq(2*letter[1] - 1*letter[2],0)

    equation_list = [1*letter[0] - 1*letter[2],1*letter[0] - 2*letter[3],2*letter[1] - 1*letter[2]];

    system_equation = [];
    for equation in equation_list:
        system_equation.append(sp.Eq(equation,0));


    solv = sp.solve(system_equation,[letter[0],letter[1],letter[2],letter[3]]);

    #solv =sp.solve([eq1, eq2, eq3],[letter[0],letter[1],letter[2],letter[3]])
    print(solv)
    b = solv.get(letter[1]);
    b = str(letter[1]);
    for element in b:
        print(element)

if __name__ == "__main__":
    main()