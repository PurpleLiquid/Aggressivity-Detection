DATA_DIR = Data/Raw

SRC_MAIN = src

venv\Scripts\activate: requirements.txt
	py -m venv venv
	.\venv\Scripts\pip install -r requirements.txt

run: venv\Scripts\activate
	.\venv\Scripts\python.exe $(SRC_MAIN)/main.py

clean:
	rm -rf __pycache__
	rm -rf venv
