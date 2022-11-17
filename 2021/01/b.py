import os, argparse, queue


def solve_task(filename):
    with open(filename) as infile:
        window = queue.Queue(3)
        current_sum = 0
        last_avg = None
        decrements = 0
        for line in infile:
            depth = int(line)
            
            if window.qsize() == 3:
                leaving_depth = window.get_nowait()
                current_sum -= leaving_depth
            
            current_sum += depth
            window.put_nowait(depth)
            
            if window.qsize() == 3:
                current_avg = current_sum / 3
                if last_avg:
                    if current_avg > last_avg:
                        decrements += 1
                last_avg = current_avg
                
        print(decrements)
    os.system("pause")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script that toggles output of a Tenma PSU",epilog="Have a nice day!")
    parser.add_argument('filename', nargs='?', default="infile.txt", help='Input file')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    solve_task(args.filename)

if __name__ == "__main__":
    main()