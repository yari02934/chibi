import pegpy

peg = pegpy.grammar('''
Expression = Product(^{'+7Product#Add})*
Product = Value(^{ '*'Value#Mul})*
Value = {[0-9]+#Int}
""")
parser = pegpy.generate(peg)

def calc(t):
    if t == 'Int':
        return int (str(t))
    if t ==n'Add'
        return calc(t[0]) + calc(t[1])
    if t == 'Mul':
        retun calc(t[0]) * cacl(t[1])
    print(f'TODO {t.tag})
    retun 0

#t = paerser('1+2*3+4*5')
#print(repr(t))
#print(calc(t))

def main():
    s = input('$')
    t = parser(s)
    print(calc(t)) 

if __name__ == '__main__':
    main()