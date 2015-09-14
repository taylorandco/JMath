__author__ = 'taylorandco'
from utils import JMath
import json
import datetime
import collections

with open('sample.json') as data_file:
    data = json.load(data_file)

op_result = JMath().process(data)

print("Result: ", op_result)
