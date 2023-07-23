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
print(e_notes)
B_notes = mod_12(list(map(lambda k : k + BOffset, scale_on_e)))
G_notes = mod_12(list(map(lambda k : k + GOffset, scale_on_e)))
D_notes = mod_12(list(map(lambda k : k + DOffset, scale_on_e)))
A_notes = mod_12(list(map(lambda k : k + AOffset, scale_on_e)))
E_notes = mod_12(list(map(lambda k : k + EOffset, scale_on_e)))

import drawsvg as draw
d = draw.Drawing(1000, 1000, origin='center')

x0 = 0
y0 = 0
h = 10

fretSize = 1
fretGap = 50
Lx = fretGap * max_fret  * (1 - (max_fret + 1)/(2 * 26))
#w(x) = L1 TH(x<=12) + L1/2 TH(x > 12)
#sum(w) = 12 L1 + 12 L1/2 = 18 L1 = L -> L1 = L/18 -> L/(1.5 * 12) = L/(3/2 * 24/2) =  4 * L/(3 * nF)


nutSize = 5
nutSpacing = 3
e_line_label = draw.Text("e", 10, x0 - nutSize * nutSpacing, y0 - 0.25 * h, fill="black")
B_line_label = draw.Text("B", 10, x0 - nutSize * nutSpacing, y0 - 1.25 * h, fill="black")
G_line_label = draw.Text("G", 10, x0 - nutSize * nutSpacing, y0 - 2.25 * h, fill="black")
D_line_label = draw.Text("D", 10, x0 - nutSize * nutSpacing, y0 - 3.25 * h, fill="black")
A_line_label = draw.Text("A", 10, x0 - nutSize * nutSpacing, y0 - 4.25 * h, fill="black")
E_line_label = draw.Text("E", 10, x0 - nutSize * nutSpacing, y0 - 5.25 * h, fill="black")
e_line = draw.Line(x0,y0 -  0 * h, x0 + Lx,y0 - 0 * h, stroke='black')
B_line = draw.Line(x0,y0 -  1 * h , x0 + Lx,y0 -  1 * h, stroke='black')
G_line = draw.Line(x0,y0 -  2 * h, x0 + Lx,y0 -  2 * h, stroke='black')
D_line = draw.Line(x0,y0 -  3 * h, x0 + Lx,y0 -  3 * h, stroke='black')
A_line = draw.Line(x0,y0 -  4 * h, x0 + Lx,y0 -  4 * h, stroke='black')
E_line = draw.Line(x0,y0 -  5 * h, x0 + Lx,y0 -  5 * h, stroke='black')
for l in [e_line, B_line, G_line, D_line, A_line, E_line]:
    d.append(l)
for l_label in [e_line_label, B_line_label, G_line_label, D_line_label, A_line_label, E_line_label]:
    d.append(l_label)
#nut = draw.Rectangle(x0 - nutSize/2 - fretSize/2., y0, nutSize, 5 * h)
#d.append(nut)
for i in range(max_fret):
#    if i <= 12:
    fret = draw.Rectangle(x0 + i * (1 - (i + 1)/(2 * 26)) * fretGap - fretSize/2., y0 - 5 * h , fretSize, 5 * h)
    #else:
    #    fret = draw.Rectangle(x0 + i * fretGap/2 - fretSize/2., y0, fretSize, 5 * h)
    d.append(fret)


#if 0 not in e_notes:
#    cross = draw.Text("X", 10, x0 - nutSize * nutSpacing + 5)
#    d.append(cross)

def draw_notes(notes, string_height):
    circles = []
    for n in notes:
        if n==0:
            circle = draw.Circle(x0 - nutSize * nutSpacing/2 , y0 + 0.25 * h - 0.25 * h , 2, fill='white', stroke_width=1, stroke='black')
        else:
            fretGapAtFret = fretGap/24 * (24 - n)
            circle = draw.Circle(x0 + n * (1 - (n + 1)/(2 * 26)) * fretGap - fretGapAtFret/2., y0 +  string_height - 0.25 * h, 2)
            #else:
            #    circle = draw.Circle(x0 + 11.5 * fretGap + (n%12 + 0.5) * fretGap/2, 0.25 * h, 1)
        circles += [circle]
    return circles

e_circles = draw_notes(e_notes, -0.25 * h)
B_circles = draw_notes(B_notes, -1.25 * h)
G_circles = draw_notes(G_notes, -2.25 * h)
D_circles = draw_notes(D_notes, -3.25 * h)
A_circles = draw_notes(A_notes, -4.25 * h)
E_circles = draw_notes(E_notes, -5.25 * h)

circles = e_circles + B_circles + G_circles + D_circles + A_circles + E_circles

for circle in circles:
    d.append(circle)

d.set_pixel_scale(2)
d.save_svg('blank.svg')
