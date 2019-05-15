import sys
kgp = open("ling073/ling073-kgp-por-corpus/kgp.sentences.txt", "r")
k_lines = kgp.readlines()
kgp.close()

por = open("ling073/ling073-kgp-por-corpus/por.sentences.txt", "r")
p_lines = por.readlines()
por.close()

word = " " + sys.argv[1] + " "

for i in range(len(k_lines)):
  if word in k_lines[i]:
    print(k_lines[i])
    print(p_lines[i])
    print()
