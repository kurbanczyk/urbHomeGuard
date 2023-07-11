start-env:
	pip install -r ./backend/requirements.txt
	docker-compose build
	docker-compose up

test-functioncal:
	pytest tests --durations=1