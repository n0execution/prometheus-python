import sys
import math

x = float(sys.argv[1]);
m = float(sys.argv[2]);
sigma = float(sys.argv[3]);

a = 1 / (sigma * math.sqrt(2 * math.pi));
b = math.pow(math.e, math.pow(x - m, 2) / -(2 * math.pow(sigma, 2)))

print a * b
