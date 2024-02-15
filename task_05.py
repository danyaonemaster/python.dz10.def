import copy


def sum_lists(list_):
    list_num = [i for i in list_ if type(i) is int]
    return sum(list_num)


def sorted_lists(list_):
    str_list = [i for i in list_ if type(i) is str]
    return sorted(str_list)


def swap_elements(list_, n1, n2):
    list_[n1], list_[n2] = list_[n2], list_[n1]
    return list_


def pop_two_elements(original_list, copied_list, compare):
    for i in range(len(original_list)):
        if compare(i):
            original_list.remove(copied_list[i])
    return original_list


original_list = ["Category", 5, 10, "Movie", "Game", 20, 18, "App", "Source", 50]
copied_list = copy.deepcopy(original_list)

cmp = lambda x: x % 2 == 0
print(f"sum numbers : {sum_lists(original_list)}\n"
      f"sorted list : {sorted_lists(original_list)}\n"
      f"swap elements : {swap_elements(original_list, 1, 6)}\n"
      f"removing even elements : {pop_two_elements(original_list, copied_list, cmp)}\n")
