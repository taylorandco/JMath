__author__ = 'taylorandco'

# JMath class
class JMath:

    # function to process the operations in the JSON file
    def process(self, node):

        # Set default result 0 or False
        result = 0

        # Iterate through dicts in JSON
        for key, item in node.items():

            # Catch functions containing prefix "jm_"
            if key.startswith("jm_"):

                # List of bs_ functions here
                if key == "jm_sum":
                    # Sum function - will sum all values in list. eg. "jm_sum": [1, 2, 3] - Result: 6
                    result = self.jm_sum(item)
                elif key == "jm_count":
                    # Count function - will count number of values in list. eg. "jm_count": [1, 2, 3] - Result: 3
                    result = self.jm_count(item)
                else:
                    print("Function not found")
                    break
            else:

                # Comparative operations should only have 2 operands
                if len(item) != 2:
                    print("There must be only 2 operands per statement")
                    break

                # If the item is a dict then call the process function recursively, otherwise assign the value
                # to the operand
                if type(item[0]) == dict:
                    operand1 = self.process(item[0])
                else:
                    operand1 = item[0]

                # If the item is a dict then call the process function recursively, otherwise assign the value
                # to the operand
                if type(item[1]) == dict:
                    operand2 = self.process(item[1])
                else:
                    operand2 = item[1]

                # Process operations here
                if key == "+": # Addition
                    result = operand1 + operand2
                elif key == "-": # Subtraction
                    result = operand1 - operand2
                elif key == "x": # Multiplication
                    result = operand1 * operand2
                elif key == "/": # Division
                    result = operand1 / operand2
                elif key == "AND": # Boolean AND
                    result = operand1 & operand2
                elif key == "OR": # Boolean OR
                    result = operand1 | operand2
                elif key == "XOR": # Boolean XOR
                    result = operand1 ^ operand2
                elif key == ">": # Greater than
                    result = operand1 > operand2
                elif key == "<": # Less than
                    result = operand1 < operand2
                elif key == "=": # Equals
                    result = operand1 == operand2
                else:
                    print("Operation not found")
                    break

        #Return result
        return result

    # Specific functions here:
    def jm_sum(self, input):
        # Returns sum of inputs
        return sum(input)

    def jm_count(self, input):
        # Returns count of inputs
        return len(input)