install

	apt
		install python-virtualenv
		python3-pip
		python3-django
		python-django-common


	pip3
		python3-django
			<sel>
			djangorestframework

setting
	python3 -m venv myvenv
	virtualenv --python=python3.6 myvenv
		<after env/bin/activate>
			이후에 django세팅 해줘야됨 ... 
			따라서 이걸 일일이 쳐주기 보단 파일을 만들어서<requirements.txt>
				-pip install -r requirements.txt
	django-admin startproject mysite

------ error -----
no module name django
	-> (myvenv) pip install django
	?-> why myvenv pip version 10.0.1 and real pip version 9.0.1
	?-> I installed django in real but why env cannot recognize


