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
 Time taken to execute method_1  for list size 10 time taken 1.6664998838678002e-05
 Time taken to execute method_2  for list size 10 times taken 4.312998498789966e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100 times taken 9.017199772642925e-05
 Time taken to execute method_2  for list size 100 times taken 7.853999704821035e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 1000 times taken 0.0013307379995239899
 Time taken to execute method_2  for list size 1000 times taken 1.603900091140531e-05
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 10000 times taken 0.023338892999163363
 Time taken to execute method_2  for list size 10000 times taken 4.822999471798539e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  for list size 100000 times taken 1.2535453109994705
 Time taken to execute method_2  for list size 100000 times taken 1.3228000170784071e-05
---------------------------------------------------------------------------------


```

