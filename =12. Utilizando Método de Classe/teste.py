import re

def from_text(string):
    item = re.findall("é \w*", string)
    return item[0][2:] 

print(from_text("Meu video game é Wiiu e o preço é 1000 reais"))