# _activate-env:
# 	. venv/bin/activate

start-env:
	pip install -r ./backend/requirements.txt
	docker-compose build
	docker-compose up

test-functional:
	python3 -m pytest tests --durations=1