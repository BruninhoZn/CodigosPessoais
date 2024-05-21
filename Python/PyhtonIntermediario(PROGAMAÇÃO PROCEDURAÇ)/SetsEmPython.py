# add, update, clear, discard
# union
# intersection &(todos os elementos presentes nos dois sets)
# difference (elementos apenas no set da esquerda)
# symmetric_difference (elementeos que estão nois sets, mas nao em ambos)
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2
print(s3)