# Voltron Automation Test

The Automation Test project allows automating test cases for UI and API.

### Content
1. [Description](#description)
2. [Project Setup](#project-setup)
3. [Links](#links)

### Description
Automation Project with screenpy and allure.
### Project Setup
* Install python 3.10
* Install allure commandline
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
```
irm get.scoop.sh | iex
```
```
scoop install allure
```
* Clone this repo to your local machine
* Open the project
* Open terminal on IDE at project folder
* Install virtualenv:
```
py -m pip install --user virtualenv
```
* Create a virtual environment:
```
py -m venv venv
```
* Activate your virtual environment:
```
./venv/Scripts/activate
```
* Install dependencies:
```
pip install -r requirements.txt
```
### Running tests
* Run tests in a directory
```
pytest <path to test>
```
* Run tests by keyword expressions
```
pytest -k "keywork or test case name"
```
Example:
```
pytest --alluredir report  --window-size 1920,950  -k test_youtube_hub
```

### Generating report
```
allure serve <path of report>
```
Example:
```
allure serve report
```

### Links
[Pytest](https://docs.pytest.org/en/7.2.x/contents.html) 

[ScreenPy](https://screenpy-docs.readthedocs.io/en/latest/)

[Selenium Python](https://selenium-python.readthedocs.io/)
