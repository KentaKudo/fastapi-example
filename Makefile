.PHONY: dep
dep:
	pip install -r requirements.txt

.PHONY: run
run:
	uvicorn main:app --reload
