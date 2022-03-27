import urllib.request
import webbrowser
def getlink(name):
    return "https://www.krak.dk/"+ str(name.replace(" ", "+"))+"/personer"
def inputbypass():

    name = input("Enter Name:\n")

    link = getlink(name)
    print(link)
    f = urllib.request.urlopen(link)
    myfile = f.read()
    # print(myfile)

    f = open("krak.html", "wb")
    f.write(myfile)
    f.close()
    print("Done!")

    webbrowser.open(link, new=0, autoraise=True)
print("Krak Has Runned Succesfully!")

#f = open("krak.html", "r")
#print(f.read())
