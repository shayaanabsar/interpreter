from error import *
from math import floor, ceil
from random import random

symbolTable = {}
functionTable = {}

special_values = {
    "return_value": None
}


class AssignVar:
    def __init__(self, name, value, index=None):
        self.name = name
        self.value = value
        self.index = index

    def evaluate(self, table=symbolTable):
        value = self.value.evaluate(table=table)

        if type(value) == float:
            type_ = "Number"
        elif type(value) == bool:
            type_ = "Boolean"
        elif type(value) == str:
            type_ = "String"
        elif type(value) == list:
            type_ = "List"

        if self.index is None:
            table[self.name] = Variable(type_, value)
        else:
            if type_ == "Number":
                value = Number(value)
            elif type_ == "Boolean":
                value = Boolean(value)
            elif type_ == "String":
                value = String(value)

            table[self.name].value[int(self.index.evaluate(table=table))] = value

    def __repr__(self):
        return f"{self.name} = {self.value}"


class Variable:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"


class Identifier:
    def __init__(self, name):
        self.name = name

    def evaluate(self, table=symbolTable):
        return table[self.name].value

    def __repr__(self):
        return f"Id({self.name})"


class Number:
    def __init__(self, value):
        self.value = value

    def evaluate(self, table=symbolTable):
        return float(self.value)

    def __repr__(self):
        return f"{self.value}"


class Boolean:
    def __init__(self, value):
        self.value = value

    def evaluate(self, table=symbolTable):
        match self.value:
            case "True":
                return True
            case "False":
                return False
            case _:
                return self.value

    def __repr__(self):
        return f"{self.value}"


class String:
    def __init__(self, value):
        self.value = value

    def evaluate(self, table=symbolTable):
        return self.value

    def __repr__(self):
        return f'"{self.value}"'


class List:
    def __init__(self, items):
        self.items = items

    def evaluate(self, table=symbolTable):
        return list(self.items)


class Index:
    def __init__(self, identifier, index):
        self.identifier = identifier
        self.index = index

    def evaluate(self, table=symbolTable):
        return table[self.identifier].value[int(self.index.evaluate(table=table))].evaluate(table=table)


class Negation:
    def __init__(self, value):
        self.value = value

    def evaluate(self, table=symbolTable):
        return 0 - self.value.evaluate(table=table)

    def __repr__(self):
        return f"(-{self.value})"


class Addition:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) + self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} + {self.right})"


class Subtraction(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) - self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} - {self.right})"


class Multiply(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) * self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} * {self.right})"


class Divide(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) / self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} / {self.right})"


class Modulus(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) % self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} % {self.right})"


class Greater(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) > self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} > {self.right})"


class Less(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) < self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} < {self.right})"


class Equal(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) == self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} == {self.right})"


class NotEqual(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) != self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} != {self.right})"


class GreaterEqual(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) >= self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} >= {self.right})"


class LessEqual(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) <= self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} <= {self.right})"


class And(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) and self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} && {self.right})"


class Or(Addition):
    def evaluate(self, table=symbolTable):
        return self.left.evaluate(table=table) or self.right.evaluate(table=table)

    def __repr__(self):
        return f"({self.left} || {self.right})"


class Not(Negation):
    def evaluate(self, table=symbolTable):
        return not self.value.evaluate(table=table)

    def __repr__(self):
        return f"!{self.value}"


class IfStatement:
    def __init__(self, expression, instructions, elseInstructions=None):
        self.expression = expression
        self.instructions = instructions
        self.elseInstructions = elseInstructions

    def evaluate(self, table=symbolTable):
        if self.expression.evaluate(table=table):
            for instruction in self.instructions:
                evaluated = instruction.evaluate(table=table)

                if special_values["return_value"] is not None:
                    return special_values["return_value"]

                if evaluated is not None:
                    print(evaluated)
        else:
            if self.elseInstructions is not None:
                for instruction in self.elseInstructions:
                    evaluated = instruction.evaluate(table=table)
                    if evaluated is not None:
                        print(evaluated)

    def __repr__(self):
        return f"if {self.expression} THEN {self.instructions} else {self.elseInstructions}"


class WhileLoop:
    def __init__(self, expression, instructions):
        self.expression = expression
        self.instructions = instructions

    def evaluate(self, table=symbolTable):
        while self.expression.evaluate(table=table):
            for instruction in self.instructions:
                evaluated = instruction.evaluate(table=table)

                if special_values["return_value"] is not None:
                    return special_values["return_value"]

                if evaluated is not None:
                    print(evaluated)


class SwitchStatement:
    def __init__(self, switchOf, paths, default=None):
        self.identifier = switchOf
        self.paths = paths
        self.default = default

    def evaluate(self, table=symbolTable):
        for path in self.paths:
            if path.expression.evaluate(table=table):
                return path.evaluate(table=table)
        if self.default is not None:
            for instruction in self.default:
                evaluated = instruction.evaluate(table=table)
                if evaluated is not None:
                    print(evaluated)


class Input:
    def __init__(self, identifier):
        self.identifier = identifier

    def evaluate(self, table=symbolTable):
        variable = table[self.identifier.name]

        match variable.type:
            case "Number":
                x = float(input())
            case "String":
                x = input()
        table[self.identifier.name].value = x

    def __repr__(self):
        return f"INPUT {self.identifier}"


class Output:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, table=symbolTable):
        print(self.expression.evaluate(table=table))


class FunctionDefinition:
    def __init__(self, name, params, instructions):
        self.name = name
        self.instructions = instructions
        self.params = params

    def evaluate(self):
        functionTable[self.name] = self

    def __repr__(self):
        return f"{self.name} {tuple(self.params)} {self.instructions}"


class FunctionCall:
    def __init__(self, name, params):
        self.function = functionTable[name]
        self.params = params

        self.localSymbolTable = {}

        for index, param in enumerate(self.function.params):
            value = self.params[index].evaluate()

            if type(value) == float:
                type_ = "Number"
            elif type(value) == bool:
                type_ = "Boolean"
            elif type(value) == str:
                type_ = "String"
            elif type(value) == list:
                type_ = "List"

            self.localSymbolTable[param.name] = Variable(type_, value)

    def evaluate(self, table=symbolTable):
        for instruction in self.function.instructions:
            evaluated = instruction.evaluate(table=self.localSymbolTable)

            if special_values["return_value"] is not None:
                return_value = special_values["return_value"]
                special_values["return_value"] = None
                return return_value

            if evaluated is not None:
                print(evaluated)


class Return:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, table=symbolTable):
        special_values["return_value"] = self.expression.evaluate(table=table)


class Builtin:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def evaluate(self, table=symbolTable):
        match self.name:
            case "len":
                return len(self.parameters[0].evaluate(table))
            case "pow":
                return self.parameters[0].evaluate(table) ** self.parameters[1].evaluate(table)
            case "str":
                return str(self.parameters[0].evaluate(table))
            case "round":
                return round(self.parameters[0].evaluate(table), int(self.parameters[1].evaluate(table)))
            case "random":
                return random()
            case "floor":
                return floor(self.parameters[0].evaluate(table))
            case "ceil":
                return ceil(self.parameters[0])