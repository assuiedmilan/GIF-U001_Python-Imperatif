from math import cos, sin, radians




def position_xy(rayon, theta):
    theta = radians(theta)
    return rayon * cos(theta), rayon * sin(theta)
