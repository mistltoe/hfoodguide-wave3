import sys,re
t=open(sys.argv[1]).read()
for k in sys.argv[2:]:
    print('==',k)
    for m in list(re.finditer(k,t,re.I))[:4]:
        print('  ..',t[max(0,m.start()-220):m.end()+220].replace('\n',' '))
