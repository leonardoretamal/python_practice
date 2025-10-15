from lxml import etree

root = etree.Element("html")

head = etree.SubElement(root, "head")
body = etree.SubElement(root, "body")

title = etree.SubElement(head, "title")
title.text = "This is page title"

heading = etree.SubElement(body, "h1", style="font-size:20pt", id="head")
heading.text = "Hello world!"

para = etree.SubElement(body, "p", id="firstPara")
para.text = "This HTML is XML Compliant!"

para = etree.SubElement(body, "p", id="secondPara")
para.text = "This is the second paragraph."

with open("input.html","wb") as f:
    f.write(etree.tostring(root, pretty_print=True))

#etree.dump(root)