# Casos en donde HTML no es compatible con XML - usando el parser HTML específico
from lxml import html  # Importa específicamente el submódulo html de lxml para parsear HTML real

# Abre el archivo HTML en modo lectura (texto)
with open("input.html") as f:
    # Lee todo el contenido del archivo HTML como una cadena de texto
    html_string = f.read()

# Parsea la cadena HTML usando el parser HTML (no XML) que es más tolerante con HTML mal formado
tree = html.fromstring(html_string)

# Busca SOLO los textos de TODOS los elementos <p> en cualquier parte del documento usando XPath
para = tree.xpath("//p/text()")

# Verifica si se encontraron textos de párrafos
if len(para) > 0:
    # Itera sobre cada texto de párrafo encontrado
    for e in para:
        # Imprime solo el contenido textual de cada párrafo
        print(f"{e}\n")
else:
    # Mensaje si no se encontraron párrafos
    print("No se encontraron parrafos.")