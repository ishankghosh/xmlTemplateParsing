import json
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader

f = open("sample-data-1.json")
data = json.loads(f.read())

print(data)
#print(data["data"]["upcomingorders"])
searchpath = ['']
engine = Engine(
    loader=FileLoader(searchpath),
    extensions=[CoreExtension()]
)
template = engine.get_template('email-template.xml')

print(template.render(data))
