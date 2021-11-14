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
