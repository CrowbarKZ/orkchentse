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
            function / bracketed / name

    bracketed = "(" space expr space ")"
    function = name "(" universal_literal ")"

    lower = name space "<" space universal_literal
    lower_or_equals = name space "<=" space universal_literal
    greater = name space ">" space universal_literal
    greater_or_equals = name space ">=" space universal_literal
    equals = name space "=" space universal_literal

    name = ~"[a-z_]+"
    universal_literal = literal / number
    literal = "'" chars "'"
    space = " "*
    chars = ~"[a-zA-Z_]+"
    number = ~"\d+"
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
        self.context.update({
            'true': True,
            'false': False,
        })

    def visit_name(self, node, chidren):
        if node.text in self.context:
            return self.context[node.text]
        else:
            raise SyntaxError(f'Unknown variable {node.text} at {node.start}')

    def visit_literal(self, node, children):
        return children[1]

    def visit_number(self, node, children):
        return int(node.text)

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

    def visit_function(self, node, children):
        f = children[0]
        arg = children[2]
        return f(arg)

    def generic_visit(self, node, children):
        if children:
            return children[-1]


if __name__ == '__main__':
    s = "has_item('sword') and stat('str') > 10 or not(roll_dice(10) < 5) or true"

    grammar = OrkLangGrammar(GRAMMAR)

    def has_item(item):
        return True

    def stat(stat):
        return 12

    def roll_dice(dice):
        return dice

    context = {
        "has_item": has_item,
        "stat": stat,
        "roll_dice": roll_dice,
    }

    evaluator = OrkLangEvaluator(grammar, context)
    print(evaluator.parse(s))

