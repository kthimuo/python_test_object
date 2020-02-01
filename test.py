"""
このファイルに解答コードを書いてください
"""
f = open('input.txt')
#f = open('sample1.txt')
data1 = f.read() 
f.close()
lines = data1.split('\n')
m_index = len(lines)-2
inputs = {}
for index,line in enumerate(lines):
    if index==m_index:
        m = int(line)
    elif index!=len(lines)-1:
       i = int(line.split(':')[0]) 
       s = line.split(':')[1]
       inputs[i]=s
    else :
        pass
sorted_i_list = sorted(inputs)

out = ''
for i in sorted_i_list:
    if (m % i) == 0:
        out = out + inputs[i]
    else:
        pass

if out =='':
    print(m)
else :
    print(out)

