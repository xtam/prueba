import re

a = "Amantes del estilo, la calidad y la accesibilidad de zapatos"
b = "Amantes a la antigua"
c = "Amantes de zapatos"


aa = re.compile("\w+").findall(a)
bb = re.compile("\w+").findall(b)
cc = re.compile("\w+").findall(c)

print aa,bb,cc

x =[]
x.append([len(set(aa) & set(bb)), "b"])
x.append([len(set(aa) & set(cc)), "c"])

print sorted(x)[0]
