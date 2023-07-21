eOffset = 0
BOffset= 5
GOffset=9
DOffset=14
AOffset =19
EOffset = 24

scale_on_e = [5, 7, 8, 10, 12, 13, 15]
min_fret = 0
max_fret = 24


rem_dups = lambda a : [int(i) for i in dict({str(i):i for i in a}).keys()]

def mod_12(x):
    mod_12 = sorted(list(map(lambda f : f % 12 , x)))
    mod_12_upper = sorted(list(map(lambda f : f % 12 + 12 , x)))
    mod_12_upper_2 = sorted(list(map(lambda f : f % 12 + 12 * 2,  x)))
    #mod_12_lower = sorted(list(map(lambda f : f - 12 , x)))
    #mod_12_lower_2 = sorted(list(map(lambda f : f % 12 - 12 * 2,  x)))

    mod_12_full_raw = mod_12 + mod_12_upper + mod_12_upper_2
    mod_12_full = rem_dups(sorted(filter(lambda f : f>=min_fret and f<=max_fret, mod_12_full_raw)))
    return mod_12_full

e_notes = mod_12(scale_on_e)
B_notes = mod_12(list(map(lambda k : k + BOffset, scale_on_e)))
G_notes = mod_12(list(map(lambda k : k + GOffset, scale_on_e)))
D_notes = mod_12(list(map(lambda k : k + DOffset, scale_on_e)))
A_notes = mod_12(list(map(lambda k : k + AOffset, scale_on_e)))
E_notes = mod_12(list(map(lambda k : k + EOffset, scale_on_e)))

import drawsvg as draw
d = draw.Drawing(400, 400, origin='center')
Lx = 100
x0 = 0
h = 10
e_line = draw.Line(x0,y0 +  0 * h, x0 + Lx,y0 +  0 * h, stroke='black')
B_line = draw.Line(x0,y0 +  1 * h , x0 + Lx,y0 +  1 * h, stroke='black')
G_line = draw.Line(x0,y0 +  2 * h, x0 + Lx,y0 +  2 * h, stroke='black')
D_line = draw.Line(x0,y0 +  3 * h, x0 + Lx,y0 +  3 * h, stroke='black')
A_line = draw.Line(x0,y0 +  4 * h, x0 + Lx,y0 +  4 * h, stroke='black')
E_line = draw.Line(x0,y0 +  5 * h, x0 + Lx,y0 +  5 * h, stroke='black')
for l in [e_line, B_line, G_line, D_line, A_line, E_line]:
    d.append(l)
d.set_pixel_scale(2)
d.save_svg('blank.svg')

