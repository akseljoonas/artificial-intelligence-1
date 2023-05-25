from  CSP_solver import *
import time

variables = [
    Variable("A", domain = [1,2,3,4] ),
    Variable("B", domain = [1,2,3,4] ),
    Variable("C", domain = [1,2,3,4] ),
    Variable("D", domain = [1,2,3,4] ),
    Variable("E", domain = [1,2,3,4] ),
]

constraints = [
    Constraint("B >= A"),
    Constraint("A > D"),
    Constraint("C != A"),
    Constraint("B != C"),
    Constraint("D + 1 != C"),
    Constraint("C != D"),
    Constraint("D > E"),
    Constraint("C > E")
]
    
seconds = 0
for i in range(10):
    start_time = time.time()
    csp = CSP(variables, constraints, init_node= False, init_arc=True, keep_node=True, keep_arc=False, heuristic= "deg")
    csp.solve() 
    seconds += (time.time()-start_time)
    
print (f"---------------- {(seconds/10)} seconds ----------------")