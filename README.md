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
 Time taken to execute method_1  10 times is 1.763099862728268e-05
 Time taken to execute method_2  10 times is 4.247001925250515e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  100 times is 5.059999239165336e-06
 Time taken to execute method_2  100 times is 3.6860001273453236e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  1000 times is 8.00400084699504e-06
 Time taken to execute method_2  1000 times is 5.771998985437676e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  10000 times is 4.0186998376157135e-05
 Time taken to execute method_2  10000 times is 7.999002264114097e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  100000 times is 1.0104999091709033e-05
 Time taken to execute method_2  100000 times is 5.53599966224283e-06
---------------------------------------------------------------------------------
 Time taken to execute method_1  1000000 times is 9.362000128021464e-06
 Time taken to execute method_2  1000000 times is 5.178000719752163e-06
---------------------------------------------------------------------------------
```

