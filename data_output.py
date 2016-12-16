import re, os, pyperclip
os.chdir('D:\jiancha')
#print(os.getcwd())


#清空原始文档，重新写入 
dataClear = open('dataOut.txt', 'w')
dataClear.write('')
dataClear.close()




#匹配中心点相关坐标
dataXRegex = re.compile(r'''(中心点\s* XC = \s*([-+]?[0-9]*\.?[0-9]*)\s* \s* X = \s*([-+]?[0-9]*\.?[0-9]*)\s* \s* YC = \s*([-+]?[0-9]*\.?[0-9]*) \s* Y = \s*([-+]?[0-9]*\.?[0-9]*)\s* \s* ZC = \s*([-+]?[0-9]*\.?[0-9]*) \s* Z = \s*([-+]?[0-9]*\.?[0-9]*)\s*)''')




#allText = str(pyperclip.paste())
#print('the clipdata is: ' + '\n' + allText)
readData = open('data.txt', 'r')
allTheText = readData.read()
dataOut = open('dataOut.txt', 'a')

#print('the data found: ' + dp.group())
print('the data found: ')

k = 1
print('the all data is :')
#print(dataXRegex.search(allText))
#print(dataXRegex.findall(allText))


for df in dataXRegex.findall(allTheText):
    #print('The ' + str(k) + ' point XC is: ' + df[1])
    print('打印中心点坐标组..........')
    print('第' + str(k) + '组匹配XC坐标： ' + df[1] + ' ' + '第' + str(k) + '组匹配X坐标： ' + df[2])
    print('第' + str(k) + '组匹配YC坐标： ' + df[3] + ' ' + '第' + str(k) + '组匹配Y坐标： ' + df[4])
    print('第' + str(k) + '组匹配ZC坐标： ' + df[5] + ' ' + '第' + str(k) + '组匹配Z坐标： ' + df[6])
    print('*****************************************************************************')
    dataOut.write('X' + df[1] +' ' + 'Y' + df[3] + '\n')
    
    k = k + 1

print('The Number of count is : ' + str(k-1))
dataOut.write('\n\n;The Number of count is : ' + str(k-1) + '\n')
dataOut.write('All the Work is Done...........................................................')
readData.close()
dataOut.close()
print('Done.........')
    
