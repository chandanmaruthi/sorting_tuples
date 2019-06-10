# sorting_tuples

## Method 1: 
Uses in-built list sort and then merge 
## Method 2: 
Does not sort but swaps or merges in place.

## Findings
Method 2 seems to be better on larger lists. Although the performance improvement is not always guaranteed. Also, there is an intermittent bug somewhere, but it did not want to take more time. 

## Code 
``` https://github.com/chandanmaruthi/sorting_tuples ```

## Results
```
Starting experiments
 Time taken to execute method_1  for list size 10 time taken 1.5382000128738582e-05
 Time taken to execute method_2  for list size 10 times taken 4.479999915929511e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100 times taken 4.80900052934885e-06
 Time taken to execute method_2  for list size 100 times taken 3.887998900609091e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 1000 times taken 9.991999831981957e-06
 Time taken to execute method_2  for list size 1000 times taken 2.1895000827498734e-05
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 10000 times taken 7.123999239411205e-06
 Time taken to execute method_2  for list size 10000 times taken 4.231002094456926e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100000 times taken 7.0690002758055925e-06
 Time taken to execute method_2  for list size 100000 times taken 4.2050014599226415e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 1000000 times taken 7.31000181986019e-06
 Time taken to execute method_2  for list size 1000000 times taken 4.158999217906967e-06
---------------------------------------------------------------------------------

```

