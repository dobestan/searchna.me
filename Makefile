# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python searchname/manage.py makemigrations
	python searchname/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls searchname/ | grep -v -e 'manage.py' | xargs -I{} rm -rf searchname/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 searchname/
	searchname/manage.py test searchname/ -v 2
