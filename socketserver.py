from socket import *
serverPort=5000 #our socket number server
serverSocket= socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("the server is ready")

while True:
    connectionSocket, addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    print(addr)
    print(sentence)
    ip=addr[0]
    port=addr[1]
    end_of_url=sentence.split()[1]#get the last part of the url

    if end_of_url == '/' or end_of_url == '/index.html':#handling the main html file
        thtml = open("main.html")
        mainhtml = thtml.read()
        thtml.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainhtml.encode())
    elif end_of_url == '/file.css':
        thtml = open("style_index.css")
        mainhtml = thtml.read()
        thtml.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainhtml.encode())

    elif end_of_url.endswith('.css'):#here for connecting the seprate css file with the main html
        thtml = open("style_index.css")
        mainhtml = thtml.read()
        thtml.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainhtml.encode())

    elif end_of_url == '/file.html':#sending another html file
        thtml = open("linkme.html")
        mainhtml = thtml.read()
        thtml.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainhtml.encode())

    elif end_of_url.endswith('.html'):
        thtml = open("linkme.html")
        mainhtml = thtml.read()
        thtml.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainhtml.encode())

    elif end_of_url =='/sortbyname':#sending the phone names and prices sorted by name
        csv = open("test.txt")
        csv1=open("test.txt")
        names=[]
        prices=[]
        index=0
        tempcsv = csv.read()
        for i in csv1:
            #loading the names and the prices
            names.append(i.split(':')[0])
            prices.append( i.split(':')[1].rstrip())
            index=index+1
       # print(names,prices)
        #sorting the phones by name ascending
        for i in range(len(names)):
            for j in range(i+1,len(names)):
                if names[i]>names[j]:
                    names[i],names[j]=names[j],names[i]#replace the elements
                    prices[i],prices[j]=prices[j],prices[i]#and replace thier price with them
        #print(names, prices)
        csv.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/plain \r\n".encode())
        connectionSocket.send("\r\n".encode())

        output = "Names" +" Prices\n"  # Put titles to the columns.
        for i in range(0, len(names)):
            output += str(names[i])  + ":" + str(prices[i]) + "\n"
        connectionSocket.send(output.encode())

    elif end_of_url =='/sortbyprice':#sending the phone names and prices sorted by price
        csv = open("test.txt")
        csv1=open("test.txt")
        names=[]
        prices=[]
        index=0
        tempcsv = csv.read()
        for i in csv1:
            names.append(i.split(':')[0])
            prices.append(int( i.split(':')[1].rstrip()))
            index=index+1
        #print(names,prices)
        for i in range(len(names)):
            for j in range(i+1,len(names)):
                if prices[i]>prices[j]:
                    names[i],names[j]=names[j],names[i]
                    prices[i],prices[j]=prices[j],prices[i]
       # print(names, prices)
        csv.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/plain \r\n".encode())
        connectionSocket.send("\r\n".encode())
        output = "Names" +" Prices\n"  # Put titles to the columns.
        for i in range(0, len(names)):
            output += str(names[i])  + ":" + str(prices[i]) + "\n"
        connectionSocket.send(output.encode())
    elif  end_of_url.endswith('.jpg'):#sending the .png picture
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        imagejpg=open("pic1jpg.jpg",'rb')
        jpg=imagejpg.read()
        imagejpg.close()
        connectionSocket.send(jpg)
    elif end_of_url.endswith('.png'):#sending the .jpg
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        imagepng = open("pic2png.png", 'rb')
        png = imagepng.read()
        imagepng.close()
        connectionSocket.send(png)
    else:#if the url is wrong load the error.html file
        terror = open("error.html")
        mainerror = terror.read()
        terror.close()
        #to load the ip and port number of the client
        x=mainerror.index("$")#replace the first $ with the ip
        firstpart=mainerror[0:x]
        secondpart=mainerror[x+1:]
        mainerror=firstpart + str(addr[0]) + secondpart
        x = mainerror.index("$")#replace the second $ with the ip
        firstpart = mainerror[0:x]
        secondpart = mainerror[x + 1:]
        mainerror = firstpart + str(addr[1]) + secondpart
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainerror.encode())
    connectionSocket.close()