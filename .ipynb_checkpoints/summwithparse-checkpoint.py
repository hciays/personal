import os
import argparse
#This is just the sum of two integers with parse

parser = argparse.ArgumentParser()
parser.add_argument('first_number', type=int, help='the first number for the sum')
parser.add_argument('second_number', type=int, help='the second number for the sum')
args=parser.parse_args()

c=args.first_number + args.second_number
print("the sum is" , c)

os.system("pause")