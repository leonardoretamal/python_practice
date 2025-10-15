from lxml import etree  # Importa el módulo etree de la biblioteca lxml para trabajar con XML/HTML

# Parsea (lee y analiza) el archivo HTML y crea un árbol de elementos
tree = etree.parse("input.html")
# Obtiene el elemento raíz del árbol del documento (normalmente <html>)
elem = tree.getroot()

# PRIMERA FORMA: Búsqueda con findall usando XPath básico
print("################### Primera forma ###################\n")
# Busca TODOS los elementos <p> que son hijos directos de <body>
para = elem.findall("body/p")

# Verifica si se encontraron elementos
if len(para) > 0:
    # Itera sobre cada elemento <p> encontrado
    for e in para:
        # Muestra la estructura completa de cada párrafo con sus etiquetas y atributos
        etree.dump(e)
else:
    # Mensaje si no se encontraron párrafos
    print("No se encontraron parrafos en la primera forma")

# SEGUNDA FORMA: Búsqueda con XPath avanzado
print("################### Segunda forma ###################\n")
# Busca SOLO los TEXTOS de TODOS los elementos <p> en cualquier parte del documento
parags = elem.xpath("//p/text()")

# Verifica si se encontraron textos de párrafos
if len(parags) > 0:
    # Itera sobre cada texto de párrafo encontrado
    for parag in parags:
        # Imprime solo el contenido textual de los párrafos
        print(f"{parag}\n")
else:
    # Mensaje si no se encontraron textos de párrafos
    print("No se encontraron parrafos en la segunda forma")