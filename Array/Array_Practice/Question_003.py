# remove the diplicate elements from the array
def remove_duplicates(my_list):
    lst = []
    for i in my_list:
        if i not in lst:
            lst.append(i)
    my_list = lst
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    print("The list with unique elements only:")
    print(remove_duplicates(my_list))
