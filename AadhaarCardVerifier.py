#  AADHARCARDVERIFIER

from tkinter import *
from tkinter import filedialog
import time, os, pytesseract,  re
from selenium.webdriver.common.by import By as LC
from selenium import webdriver as WB
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


"""
Created By Suresh P | Aadhaar Card Verifier

The Aadhaar Card Verifier tool is verifying an aadhaar card number whether it's valid or invalid. 
It's a helpful tool for everyone who wants to check a fake aadhaar card to do unusual activities in India.
it's written in python and runs very smoothly without any delay.

जय हिन्द !!

made in india :)
"""

def aadhars(path):
    SDFx = Service(os.path.join(os.getcwd(), 'chromedriver.exe'))
    pytesseract.pytesseract.tesseract_cmd=os.path.join(os.getcwd(), r"ocr/tesseract.exe")
    img = path
    print('sdfasdf', img)
    text = pytesseract.image_to_string(img)
    ptn_aadhar = "\d{4}\s\d{4}\s\d{4}"
    l = re.findall(ptn_aadhar, text)
    opts = WB.ChromeOptions()
    opts.add_argument("--headless")
    driver = WB.Chrome(service=SDFx, options=opts)

    driver.get("https://myaadhaar.uidai.gov.in/verifyAadhaar")


    wait = WW(driver, 10)

    time.sleep(10)
    wait.until(
        EC.presence_of_element_located(
            (LC.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/form/div/div[1]/div/div/div/input")
        )
    ).send_keys("".join(l))

    time.sleep(10)
    try:
        m = wait.until(
            EC.presence_of_element_located(
                (LC.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/form/div/div[1]/div/div[2]/span")
            )
        )
        
        if str(m.text).startswith("Plea"):
                msg = 'invalid'
        else:
            msg = 'valid'
    except:
        msg = 'valid'


    driver.close()
    return msg



def c_screen(z,ww,hh):
        global w,h 
        w,h = z.winfo_screenwidth(),z.winfo_screenheight()
        z.geometry("{}x{}+{}+{}".format(ww, hh, int((w/2) - (ww/1.9)), int((h/2.2) - (hh/2))))



def upload_file():
    g = []
    fname = filedialog.askopenfilename(
        title='Upload a file',
        initialdir='/',
        filetypes=(
            ('jpeg files', '.jpg'),
            ('All files', '*.*')
            )
    )

    a = fname
    g.append(a)

    aadhar_card_verifier.destroy()

    dia("".join(g))
    




aadhar_card_verifier = Tk()
aadhar_card_verifier.title("Aadhaar Card Verifier")
aadhar_card_verifier.geometry("800x500")
c_screen(aadhar_card_verifier, 800, 500)
aadhar_card_verifier.config(background="#003566")
pimages = PhotoImage(file='btns.png')

pp = { 
    'image': pimages, 
    'border': 0, 
    'borderwidth': 0, 
    'background': "#003566", 
    'foreground':"#003566", 
    'highlightthickness': 0, 
    'command': upload_file
}

aadhar_btns = Button(aadhar_card_verifier, **pp)
aadhar_btns.pack()
aadhar_btns.place(relx=0.38, rely=0.42)

def dia(x):


    pp = []
    pp.append(aadhars(x))
    print(pp)

    s = Tk()
    s.geometry("800x500")
    s.title("Result | Aadhaar Card Verifier")
    s.config(background="#001D3D")
    c_screen(s, 800, 500)

    if "".join(pp) == 'valid':
        ss = Label(s, text="Valid :)\tXXXX XXXX XXXX\n", background="#FFD60A", foreground="#001D3D", width=30, font=("Arial", 20))
    elif "".join(pp) == 'invalid':
        ss = Label(s, text="invalid !!\tXXXX XXXX XXXX\n", background="#FFD60A", foreground="#001D3D", width=30, font=("Arial", 20))

    ss.pack()
    ss.place(relx=0.19, rely=0.25, height=240)

    s.mainloop()
    



aadhar_card_verifier.mainloop()