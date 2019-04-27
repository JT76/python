from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt

x_range= 800
y_range=600
max_iter = 255
bias_y = 0.27015
bias_x = -0.7

def x_scale(x, x_range):
    return 1.5*(x-x_range/2)/(0.5*x_range)

def y_scale(y, y_range):
    return 1.0*(y-y_range/2)/(0.5*y_range)

def gen_pixel(scaled_x, scaled_y, max_iter, bias_x, bias_y):
    iteration=max_iter
    while iteration>1 and scaled_x**2 + scaled_y**2 <4:
        new_x=scaled_x**2-scaled_y**2+bias_x
        scaled_y=2.0*scaled_x*scaled_y+bias_y
        scaled_x = new_x
        iteration = iteration - 1
    return iteration

def julia_set(x_range, y_range, max_iter, bias_x, bias_y):
    julia_set = np.zeros([y_range, x_range])
    for x in range(x_range):
        for y in range(y_range):
            scaled_x = x_scale(x, x_range)
            scaled_y = y_scale(y, y_range)
            julia_set[y][x]=gen_pixel(scaled_x, scaled_y, 
                                      max_iter, bias_x, bias_y)
    return julia_set

def plot_julia_set(x_range, y_range, max_iter, bias_x, bias_y):
    julia = julia_set(x_range, y_range, max_iter, bias_x, bias_y)  
    plt.imshow(julia)
    plt.savefig('julia_set.png')  
    plt.show()
 
def process():  
    parser = ArgumentParser(description=
                            "Display Julia set for chosen parameters")
    parser.add_argument('-xr','--x_range', type=int,
                        help='X range', default=800)
    parser.add_argument('-yr', '--y_range', type=int, 
                        help='Y Range',
                        default=600)
    parser.add_argument('-mi', '--max_iter', type=int,
                        help='max number of iterations', default=255)
    parser.add_argument('-xb','--bias_x', type=float,
                        help='bias on x', default=-0.7)
    parser.add_argument('-yb','--bias_y', type=float,
                        help='bias on y', default=0.27015)
    args = parser.parse_args()
    plot_julia_set(args.x_range, args.y_range, args.max_iter, 
                   args.bias_x, args.bias_y)

if __name__ == "__main__":
    process()