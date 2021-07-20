import os
import io
import codecs


def getrandomdata(n):
    import random
    data=''
    for x in range(0,n):
        data+=chr(random.randint(1,100))
    if ((data.__contains__('{')) or data.__contains__('}') or data.__contains__('$')):
        return getrandomdata(n)
    return data

def Encrypt(folderpath):
    pasFiles = [f for f in os.listdir(folderpath) if f.endswith('.pas')]
    for filename in pasFiles:
        file = codecs.open(folderpath+'\\'+filename,'r','1251')
        data=file.read()
        file.close()
        while (data.__contains__('\n\n')):
            data=data.replace('\n\n','\n')
        templst = data.split('  ')
        dataa=''
        for x in templst:
            dataa+=x+'{'+getrandomdata(50)+'}'    
        dataa=dataa.replace(';',';       \n       \n            \n      \n            \n       \n    ')
        lstofdata = dataa.split('\n')
        counter = 1
        data=''
        for x in lstofdata:
            counter+=len(x)
            if(counter>300):
                data+=' \n'+x  
                counter=1
            else:
                data+=' '+x
        output = codecs.open(f'{folderpath}\\{filename}','w','1251')
        output.write(data)
        print(f'{filename} | Encrypted')


def Decrypt(folderpath):
    pasFiles = [f for f in os.listdir(folderpath) if f.endswith('.pas')]
    for filename in pasFiles:
        input = io.open(folderpath+'\\'+filename,'r',encoding='1251')
        encData=input.read()
        decData=''
        write=True
        for i in range(0,len(encData)):
            if (encData[i]=='{'):
                if (encData[i+1]=='$'):
                    decData+=encData[i]
                    continue
                write= False
            elif(encData[i-1]=='}'):
                write=True
            if (write):
                decData+=encData[i]
        while (decData.__contains__('  ')):
            decData=decData.replace('  ',' ')
        while (decData.__contains__('\n\n')):
            decData=decData.replace('\n\n','\n')
        decData=decData.replace(';',';\n')
        output = open(f'{folderpath}\\{filename}','w',encoding='1251')
        output.write(decData)
        print(f'{filename} | Decrypted')

def main():
    filename = input('Путь проекта: ')
    print('Внимание, рекурсивное использование обфускатора приведет к порче проекта.')
    answer = input('1 - Encrypt | 2 - Decrypt :')
    if (answer=='1'):
        Encrypt(filename)
    elif (answer=='2'):
        Decrypt(filename)
    input()
  
        
    


if __name__=='__main__':
    main()


