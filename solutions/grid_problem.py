from typing import List


def calc_product(lst: list, limit_product: int = 4) -> int:
    """
    Simple function for calculating the product of a list of 4 values
    :param lst: List of 4 values
    :return:
    int
        The product of the x numbers
    """
    # prd = lambda w, x, y, z: w*x*y*z
    # assert len(list) == limit_product
    # @todo remove limit_product

    if 0 in lst:
        return 0
    else:
        res = 1
        for ea in lst:
            res = res * ea
        return res


def get_vals(grid: List[list], row: int, indx: int, limit_product: int = 4) -> List[list]:
    """
    Function for getting the 4 directional sets of 4 numbers
        Left, Down, Diagonial Down Right, Diagonal Down left
    :param grid: Grid being worked ith
    :param row: Current Row
    :param indx: Current Index
    :return:
    List[list]
        List of Lists for the four directions
    """
    l_nums = []
    d_nums = []
    dr_nums = []
    dl_nums = []
    for add_ind in range(0, limit_product):
        l_nums.append(grid[row][indx + add_ind])
        d_nums.append(grid[row + add_ind][indx])
        dr_nums.append(grid[row + add_ind][indx + add_ind])

        if indx >= limit_product:
            dl_nums.append(grid[row + add_ind][indx - add_ind])
    all_nums = [l_nums, d_nums, dr_nums]
    if len(dl_nums) == limit_product:
        all_nums.append(dl_nums)
    return all_nums


def process_position(in_list: List[list], limit_product: int = 4) -> int:
    """
    Process a positions set of values. Returns the highest value in a set
    :param in_list: List of lists of values to publish
    :return:
    int
        The Highest Value Calulated
    """
    _v = 1
    for each in in_list:
        val = calc_product(each, limit_product=limit_product)
        _v = val if val > _v else _v
    return _v


def grid_check(grid):
    for i in grid:
        if len(i) != len(grid):
            return False
    return True


def process_grid(grid, limit_product: int = 4) -> int:
    """
    Main function for processing the grid.
    :param grid: Basically a list of lists
    :return:
    int
        Returns the highest value calulated.
    """
    _value = 1
    # Because we are doing 4 values we can stop each time 4 from the end.
    # Turned this into a var so you can choose to do more number in the grid
    # Also, can take any size of grid
    assert len(grid) > limit_product
    assert grid_check(grid)

    # Dont need to go to the end of the row or the grid so take 4 away.
    for row in range(len(grid) - limit_product):
        for indx in range(len(grid[row]) - limit_product):
            try:
                _pos_vals = get_vals(grid, row, indx, limit_product=limit_product)
                _c_val = process_position(_pos_vals, limit_product=limit_product)
                _value = _c_val if _c_val > _value else _value
            except Exception as e:
                print(e)
    return _value


list =[[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

answer = process_grid(list)
print(answer)