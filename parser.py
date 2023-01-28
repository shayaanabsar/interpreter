from nodes import *
from tokens import *
from error import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenCounter = 0
        if len(self.tokens) == 0:
            exit()
        else:
            self.currToken = self.tokens[0]
        self.error = None

        self.currLine = 1

    def parse(self):
        while self.currToken.type != "EOF":
            parse_tree = self.parse_expression()
            if self.error is not None:
                print(self.error)
                exit()
            evaluated_parse_tree = parse_tree.evaluate()
            if evaluated_parse_tree is not None:
                print(evaluated_parse_tree)

    def next_token(self):
        while True:
            self.tokenCounter += 1
            if self.tokenCounter < len(self.tokens):
                self.currToken = self.tokens[self.tokenCounter]
            else:
                self.currToken = Token("EOF", 0, None)
            if self.currToken.type not in ("NEWLINE", "COMMENT"):
                return self.currToken
            elif self.currToken.type == "NEWLINE":
                self.currLine += 1

    def get_instructions(self):
        instructions = []
        if self.currToken.type == "LCURLYPAREN":
            self.next_token()
            while self.currToken.type != "RCURLYPAREN":
                instruction = self.parse_expression()
                instructions.append(instruction)
                if self.currToken.type == "EOF":
                    self.error = Error("InvalidSyntax", self.currLine, None, "Expected '}'")
                    return
        else:
            self.error = Error("InvalidSyntax", self.currLine, None, "Expected '{'.")
            return
        self.next_token()
        return instructions

    def get_conditional(self, type_):
        expression = self.parse_expression()
        instructions = self.get_instructions()

        if type_ == "IF":
            else_instructions = None
            if self.currToken.type == "ELSE":
                self.next_token()
                else_instructions = self.get_instructions()

            return IfStatement(expression, instructions, else_instructions)
        return WhileLoop(expression, instructions)

    def get_parameters(self):
        params = []
        if self.currToken.type == "LPAREN":
            self.next_token()
            while self.currToken.type != "RPAREN":
                params.append(self.parse_expression())
            self.next_token()

        return params

    def parse_factor(self):
        """
            F -> Number | -Number | (expression) | !expression | id = expression | Variable | true | false | "str"
            | if expr {instr}
            | case id {paths}
            | while expr {instr}
            | stdin identifier
            | stdout expr
            | func(params) {instr}
        """
        if self.currToken.type == "NUMBER":
            number = float(self.currToken.value)
            self.next_token()
            return Number(number)
        if self.currToken.type == "MINUS":
            self.next_token()
            number = self.parse_factor()
            return Negation(number)
        if self.currToken.type == "LPAREN":
            self.next_token()
            expression = self.parse_expression()
            if self.currToken.type == "RPAREN":
                self.next_token()
                return expression
            else:
                self.error = Error("InvalidSyntax", self.currLine, None, "Expected ')'.")
        if self.currToken.type == "ID":
            identifier = self.currToken.value
            self.next_token()
            if self.currToken.type == "ASSIGN":
                self.next_token()
                expression = self.parse_expression()
                return AssignVar(identifier, expression)
            if self.currToken.type == "LSQUAREPAREN":
                self.next_token()
                index = self.parse_expression()
                if self.currToken.type == "RSQUAREPAREN":
                    self.next_token()
                if self.currToken.type != "ASSIGN":
                    return Index(identifier, index)
                self.next_token()
                expression = self.parse_expression()
                return AssignVar(identifier, expression, index)
            if identifier in functionTable:
                params = []
                if self.currToken.type == "LPAREN":
                    self.next_token()
                    while self.currToken.type != "RPAREN":
                        params.append(self.parse_expression())
                    self.next_token()
                return FunctionCall(identifier, params)
            return Identifier(identifier)
        if self.currToken.type == "LSQUAREPAREN":
            self.next_token()
            items = []
            while self.currToken.type != "RSQUAREPAREN":
                items.append(self.parse_expression())
            self.next_token()
            return List(items)
        if self.currToken.type == "NOT":
            self.next_token()
            expression = self.parse_expression()
            return Not(expression)
        if self.currToken.type in ("TRUE", "FALSE"):
            value = self.currToken.value
            self.next_token()
            return Boolean(value)
        if self.currToken.type == "STRING":
            value = self.currToken.value[1:-1]
            self.next_token()
            return String(value)
        if self.currToken.type == "IF":
            self.next_token()
            return self.get_conditional("IF")
        if self.currToken.type == "SWITCH":
            self.next_token()
            switch_of = self.parse_expression()
            if self.currToken.type == "LCURLYPAREN":
                self.next_token()
                paths = []
                default_path = None
                while self.currToken.type == "CASE":
                    self.next_token()
                    if self.currToken.type == "DEFAULT":
                        path_value = "DEFAULT"
                        self.next_token()
                    else:
                        path_value = self.parse_expression()
                    instructions = self.get_instructions()
                    if path_value == "DEFAULT":
                        default_path = instructions
                    else:
                        paths.append(IfStatement(Equal(switch_of, path_value), instructions))
            self.next_token()
            return SwitchStatement(switch_of, paths, default_path)
        if self.currToken.type == "WHILE":
            self.next_token()
            return self.get_conditional("WHILE")
        if self.currToken.type == "STDIN":
            self.next_token()
            if self.currToken.type == "ID":
                return Input(self.parse_expression())
        if self.currToken.type == "STDOUT":
            self.next_token()
            return Output(self.parse_expression())
        if self.currToken.type == "FUNCTION":
            self.next_token()
            name = self.currToken.value
            self.next_token()
            params = self.get_parameters()
            instructions = self.get_instructions()
            return FunctionDefinition(name, params, instructions)
        if self.currToken.type == "RETURN":
            self.next_token()
            return Return(self.parse_expression())

    def parse_expression(self):
        """
             E -> Term  + Term | Term - Term
        """
        a = self.parse_term()

        while self.currToken.type in ("ADD", "MINUS"):
            operator = self.currToken.type
            self.next_token()
            b = self.parse_term()
            if operator == "ADD":
                a = Addition(a, b)
            elif operator == "MINUS":
                a = Subtraction(a, b)

        if self.currToken.type in ("GREATER", "LESS", "EQUAL", "GREATER_EQUAL", "LESS_EQUAL", "NOT_EQUAL"):
            operator = self.currToken.type
            self.next_token()
            b = self.parse_expression()

            if operator == "GREATER":
                a = Greater(a, b)
            elif operator == "LESS":
                a = Less(a, b)
            elif operator == "EQUAL":
                a = Equal(a, b)
            elif operator == "GREATER_EQUAL":
                a = GreaterEqual(a, b)
            elif operator == "LESS_EQUAL":
                a = LessEqual(a, b)
            elif operator == "NOT_EQUAL":
                a = NotEqual(a, b)

            operator = self.currToken.type

            if operator in ("AND", "OR"):
                self.next_token()
                b = self.parse_expression()
                if operator == "AND":
                    a = And(a, b)
                elif operator == "OR":
                    a = Or(a, b)

        return a

    def parse_term(self):
        """
            T -> Factor * Factor | Factor / Factor
        """
        a = self.parse_factor()
        while self.currToken.type in ("MULTIPLY", "DIVIDE", "MOD"):
            operator = self.currToken.type
            self.next_token()
            b = self.parse_factor()

            if operator == "MULTIPLY":
                a = Multiply(a, b)
            elif operator == "DIVIDE":
                a = Divide(a, b)
            elif operator == "MOD":
                a = Modulus(a, b)

        return a
