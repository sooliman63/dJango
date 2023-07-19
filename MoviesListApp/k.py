o='30%'
print(int(o[:-1])/100)
# txt.split()
def replaceThe(txt: str) -> str:
    # write your code here ^_^
    star=txt[txt.index('the ')+4:]
    if star[0]in"aoue":
        return txt.replace("the","an")
    else:
        return txt.replace("the","a")
txt = 'I want the range'
print(replaceThe(txt))
# print(txt.replace('the','a'))
# d=txt[txt.index('the ')+4:]
# print(d[0])
# print(txt[txt.index('the ')+4:])
2*3.14
print('2*3.14: ', 2*3.14)
print(7/(6.28))
def word_repeat(word: str, n: int) -> str:
    # write your code here ^_^
    word1=''
    while n>0:

        word1+=f'{word} '
        n-=1
    return word1.rstrip()
word = 'Developers'
n = 3
print(word_repeat(word,n))