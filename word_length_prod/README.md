# Word Length Product

“Of the pairs of words in the dictionary that have no letters in common, find one that maximizes the product of the words' lengths.”

[How do you elaborate the question to candidates?]
After giving the problem statement, I give an example. I’ll write a sample dictionary on the board, like:

cat
dog
feed
pull
space

And give a few examples:
cat and dog share no letters, and have a product of 3*3 = 9
space and dog share no letters, and have a product of 15
space does not work with either feed (e) or pull (p)
feed and pull is the best answer for this dictionary (4*4 = 16)

The dictionary will only contain lower case letters (a-z)


#### Python

output:
```
$ python3 ./main.py
306 , 18 , 17 , chromochalcography , uninquisitiveness
```
```
$ hyperfine 'python3 word_length_prod/py/main.py'
```
```
Benchmark #1: python3 word_length_prod/py/main.py
  Time (mean ± σ):      4.302 s ±  0.322 s    [User: 4.178 s, System: 0.101 s]
  Range (min … max):    3.793 s …  4.691 s    10 runs
```

#### Rust

output:
```
$ ./target/release/rust
prod 306
len1 18
len2 17
word1 "chromochalcography"
word2 "uninquisitiveness"
```
profile:
```
$ hyperfine ./target/release/rust
```
```
Benchmark #1: ./target/release/rust
  Time (mean ± σ):     476.4 ms ±  19.2 ms    [User: 453.5 ms, System: 18.2 ms]
  Range (min … max):   451.1 ms … 505.7 ms    10 runs
```