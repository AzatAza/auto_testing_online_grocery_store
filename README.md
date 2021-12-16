# Online grocery store UI tests
Selenium/Python/Allure

Test app:
```
https://berpress.github.io/online-grocery-store/
```

Use python 3.9 +
Create and activate virtual environments:

```
python3 -m venv env
source env/bin/activate
```

Run in terminal:

```
pip install -r requirements.txt
```

pre-commit: https://pre-commit.com
```
pre-commit run --all-files
```

Run tests and get allure test report you can use:
```
pip install allure-pytest
pytest --alluredir=my_allure_results
allure serve my_allure_results
```
