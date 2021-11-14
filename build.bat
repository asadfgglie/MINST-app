chcp 65001
pip install -r requirements.txt
pyinstaller ^
    -D writter.py ^
    -w ^
    -i %cd%\icon\icon.ico ^
    --add-data %cd%\icon;.\icon ^
    --add-data %cd%\models;.\models ^
    --add-data %cd%\README.md;. ^
    --specpath %cd%\build ^
    -n MNIST手寫辨識 ^
    --clean

if  %errorlevel% == 0 (
    echo 編譯完成!
    echo 檔案位於 %cd%\dist\MNIST手寫辨識\MNIST手寫辨識.exe
)  else  (
    echo 編譯失敗!
    echo 錯誤代碼: %errorlevel%
)
