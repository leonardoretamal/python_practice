from lxml import etree  # Importa el módulo etree de la biblioteca lxml para trabajar con XML/HTML

# Parsea (lee y analiza) el archivo HTML y crea un árbol de elementos XML/HTML
tree = etree.parse("input.html")

# Obtiene el elemento raíz del árbol del documento (normalmente sería <html>)
elem = tree.getroot()

# Muestra en la consola la estructura completa del documento HTML con formato
etree.dump(elem)