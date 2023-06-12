from requests import post, get


def fetch(url):
    post(url+"fetch")

def warning(url):
    post(url+"warning")

def angUPD(ang,url):
    post(url+str(ang))

def intUPD(time,url):
    post(url+"updateWait"+str(time))

def getImage(url):
    img = get(url+"result.jpg")
    with open("./image/result.jpg","wb") as f:
        for chunk in img:
            f.write(chunk)

