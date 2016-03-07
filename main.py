from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

eyes = [[100,200,150,100],
        [100,100,50,100],
        [0,0,0,0],
        [1,1,1,1]]

draw_lines( eyes, screen, color )
trans = make_translate( 150, 0, 0 )
eyes =  matrix_mult( trans, eyes )
draw_lines( eyes, screen, color )
rot = make_rotX( 180 )
nose = matrix_mult( rot, eyes )
trans = make_translate( -75, 250, 0 )
nose = matrix_mult( trans, nose )
draw_lines( nose, screen, color )

mouth = [[100,350,350,100,100],
         [250,250,300,300,250],
         [0,0,0,0,0,],
         [1,1,1,1,1]]
draw_lines( mouth, screen, color )

display(screen)
