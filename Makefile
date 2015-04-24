MANAGE = python ./lh_project/manage.py

run:
	${MANAGE} runserver 3001

db.check:
	${MANAGE} makemigrations

db.migrate:
	${MANAGE} migrate


