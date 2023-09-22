def make_int_list(n, l, h):
    int_list = [int(x) for x in n]
    filtered = []
    
    for i in int_list:
        if i >= l and i <= h:
            filtered.append(i)
            
    return(filtered)


def main():
    user_nums = input("Enter some integers: ")
    user_lo = int(input("Lower bound: "))
    user_hi = int(input("Upper bound: "))
    num_list = user_nums.split()

    make_int_list(num_list, user_lo, user_hi)
    
    print("original list: ", num_list)
    print("filtered list: ", make_int_list(num_list, user_lo, user_hi))

main()
