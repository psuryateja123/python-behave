# python-behave


#### The tests in the framework are written in BDD pattern using feature file.

#### Installation: The required dependencies can be installed by 
* Type
```
pip install -r requirements.txt
```

* if there are any issues in installing the dependencies, they can be installed seperately using 
```
pip install name_of_the_dependency
```

#### Running tests: Considered that you have already cloned the project. You can run tests by typing behave in the commandline

* Type
```
behave
```
* Can run tests using tags, as I have added smoke tag
```
behave --tags=@smoke
```

This will run all the tests on a chrome browser.

Also integrated [Allure report](https://docs.qameta.io/allure/). This acts like a runner and also helps to generate reports.

* To run specific tests by using tags
```
behave --tags=@NAME_OF_THE_TAG -f allure_behave.formatter:AllureFormatter -o RESULTS_FOLDER ./features

```

* After running the tests, to view the results

```
allure serve RESULTS_FOLDER
```
