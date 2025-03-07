
def function_1(name):
    print(f"Func 1: {name}")
    
def function_2(name):
    print(f"Func 2: {name}")
    
def function_3(name):
    print(f"Func 2: {name}")
    
def function_4(name):
    print(f"Func 2: {name}")
    
def function_5(name):
    print(f"Func 2: {name}")


if __name__ == "__main__":
    
    example_key_arg = "func5"

    retrieval_funcs = {
        "func1": function_1,
        "func2": function_2,
        "func3": function_3,
        "func4": function_4,
    }

    for key in retrieval_funcs.keys():
        retrieval_funcs[key](key)
        
    
    if retrieval_funcs.get(example_key_arg):
        retrieval_funcs.get(example_key_arg)("ola")
