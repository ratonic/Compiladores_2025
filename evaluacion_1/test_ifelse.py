from antlr4 import *
from IfElseLangLexer import IfElseLangLexer
from IfElseLangParser import IfElseLangParser

# Entrada de prueba con if-else anidado
input_text = """
a = 10;
b = 20;
if (a > b) {
  max = a;
} else {
  if (a == b) {
    max = a;
  } else {
    max = b;
  }
}
"""

# Crear flujo de entrada
input_stream = InputStream(input_text)

# Crear analizador léxico y parser
lexer = IfElseLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = IfElseLangParser(token_stream)

# Analizar la entrada según la regla inicial
tree = parser.program()

# Mostrar el árbol sintáctico
print(tree.toStringTree(recog=parser))
