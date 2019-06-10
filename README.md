# sorting_tuples

## Method 1: 
Uses in-built list sort and then merge 
## Method 2: 
Does not sort but swaps or merges in place.

## Findings
Method 2 seems to be better on larger lists. Although the performance improvement is not always guaranteed. Also, there is an intermittent bug somewhere, but it did not want to take more time. 

**Update**
On reviewing closely method 2 is almost always faster , Yipeee !!!


## Code 
``` https://github.com/chandanmaruthi/sorting_tuples ```

## Results
```
Starting experiments
 Time taken to execute method_1  for list size 10 time taken 0.000019
 Time taken to execute method_2  for list size 10 times taken 0.000009
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100 times taken 0.000096
 Time taken to execute method_2  for list size 100 times taken 0.000005
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 1000 times taken 0.001054
 Time taken to execute method_2  for list size 1000 times taken 0.000005
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 10000 times taken 0.019317
 Time taken to execute method_2  for list size 10000 times taken 0.000009
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100000 times taken 1.234640
 Time taken to execute method_2  for list size 100000 times taken 0.000013
---------------------------------------------------------------------------------
(env) chandanmaruthi:sorting_tuples$ python sort_tuples.py 
Starting experiments
 Time taken to execute method_1  for list size 10 time taken 0.000040
 Time taken to execute method_2  for list size 10 times taken 0.000009
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100 times taken 0.000114
 Time taken to execute method_2  for list size 100 times taken 0.000005
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 1000 times taken 0.001097
 Time taken to execute method_2  for list size 1000 times taken 0.000013
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 10000 times taken 0.020413
 Time taken to execute method_2  for list size 10000 times taken 0.000013
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100000 times taken 1.239086
 Time taken to execute method_2  for list size 100000 times taken 0.000005
---------------------------------------------------------------------------------
(env) chandanmaruthi:sorting_tuples$ python sort_tuples.py 
Starting experiments
 Time taken to execute method_1  for list size 10 time taken 0.000040
 Time taken to execute method_2  for list size 10 times taken 0.000010
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100 times taken 0.000101
 Time taken to execute method_2  for list size 100 times taken 0.000006
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 1000 times taken 0.001048
 Time taken to execute method_2  for list size 1000 times taken 0.000011
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 10000 times taken 0.019216
 Time taken to execute method_2  for list size 10000 times taken 0.000012
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100000 times taken 1.225812
 Time taken to execute method_2  for list size 100000 times taken 0.000010
---------------------------------------------------------------------------------
(env) chandanmaruthi:sorting_tuples$ python sort_tuples.py 
Starting experiments
 Time taken to execute method_1  for list size 10 time taken 0.000025
 Time taken to execute method_2  for list size 10 times taken 0.000008
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100 times taken 0.000099
 Time taken to execute method_2  for list size 100 times taken 0.000005
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 1000 times taken 0.001055
 Time taken to execute method_2  for list size 1000 times taken 0.000010
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 10000 times taken 0.019549
 Time taken to execute method_2  for list size 10000 times taken 0.000008
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100000 times taken 1.233318
 Time taken to execute method_2  for list size 100000 times taken 0.000015
---------------------------------------------------------------------------------



```

