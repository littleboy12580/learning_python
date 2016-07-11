def transla(strings):    #函数实现将英文字母往后推移两位得到新的字符串
    strlist=list(strings)    #此处将字符串转为list
    for i in range(len(strlist)):
        if(strlist[i]!=' ' and strlist[i]!='(' and strlist[i]!=')' and strlist[i]!='.' and strlist[i]!="'"):
            if(strlist[i]=='y' or strlist[i]=='z'):
                strlist[i]=chr((ord(strlist[i])-24))
            else:
                strlist[i]=chr((ord(strlist[i])+2))
    apstr=''.join(strlist)  #列表合成为字符串 str.join(list)，str为连接字符
    return apstr

#另一种解法
#for x in s:
#   if ord(x)>=ord('a') and ord(x)<=ord('z'):
#       o+=chr((ord(x)+2-ord('a'))%26+ord('a'))
#   else:
#       o+=x
#return o
secr=input('请输入密文字符串')
print('解密后明文为：%s' % transla(secr))


