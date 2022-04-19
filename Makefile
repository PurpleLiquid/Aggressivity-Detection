DATA_DIR = Data/Raw

SRC_MAIN = src

venv\Scripts\activate: requirements.txt
	py -m venv venv
	.\venv\Scripts\pip install -r requirements.txt

.PHONY: run clean

run: venv\Scripts\activate
	.\venv\Scripts\python.exe $(SRC_MAIN)/__main__.py

clean:
	rm -rf src/data/__pycache__
	rm -rf venv
