# README

## 介紹

你可以在左方的繪圖區用滑鼠寫上你的數字，然後AI就會自動辨識所寫的數字

訓練數據集為MNIST

有兩種模型可用，一種是卷積神經網路(CNN)，另一種則是最基本的神經網路(NN)

---
---

## 使用

輸入
```python writter.py```

即可使用，記得安裝必要套件

使用
```pip install -r requirements.txt```

來安裝必要套件

---

### 在本手寫板中使用自己訓練的模型

將模型放入 `models` 資料夾即可

僅接受 tensorflow 框架之模型

若是已經編譯好的手寫板想新增模型，在手寫板執行檔目錄中也有一個 `models` 資料夾，將 tensorflow 框架模型放進去即可使用

---
---

## 編譯成exe可執行檔案

build.bat 是一個自動幫你把這個專案變成.exe檔案的東東，如下所示:
```build.bat```

根據電腦性能所需時間不等，約 5 ~ 15 分鐘即可完成

build.bat 同時還會自動安裝所需要的套件，若已經安裝過，不需要再次安裝的話，可以使用 `rem` 將 `build.bat` 的第二行註解掉或直接刪除

編譯完成後，可執行檔案會在 `.\dist\MNIST手寫辨識\MNIST手寫辨識.exe`

## 編譯完成的下載連結

<https://www.mediafire.com/file/19nmw012dc9d59p/MNIST手寫辨識.zip/file>
