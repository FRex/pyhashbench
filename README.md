# PyHashBench

Small script to benchmark a few hashing algorithms. Reports lowest times.

If [blake3](https://pypi.org/project/blake3/) and [xxhash](https://pypi.org/project/xxhash/)
are available they will be benchmarked as well.

Requires (and works on any) Python 3.6 or above, as tested using
[https://github.com/FRex/anypython](https://github.com/FRex/anypython),
due to usage of [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).

Example output:

```
$ python3 pyhashbench.py
Version: 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)]

1024 MiB, 3 repetitions, best (lowest) time taken

 Algorithm       | Repr                               |  Time |        Speed
-----------------|------------------------------------|-------|--------------
 xxhash.xxh128   | <class 'xxhash.xxh3_128'>          | 0.072 | 14198.5 MiB/s
 xxhash.xxh64    | <class 'xxhash.xxh64'>             | 0.096 | 10670.4 MiB/s
 xxhash.xxh32    | <class 'xxhash.xxh32'>             | 0.157 |  6536.8 MiB/s
 blake3.blake3   | <class 'blake3.blake3.blake3'>     | 0.276 |  3711.4 MiB/s
 zlib.adler32    | <built-in function adler32>        | 0.276 |  3711.3 MiB/s
 zlib.crc32      | <built-in function crc32>          | 0.468 |  2190.0 MiB/s
 hashlib.sha1    | <built-in function openssl_sha1>   | 0.503 |  2034.1 MiB/s
 hashlib.sha256  | <built-in function openssl_sha256> | 0.541 |  1892.8 MiB/s
 hashlib.sha512  | <built-in function openssl_sha512> | 1.333 |   768.2 MiB/s
 hashlib.blake2b | <class '_blake2.blake2b'>          | 1.511 |   677.6 MiB/s
 hashlib.md5     | <built-in function openssl_md5>    | 1.623 |   631.0 MiB/s
 hashlib.blake2s | <class '_blake2.blake2s'>          | 2.457 |   416.8 MiB/s

Total time taken: 30.590 seconds
```

Example output with 32 bit Python 3.6 (noticeably slower and without third party hashes):

```
$ anypython 3.6 pyhashbench.py
Failed to import blake3: No module named 'blake3'
Failed to import xxhash: No module named 'xxhash'
Version: 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)]

1024 MiB, 3 repetitions, best (lowest) time taken

 Algorithm       | Repr                               |  Time |       Speed
-----------------|------------------------------------|-------|-------------
 zlib.adler32    | <built-in function adler32>        | 0.270 | 3789.9 MiB/s
 hashlib.sha1    | <built-in function openssl_sha1>   | 0.495 | 2069.2 MiB/s
 hashlib.sha256  | <built-in function openssl_sha256> | 0.543 | 1886.6 MiB/s
 zlib.crc32      | <built-in function crc32>          | 0.708 | 1445.7 MiB/s
 hashlib.md5     | <built-in function openssl_md5>    | 1.262 |  811.3 MiB/s
 hashlib.blake2s | <class '_blake2.blake2s'>          | 2.550 |  401.5 MiB/s
 hashlib.sha512  | <built-in function openssl_sha512> | 3.463 |  295.7 MiB/s
 hashlib.blake2b | <class '_blake2.blake2b'>          | 3.976 |  257.6 MiB/s

Total time taken: 40.046 seconds
```
