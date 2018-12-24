#Raunak Srikant Mokhasi
#2017085
#Section A - Group 5

from a2 import *

global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9

assert game1(500)<=0.66 and game1(500)>= 0.52 , "ERROR"
assert game1(1000)<=0.64 and game1(1000)>= 0.53 , "ERROR"
assert game1(5000)<=0.63 and game1(10000)>= 0.54 , "ERROR"
assert game1(10000)<=0.62 and game1(10000)>= 0.55 , "ERROR"

assert game2(500)<=0.14 and game1(500)>= 0.01 , "ERROR"
assert game2(1000)<=0.13 and game1(1000)>= 0.03 , "ERROR"
assert game2(5000)<=0.115 and game1(5000)>= 0.06 , "ERROR"
assert game2(10000)<=0.11 and game1(10000)>= 0.065 , "ERROR"

assert game3(500)<=0.1 and game1(500)>= -0.01 , "ERROR"
assert game3(1000)<=0.1 and game1(1000)>= -0.01 , "ERROR"
assert game3(5000)<=0.1 and game1(5000)>= -0.01 , "ERROR"
assert game3(10000)<=0.1 and game1(10000)>= -0.01 , "ERROR"

assert validmove(-5) == False, "Please Provide a valid integer between 1 and 9"
assert validmove(-10) == False, "Please Provide a valid integer between 1 and 9"
assert validmove(1.4) == False, "Please Provide a valid integer between 1 and 9"
assert validmove(10) == False, "Please Provide a valid integer between 1 and 9"

