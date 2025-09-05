from antlr4 import *
from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser

# Entrada de prueba con while, break y continue
input_text = """
i = 0;
while (i < 10) {
  if (i == 5) {
    break;
  }
  i = i + 1;
  continue;
}
"""

# Crear flujo de entrada
input_stream = InputStream(input_text)

# Crear analizador léxico y parser
lexer = WhileLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = WhileLangParser(token_stream)

# Analizar la entrada según la regla inicial
tree = parser.program()

# Mostrar el árbol sintáctico
print(tree.toStringTree(recog=parser))
