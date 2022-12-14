from itertools import permutations
from ortools.sat.python import cp_model


# welcome to overkilling "simple" problems by importing massive libraries part _
# I'm taking a personal vengeance on all people who say python is slow (which it is)
# by using modules written in faster languages. This time it's ortools made by google in C++
# - Okay, but why?
# Well, the reason is simple: I've always wanted to try using a SAT solver in python,
# this problem is almost built for it, where we have (up to) 10 different ints from 0 to 9
# and try to solve an equation between two numbers represented as digits
#
# I've written the normal way below this function
def ortools_solution(word1, word2, word3, sign):
    assert abs(sign) == 1
    # https://developers.google.com/optimization/cp/cryptarithmetic
    model = cp_model.CpModel()

    # from our input we get the alphabet (distinct letters) and capital letters
    words = [word1, word2, word3]
    alphabet = set("".join(words))
    capitals = set(w[0] for w in words)
    # we generate a dict of variables which will be used to create the constraints
    # and fetch the values later
    create_var = lambda c: model.NewIntVar(1 if c in capitals else 0, 9, c)
    vars_dict = dict((c, create_var(c)) for c in alphabet)

    # Define the constraints
    model.AddAllDifferent(vars_dict.values())

    # translates word into a number
    def word_value(word):
        return sum(vars_dict[c] * (10**pos) for pos, c in enumerate(word[::-1]))

    # we can either add or subtract words from eachother
    if sign > 0:
        model.Add(word_value(word1) + word_value(word2) == word_value(word3))
    else:
        model.Add(word_value(word1) - word_value(word2) == word_value(word3))

    # Solution Printer Class
    class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
        def __init__(self, variables):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.__variables = variables
            self.__solution_count = 0

        def on_solution_callback(self):
            self.__solution_count += 1
            fmt = ", ".join(f"'{v}': {self.Value(v)}" for v in self.__variables)
            print(f"[{fmt}]")

        def solution_count(self):
            return self.__solution_count

    # Call the solver
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(vars_dict.values())
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # solve
    status = solver.Solve(model, solution_printer)
    # Statistics.

    print("\nStatistics")
    print(f"  status   : {solver.StatusName(status)}")
    print(f"  conflicts: {solver.NumConflicts()}")
    print(f"  branches : {solver.NumBranches()}")
    print(f"  wall time: {solver.WallTime()} s")
    print(f"  sol found: {solution_printer.solution_count()}")


# the pure pythonic way of solving
def perm_solution(word1, word2, word3, sign):
    assert abs(sign) == 1
    # from our input we get the alphabet (distinct letters) and capital letters
    words = [word1, word2, word3]
    alphabet = set("".join(words))
    # we use the letter's position to map it to a permutation
    alpha_list = list(alphabet)
    capitals = set(w[0] for w in words)

    # translates word into a number
    def word_value(word):
        return sum(values[c] * (10**pos) for pos, c in enumerate(word[::-1]))

    # we check all permutations
    for perm in permutations(range(10), len(alpha_list)):
        # values of letters
        values = dict(zip(alpha_list, perm))

        # we're skipping the cases where a capital == c
        if any(values[c] == 0 for c in capitals):
            continue

        # we yield a value if it satisfies the equation
        if word_value(word1) + sign * word_value(word2) == word_value(word3):
            yield values

def test1():
    word1 = "KIOTO"
    word2 = "OSAKA"
    word3 = "TOKIO"
    ortools_solution(word1, word2, word3, sign=1)
    # we should get the same value as in the line above
    ortools_solution(word3, word1, word2, sign=-1)
    # a + b = c == c - a = b

    sol_iter = perm_solution(word1, word2, word3, sign=1)
    for i in sol_iter:
        print(i)

def test2():
    word1 = "SEND"
    word2 = "MORE"
    word3 = "MONEY"
    ortools_solution(word1, word2, word3, sign=1)
    # we should get the same value as in the line above
    ortools_solution(word3, word1, word2, sign=-1)
    # a + b = c == c - a = b

    sol_iter = perm_solution(word1, word2, word3, sign=1)
    for i in sol_iter:
        print(i)

if __name__ == "__main__":
    test1()
    test2()
