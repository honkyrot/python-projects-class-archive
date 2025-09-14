import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

ON = 255
OFF = 0
vals = [ON, OFF]


def random_grid(n):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, n * n, p=[0.2, 0.8]).reshape(n, n)


def add_glider(i, j, grid):
    """adds a glider with the top-left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       255, 0, 255],
                      [0, 255, 255])
    grid[i:i + 3, j:j + 3] = glider


def update(frame_Num, img, grid, n):
    """copy grid since we require 8 neighbors for calculation, and go line by line"""
    new_grid = grid.copy()
    for i in range(n):
        for j in range(n):
            total = int((grid[i, (j - 1) % n] + grid[i, (j + 1) % n] +
                         grid[(i - 1) % n, j] + grid[(i + 1) % n, j] +
                         grid[(i - 1) % n, (j - 1) % n] + grid[(i - 1) % n, (j + 1) % n] +
                         grid[(i + 1) % n, (j - 1) % n] + grid[(i + 1) % n, (j + 1) % n]) / 255)
            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON
    # update data
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    # set grid size
    grid_size = 250
    if args.N and int(args.N) > 8:
        grid_size = int(args.N)

    # set animation update interval
    update_interval = 50
    if args.interval:
        update_interval = int(args.interval)

    # declare grid
    grid = np.array([])

    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(grid_size * grid_size).reshape(grid_size, grid_size)
        add_glider(1, 1, grid)
    else:
        # populate grid with random on/off - more off than on
        grid = random_grid(grid_size)

    fig, ax = plt.subplots()

    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, grid_size,),
                                  frames=10,
                                  interval=update_interval,
                                  save_count=50)

    # set output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()


# call main
if __name__ == '__main__':
    main()
