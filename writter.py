from tkinter import *
from tkinter import ttk
from tensorflow.keras.models import load_model
import numpy as np
from numpy import argmax
from PIL import Image
from PIL.ImageOps import invert
import os

PATH = os.getcwd()
print(PATH)

model_list = []

for entry in os.listdir(PATH + '/models/'):
    if os.path.isdir(os.path.join(PATH + '/models/', entry)):
        print(entry)
        model_list.append(entry)

model = load_model(PATH + '/models/' + model_list[0])

def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
    pox = str(event.x)
    poy = str(event.y)
    poxy['text']=f'(x,y):({pox},{poy})'

def addLine(event):
    canvas.create_line((lastx, lasty, event.x, event.y), fill='black', width=15)
    savePosn(event)

def predict_pic():
    # save postscipt image 
    canvas.update()
    canvas.postscript(file=PATH + '/img.eps')
    data = None
    try:
        data = Image.open(PATH + '/img.eps').convert('L').resize((28,28))
    except:
        prediction['text'] = "讀取圖片失敗!"
        return
    try:
        os.remove(PATH + '/img.eps')
    except:
        prediction['text'] += "\n清除緩存失敗!"
    data = invert(data)
    data = np.array( [ list( np.array( list( data.getdata() ) ).reshape((28,28)) ) ] ) / 255.0
    prediction['text'] = prediction_str + str(argmax(model.predict(data[:])))

def delete():
    canvas.delete('all')
    prediction['text'] = prediction_str

def change_model(event):
    global model
    model = load_model('./models/' + model_select.get())
    model_info['text'] = model_info_str + get_model_info()

def get_model_info():
    global model
    stringlist = []
    model.summary(print_fn=lambda x: stringlist.append(x))
    short_model_summary = "\n".join(stringlist)
    return short_model_summary

root = Tk()
root.resizable(0,0)
root.title('MNIST 手寫數字辨識板')
root.iconbitmap(PATH + "/icon/icon.ico")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, background='#B2FFCC', width=420, height=420)
canvas.grid(column=0, row=0, rowspan=4)
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

poxy = ttk.Label(root, text='(x,y):(None,None)')
poxy.grid(column=0, row=4, sticky=W, padx=5, pady=5)

prediction_str = '辨識結果:'
prediction = ttk.Label(root, text=prediction_str, width=30)
prediction.grid(column=1, row=0, sticky=(N, W), padx=5, pady=5)

model_info_str = '模型訊息:\n'
model_info = ttk.Label(root, text=model_info_str + get_model_info())
model_info.grid(column=2, row=0, sticky=(N, W), padx=5, pady=5)

model_select = ttk.Combobox(root)
model_select['values'] = model_list
model_select.set(model_list[0])
model_select.state(["readonly"])
model_select.bind('<<ComboboxSelected>>', change_model)
model_select.grid(column=1, row=1, padx=5, pady=5, sticky=(E, W))

reset = ttk.Button(root, command=delete, text='清空畫布')
reset.grid(column=1, row=2, padx=5, pady=5, sticky=(E, W))
predict = ttk.Button(root, command=predict_pic, text='辨識這個數字')
predict.grid(column=1, row=3, padx=5, pady=5, sticky=(E, W))


root.mainloop()