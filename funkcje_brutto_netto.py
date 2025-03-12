# def calculate_brutto(netto: float, vat: float) -> float:
    
#     return netto * (1 + vat)


# calculate_brutto(100,0.23)

# 1000
# 0.1 - dodatek 
# 0.25 - dodatek dodatku
# 0.3 - dodatek dodatku dodatkowego
def calculate_salary(*args, base:float)-> float:
    salary = base
    for arg in args:
        salary = salary + (salary * arg)
    return salary
    # print(args)


print(calculate_salary(0.1, 0.25,0.3, base=1000))
print(calculate_salary(0.1, base=1000))