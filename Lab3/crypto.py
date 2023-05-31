from  CSP_solver import *

variables = [
    Variable("U", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("N", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("E", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("F", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("O", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("Z", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("a", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("b", domain = [0,1,2,3,4,5,6,7,8,9] ),
    Variable("c", domain = [0,1,2,3,4,5,6,7,8,9] )
]


constraints = [
    Constraint("N + N + F == E + a * 10"),
    Constraint("a + U + U + U == Z + b * 10"),
    Constraint("b + E == N + c * 10"),
    Constraint("c + N == O")
]


csp = CSP(variables, constraints, init_node = False, init_arc = False, keep_node= True, keep_arc= True, heuristic= "mrv")

csp.solve()
