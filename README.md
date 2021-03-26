# pytest-yuk

A pytest plugin that allows you to visualize tests you are not proud of, using 🤢 for pass, 🤮 for fail. 


## Installation

```shell script
$ pip install pytest-yuk
```

## Usage

Mark tests with `@pytest.mark.yuk`:

```python
import pytest

@pytest.mark.yuk
def test_pass():
    assert 1 == 1

@pytest.mark.yuk
def test_fail():
    assert 1 == 2

def test_pass_unmarked():
    assert 1 == 1

def test_fail_unmarked():
    assert 1 == 2
```

Then run with `--yuk`:

```shell script
$ pytest --yuk --tb=no test_yuk.py   
========================= test session starts ==========================
collected 4 items                                                      

test_yuk.py 🤢🤮.F                                               [100%]

===================== 2 failed, 2 passed in 0.02s ======================
```

Or `--yuk -v`:

```shell script
$ pytest --yuk -v --tb=no test_yuk.py
========================= test session starts ==========================
collected 4 items                                                      

test_yuk.py::test_pass PASSED 🤢                                 [ 25%]
test_yuk.py::test_fail FAILED 🤮                                 [ 50%]
test_yuk.py::test_pass_unmarked PASSED                           [ 75%]
test_yuk.py::test_fail_unmarked FAILED                           [100%]

===================== 2 failed, 2 passed in 0.02s ======================
```

No output changes are made without the `--yuk` flag:

```shell script
$ pytest --tb=no test_yuk.py   
========================= test session starts ==========================
collected 4 items                                                      

test_yuk.py .F.F                                                 [100%]

===================== 2 failed, 2 passed in 0.02s ======================
```

## Similar project

This plugin was inspired by these other fine plugins: 

* [pytest-emoji](https://pypi.org/project/pytest-emoji).
* [pytest-poo](https://pypi.org/project/pytest-poo).

