# This program eliminates duplicates from a list using sets
# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    # This is an option without sets
    # without_duplicates = []

    # for element in some_list:
    #     if element not in without_duplicates:
    #         without_duplicates.append(element)

    # return without_duplicates

    # This is an option using sets
    without_duplicates = set(some_list)
    return without_duplicates

    # Other option
    # return without_duplicates(set(some_list))

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()