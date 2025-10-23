import pandas as pd
diabetes = pd.read_csv('data/diabetes.csv',sep=',')
print(diabetes)

import re


class Calculator:

    def __init__(self):

        self.left_value = 0

        self.right_value = 0


    def calculate(self, operation):

        if self._check_and_set_value(operation):

            if "+" in operation:

                return self.left_value + self.right_value

            elif "-" in operation:

                return self.left_value - self.right_value

            elif "*" in operation:

                return self.left_value * self.right_value

            elif "/" in operation:

                try:

                    return self.left_value / self.right_value

                except ZeroDivisionError:

                    return "Invalid operation : Zero Division Error"

            else:

                return "Invalid operation"

        else:

            return "Invalid operation"


    def _check_and_set_value(self, operation):

        operation = operation.replace(" ", "")

        values = re.split('\+|\-|\*|\/', operation)

        if len(values) == 2:

            try:

                self.left_value = float(values[0])

                self.right_value = float(values[1])

                return True

            except ValueError:

                return False

        else:

            return False