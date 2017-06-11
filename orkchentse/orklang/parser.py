"""
Parser for OrkLang - simple scripting language
meant for writing expressions which evaluate to boolean at the end, like

    has_item('sword') and stat('str') > 10 or not(roll_dice(10) < 5) or true
"""
import parsimonious


GRAMMAR = r"""
    expr = space or space
    or = and more_or
    more_or = ( space "or" space and )*
    and = term more_and
    more_and = ( space "and" space term )*
    term = not / value
    not = "not" space value
    value = equals / lower / lower_or_equals / greater / greater_or_equals /
            bracketed / name
    bracketed = "(" space expr space ")"

    lower = name space "<" space literal
    lower_or_equals = name space "<=" space literal
    greater = name space ">" space literal
    greater_or_equals = name space ">=" space literal
    equals = name space "=" space literal

    name = ~"[a-z]+"
    literal = "'" chars "'"
    space = " "*
    chars = ~"[^']*"
"""


class OrkLangGrammar(parsimonious.grammar.Grammar):
    pass


class OrkLangEvaluator(parsimonious.NodeVisitor):
    """
    Parses expression using grammar, then
    visits nodes in produced syntax tree and evaluates them
    """
    def __init__(self, grammar, context):
        self.grammar = grammar
        self.context = context

    def visit_name(self, node, chidren):
        if node.text in self.context :
            val = self.context[node.text]
            return val
        else:
            raise SyntaxError(f'Unknown variable {node.text} at {node.start}')

    def visit_literal(self, node, children):
        return children[1]

    def visit_chars(self, node, children):
        return node.text

    def visit_equals(self, node, children):
        return children[0] == children[-1]

    def visit_greater(self, node, children):
        return children[0] > children[-1]

    def visit_greater_or_equals(self, node, children):
        return children[0] >= children[-1]

    def visit_lower(self, node, children):
        return children[0] < children[-1]

    def visit_lower_or_equals(self, node, children):
        return children[0] == children[-1]

    def visit_expr(self, node, children):
        return children[1]

    def visit_or(self, node, children):
        return children[0] or children[1]

    def visit_more_or(self,node, children):
        return any(children)

    def visit_and(self, node, children):
        return children[0] and (True if children[1] is None else children[1])

    def visit_more_and(self, node, children):
        return all(children)

    def visit_not(self, node, children):
        return not children[-1]

    def visit_bracketed(self, node, children):
        return children[2]

    def generic_visit(self, node, children):
        if children:
            return children[-1]



if __name__ == '__main__':
    s = "has_item('sword') and stat('str') > 10 or not(roll_dice(10) < 5) or true"
    s = "not(mime = 'asd')"

    grammar = OrkLangGrammar(GRAMMAR)

    context = {"name": "test.pdf",
               "mime": "application/pdf",
               "from": "jim@example.com",
               "to": "myself@example.com",
               "attached": True,
               "seen": False
                }

    evaluator = OrkLangEvaluator(grammar, context)
    print(evaluator.parse(s))

