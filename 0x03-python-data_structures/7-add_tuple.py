#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    l1 = len(tuple_a)
    l2 = len(tuple_b)
    if l1 < 2 or l2 < 2:
        if l1 < 2:
            if l1 == 0:
                new_t_a = (0, 0)
                tuple_a = new_t_a
            else:
                new_t_a = (tuple_a[0], 0)
                tuple_a = new_t_a
        if l2 < 2:
            if l2 == 0:
                new_t_b = (0, 0)
                tuple_b = new_t_b
            else:
                new_t_b = (tuple_b[0], 0)
                tuple_b = new_t_b

    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (sum_tuple)
