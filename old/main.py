import yaml
import os

import numpy as np


def rem_dups(a): 
    return [int(i) for i in dict({str(i):i for i in a}).keys()]

def mod_12(x, min_fret =0, max_fret = 24):
    mod_12 = sorted(list(map(lambda f : f % 12 , x)))
    mod_12_upper = sorted(list(map(lambda f : f % 12 + 12 , x)))
    mod_12_upper_2 = sorted(list(map(lambda f : f % 12 + 12 * 2,  x)))
    #mod_12_lower = sorted(list(map(lambda f : f - 12 , x)))
    #mod_12_lower_2 = sorted(list(map(lambda f : f % 12 - 12 * 2,  x)))

    mod_12_full_raw = mod_12 + mod_12_upper + mod_12_upper_2
    mod_12_full = rem_dups(sorted(filter(lambda f : f>=min_fret and f<=max_fret, mod_12_full_raw)))
    return mod_12_full

def notes_on_strings(scale_on_e, strings, min_fret =0, max_fret = 24):
    return {string : mod_12(list(map(lambda k : k + strings[string]['offset'], scale_on_e)), min_fret, max_fret) for string in strings}

strings = {"E_low" : {"offset" : 0}, "A" : {"offset" : 5}, "D" : {"offset" : 10}, "G" : {"offset" : 3}, "B" : {"offset" : 7}, "E_high" : {"offset" : 0}}
scale_on_e = [0,1,3,5,7,8,10,12]

scales = notes_on_strings(scale_on_e, strings)
