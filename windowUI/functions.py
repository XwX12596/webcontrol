from requests import post, get

url = "http://127.0.0.1/"

def fetch():
    post(url+"fetch")

def warning():
    post(url+"warning")

def angUPD(ang):
    post(url+"angle"+str(ang))

def intUPD(time):
    post(url+"updateWait"+str(time))

def getImage():
    img = get(url+"result.jpg")
    with open("./image/result.jpg","wb") as f:
        for chunk in img:
            f.write(chunk)

if __name__ == "__main__":
    timeUPD(5)
