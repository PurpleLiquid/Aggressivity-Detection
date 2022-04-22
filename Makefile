DATA_DIR = Data/Raw

SRC_MAIN = src

venv\Scripts\activate: requirements.txt
	py -m venv venv
	.\venv\Scripts\pip install -r requirements.txt

.PHONY: setup run clean

setup: venv\Scripts\activate
	.\venv\Scripts\python.exe -m pip install --upgrade pip
	.\venv\Scripts\pip install pandas
	.\venv\Scripts\pip install glob2
	.\venv\Scripts\pip install nltk

run: venv\Scripts\activate
	.\venv\Scripts\python.exe $(SRC_MAIN)/__main__.py

clean:
	rm -rf src/data/__pycache__
	rm -rf src/ml/__pycache__
	rm -rf venv
