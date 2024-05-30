# import sys

# f1 = open(sys.argv[1],'one.txt',mode='r')
# f2 = open(sys.argv[2],'two.txt',mode='a')

# data = f1.read()
# f2.write(data)

# f1.close()
# f2.close()

# -------------------------------------

import argparse
import sys

def calc(args):
    if args.o=='mul':
        return args.x * args.y
    
    elif args.o=='add':
        return args.x + args.y
    
    elif args.o=='sub':
        return args.x - args.y
    
    elif args.o=='div':
        return args.x / args.y
    
    else:
        return "Something went wrong"
    
if __name__=='__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float,default=1.0, help="Enter first number ")
    parser.add_argument('--y',type=float,default=3.0,help="Enter second number")
    parser.add_argument('--o',type=str,default="add",help="this is a utiliuty for calculation")

args = parser.parse_args()
sys.stdout.write(str(calc(args)))