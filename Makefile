.PHONY: tailwind-watch django-runserver dev

tailwind-watch:
	npm run tailwind:watch

django-runserver:
	. venv/bin/activate && python3 manage.py runserver

dev:
	# Rodando ambos em paralelo
	$(MAKE) -j 2 tailwind-watch django-runserver
