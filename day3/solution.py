import argparse


class Mountain():
    def __init__(self, grid, start_h, start_v):
        self.grid = grid
        self.grid_length = len(self.grid)
        self.grid_width = len(self.grid[0])
        self.pos_h = start_h
        self.pos_v = start_v
    
    def traverse(self, v, h):
        self.pos_h += h
        self.pos_v += v
        if self.pos_v  == self.grid_length - 1:
            stopped = True
        else:
            stopped = False
        return stopped
    
    def get_space(self, v, h):
        if h >= self.grid_width:
            h = h % self.grid_width
        return self.grid[v][h]
    
    def get_current_space(self):
        return self.get_space(self.pos_v, self.pos_h)


def vector(s):
    try:
        v, h = map(int, s.split(','))
        return v, h
    except:
        raise argparse.ArgumentTypeError("Vector must be v, h")


def main(filepath, vector):
    data = [line for line in open(filepath, "r").read().split("\n")]
    multiplied = 1
    for v, h in vector:
        mountain = Mountain(data, start_h=0, start_v=0)
        trees_hit = 0
        stopped = False
        while not stopped:
            stopped = mountain.traverse(v, h)
            if mountain.get_current_space() == "#":
                trees_hit += 1
        print(f"Traversal vector: right {h}, down {v}")
        print(f"\tTrees hit: {trees_hit}")
        multiplied *= trees_hit
    print(f"Part 2 Answer: {multiplied}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", help="path to file to be processed", required=True)
    parser.add_argument(
        "-v",
        "--vector",
        nargs="+",
        type=vector,
        help="arbitrary number of tuples representing the vertical and horizontal distance travelled at each step in the form 'v,h v,h'",
        required=True
    )
    args = parser.parse_args()
    filepath=args.filepath
    vector = args.vector
    main(filepath=filepath, vector=vector)
