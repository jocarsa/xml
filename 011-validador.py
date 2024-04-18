from lxml import etree

archivo = '012-esquema continuo.xml'
esquema = '009-esquema.xsd'

xml = etree.parse(archivo)
xmlesquema = etree.XMLSchema(file=esquema)

if xmlesquema.validate(xml):
    print("valida OK")
else:
    print("no valida")
    print(schema.error_log)
