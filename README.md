# README

## 介紹

你可以在左方的繪圖區用滑鼠寫上你的數字，然後AI就會自動辨識所寫的數字

訓練數據集為MNIST

有兩種模型可用，一種是卷積神經網路(CNN)，另一種則是最基本的神經網路(NN)

---

## 使用

輸入
>\> `python writter.py`

即可使用，記得安裝必要套件

使用
>\> `pip install -r requirements.txt`

來安裝必要套件

---

## 編譯成exe可執行檔案

build.bat是一個自動幫你把這個專案變成.exe檔案的東東，如下所示:
>\> `build.bat`

根據電腦性能所需時間不等，約5~15分鐘即可完成

build.bat同時還會自動安裝所需要的套件，若已經安裝過，不需要再次安裝的話，可以使用 `rem` 將 `build.bat` 的第二行註解掉或直接刪除

編譯完成後，可執行檔案會在 `.\dist\MNIST手寫辨識\MNIST手寫辨識.exe`

# 編譯完成的下載連結

https://download1585.mediafire.com/72vzxvyxjz7g/x3d9b62j1wt14td/MNIST%E6%89%8B%E5%AF%AB%E8%BE%A8%E8%AD%98.zip
