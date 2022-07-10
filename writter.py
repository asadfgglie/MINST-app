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
last_x = 0
last_y = 0

# load models
for entry in os.listdir(PATH + '/models/'):
    if os.path.isdir(os.path.join(PATH + '/models/', entry)):
        print(entry)
        path = os.listdir(os.path.join(PATH + '/models/', entry))
        print(path)
        if 'saved_model.pbtxt' in path or 'saved_model.pb' in path:
            model_list.append(entry)

model = load_model(PATH + '/models/' + model_list[0])


def save_position(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y
    pox = str(event.x)
    poy = str(event.y)
    poxy['text'] = f'(x,y):({pox},{poy})'


def add_line(event):
    canvas.create_line((last_x, last_y, event.x, event.y), fill='black', width=15)
    save_position(event)


def center_point(array):
    m = 0
    center_x = 0
    center_y = 0

    for i in array:
        for j in i:
            m += j

    for i in range(len(list(array))):
        for j in range(len(list(array[i]))):
            center_x += i * array[i][j] / m
            center_y += j * array[i][j] / m

    return int(center_x), int(center_y)


def print_data(param):
    for i in param:
        for j in i:
            print('%.1f\t' % j, end='')
        print()


def predict_pic():
    # save postscript image
    canvas.update()
    canvas.postscript(file=PATH + '/img.eps')
    try:
        data = Image.open(PATH + '/img.eps').convert('L').resize((28, 28))
    except:
        prediction['text'] = "讀取圖片失敗!"
        return
    try:
        os.remove(PATH + '/img.eps')
    except:
        prediction['text'] += "\n清除緩存失敗!"

    # load img
    data = invert(data)
    data = np.array(list(data.getdata())).reshape((28, 28)) / 255.0

    # roll to center
    print_data(data)
    print(center_point(data))
    print((14 - center_point(data)[0], 14 - center_point(data)[1]))

    data = np.roll(data, 14 - center_point(data)[0], 0)
    data = np.roll(data, 14 - center_point(data)[1], 1)

    print_data(data)
    print(center_point(data))

    # put into the model
    data = np.array([list(data)])
    prediction['text'] = prediction_str + str(argmax(model.predict(data)))

def delete():
    canvas.delete('all')
    prediction['text'] = prediction_str


def change_model(event):
    global model
    model = load_model('./models/' + model_select.get())
    model_info['text'] = model_info_str + get_model_info()


def get_model_info():
    global model
    string_list = []
    model.summary(print_fn=lambda x: string_list.append(x))
    short_model_summary = "\n".join(string_list)
    return short_model_summary


# GUI setup
root = Tk()
root.resizable(0, 0)
root.title('MNIST 手寫數字辨識板')
root.iconbitmap(PATH + "/icon/icon.ico")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, background='#B2FFCC', width=420, height=420)
canvas.grid(column=0, row=0, rowspan=4)
canvas.bind("<Button-1>", save_position)
canvas.bind("<B1-Motion>", add_line)

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
