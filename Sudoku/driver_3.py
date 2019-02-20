import argparse
from main import main

parser=argparse.ArgumentParser(description='Find a solution of a Sudoku board')
parser.add_argument('Board',metavar='Board',type=str,help='A string of 81 digits representing the board')
parser.add_argument('--show-process',action='store_true',default=False,dest='display',help='If given, the process of finding a solution will be displayed.')

args=parser.parse_args()
b=args.Board
display=args.display



print('Solution:',main(b,display))
f = open('output.txt', 'w')
f.write(main(b,display) + ' BTS')