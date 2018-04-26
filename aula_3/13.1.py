file = open('normal.txt', 'w')
file.write('this is\nthe normal file\nwith the\nnormal text\nin the\nnormal order\n')
file.close()

fin = open('normal.txt', 'r')
lines = fin.readlines()
fin.close()

fout = open('reversed.txt', 'w')
fout.writelines(lines[::-1])
fout.close()
