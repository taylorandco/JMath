__author__ = 'taylorandco'


class JMath:
    def process(self, node):
        result = 0

        for key, item in node.items():

            if key.startswith("bs_"):
                if key == "bs_sum":
                    result = self.bs_sum(item)
                elif key == "bs_count":
                    result = self.bs_count(item)
            else:
                if len(item) != 2:
                    print("There must be only 2 operands per statement")
                    break
                if type(item[0]) == dict:
                    operand1 = self.process(item[0])
                else:
                    operand1 = item[0]

                if type(item[1]) == dict:
                    operand2 = self.process(item[1])
                else:
                    operand2 = item[1]

                if key == "+":
                    result = operand1 + operand2
                elif key == "-":
                    result = operand1 - operand2
                elif key == "x":
                    result = operand1 * operand2
                elif key == "/":
                    result = operand1 / operand2
                elif key == "AND":
                    result = operand1 & operand2
                elif key == "OR":
                    result = operand1 | operand2
                elif key == "XOR":
                    result = operand1 ^ operand2
                elif key == ">":
                    result = operand1 > operand2
                elif key == "<":
                    result = operand1 < operand2
                elif key == "=":
                    result = operand1 == operand2

        return result

    def bs_sum(self, input):
        return sum(input)

    def bs_count(self, input):
        return len(input)