import json
import sys
# import boto
import boto3

name = lambda a,b : a+b
print(name(10,20))

x = [2,4,5,6,7,9,24]
for i in x:
  name1 = lambda i : i%2 == 0
  print(name1(i))

def main(a,b):
  myresult = lambda a,b : a*b
  print(myresult(a,b))

main(10,20)