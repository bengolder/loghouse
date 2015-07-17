MANAGE = python ./lh/manage.py

serve:
	$(MANAGE) runserver 3001

run:
	$(MANAGE) runscript $(script)

db.rm:
	rm ./lh/test_db.sqlite3

db.check:
	$(MANAGE) makemigrations

db.migrate:
	$(MANAGE) migrate

test.travis:
	nosetests \
		--nocapture \
		--with-coverage \
		--cover-package=loghouse
test:
	make test.travis
	make clean

