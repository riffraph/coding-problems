import otherProducts as myModule

def test_solution_1():
    input_1 = [1, 2, 3, 4, 5]
    output_1 = [120, 60, 40, 30, 24]

    assert(myModule.otherProducts_sol1(input_1) == output_1)

# assert(myModule.otherProducts_sol2(input_1) == output_1)


# ## Time the different solutions
# def wrapper(func, *args, **kwargs):
#     def wrapped():
#         return func(*args, **kwargs)
#     return wrapped

# wrappedFunc = wrapper(otherProducts_sol1, input_1)
# print('sol1 time= ', timeit.timeit(wrappedFunc))

# wrappedFunc = wrapper(otherProducts_sol2, input_1)
# print('sol2 time= ', timeit.timeit(wrappedFunc))