__author__ = 'taylorandco'
from utils import JMath
import json

# Load JSON file
with open('sample.json') as data_file:
    data = json.load(data_file)

# Get result of operations
op_result = JMath().process(data)

# Print result
print("Result: ", op_result)
