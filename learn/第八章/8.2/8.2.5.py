import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.safe_load(text)
print(data)
print(data['details'])
print(len(data['poems']))

print(data['poems'][1]['title'])
