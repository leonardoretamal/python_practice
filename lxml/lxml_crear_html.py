from lxml import etree  # Importa el módulo etree de la biblioteca lxml para trabajar con XML/HTML

# Crea el elemento raíz del documento HTML
root = etree.Element("html")

# Crea el elemento head como subelemento directo de root (html)
head = etree.SubElement(root, "head")
# Crea el elemento body como subelemento directo de root (html)
body = etree.SubElement(root, "body")

# Crea el elemento title dentro de head (para el título de la página)
title = etree.SubElement(head, "title")
# Asigna el texto que aparecerá en la pestaña del navegador
title.text = "This is page title"

# Crea un encabezado h1 en el body con atributos de estilo e ID
heading = etree.SubElement(body, "h1", style="font-size:20pt", id="head")
# Asigna el texto principal del encabezado
heading.text = "Hello world!"

# Crea un párrafo en el body con identificador único
para = etree.SubElement(body, "p", id="firstPara")
# Asigna el texto del primer párrafo
para.text = "This HTML is XML Compliant!"

# Crea un segundo párrafo en el body (reutilizando la variable 'para')
para = etree.SubElement(body, "p", id="secondPara")
# Asigna el texto del segundo párrafo
para.text = "This is the second paragraph."

# Abre/Crea el archivo HTML en modo escritura binaria
with open("input.html","wb") as f:
    # Escribe la estructura HTML en el archivo con formato legible
    f.write(etree.tostring(root, pretty_print=True))

# Alternativa: etree.dump(root) 
# Esta línea comentada mostraría el HTML en consola en lugar de guardarlo