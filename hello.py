msg = "Hello World"
print (msg)
import xmlschema
from pprint import pprint
my_schema = xmlschema.XMLSchema('./exampleXsd/test.xsd')
#pprint(my_schema.to_dict('./exampleXsd/test.xml'))
pprint(dict(my_schema.elements)["SetStateOperDateEKSRs"])