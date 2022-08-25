# Python Process Manager (processpy)


processpy is simple process manager for python.
If you want to run multiple process for the same function, this tool is for you.

* You can run multiple process of the same function concurrently.
* You can choose to kill previous running process before running a new process of the same function.
* You can choose to ignore new process of the same function if it's already running.


## Installation

```bash
pip install processpy
```

## Example (No concurrency and no previous kill)

```python
from processpy import ProcessManager
import time

def sum(a, b):
    time.sleep(30)
    print(a+b)

sum_process = ProcessManager(sum, kill_previous=False, concurrent_running=False)
sum_process.run({'a': 10, 'b': 20})
time.sleep(5)

"""
The following will not run. Because concurrent run is false and kill previous is also false. So, it will simply return with doing nothing and let the previous run.
"""
sum_process.run({'a': 10, 'b': 20}) 

```

## Example (No concurrency but with previous kill)
```python
from processpy import ProcessManager
import time

def sum(a, b):
    time.sleep(30)
    print(a+b)

sum_process = ProcessManager(sum, kill_previous=True, concurrent_running=False)
sum_process.run({'a': 10, 'b': 20})
time.sleep(5)

"""
The following will kill the previous unfinished process and run. Because concurrent run is false and kill previous is True. So, it will simply kill the previous unfinished process. If previous one is already finished, nothing to kill. 
"""
sum_process.run({'a': 10, 'b': 20}) 
```

## Example (with concurrency)
```python
from processpy import ProcessManager
import time

def sum(a, b):
    time.sleep(30)
    print(a+b)

sum_process = ProcessManager(sum, concurrent_running=True)
sum_process.run({'a': 10, 'b': 20})
time.sleep(5)

"""
The following will run alongside of the previous process. 
"""
sum_process.run({'a': 10, 'b': 20}) 
```

## You can also kill the running process (if concurrent_running=False )
```python
sub_process.kill()
```