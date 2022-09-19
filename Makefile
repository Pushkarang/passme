setup:
	python3 -m pip install --user virtualenv
	python3 -m venv env
	
installDeps: 
	pip install -r requirements.txt

build: installDeps src/passme.py
	pyinstaller --onedir src/passme.py
	rm -rf env
	rm -rf build
	rm passme.spec

install: build
	sudo ln -s `pwd`/dist/passme/passme /usr/local/bin/passme




