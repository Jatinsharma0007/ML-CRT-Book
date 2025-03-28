def modify_list(input_list):
    input_list.append(77)
    print("Inside the function (after modification):")
    print(input_list)

def main():
    my_list = [1, 2, 3, 4, 5]
    print("Original list before function call:")
    print(my_list)
    
    modify_list(my_list)
    
    print("\nList after function call:")
    print(my_list)

main()