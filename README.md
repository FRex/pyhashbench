# PyHashBench

Small script to benchmark a few hashing algorithms. Reports lowest times.

If `blake3` and `xxhash` are available they will be benchmarked as well.

```
$ python3 pyhashbench.py
1024 MiB, 3 repetitions
source         |repr                              |size      | time|        speed
---------------|----------------------------------|----------|-----|-------------
xxhash.xxh128  |<class 'xxhash.xxh3_128'>         |1024.0 MiB|0.077|13371.6 MiB/s
xxhash.xxh64   |<class 'xxhash.xxh64'>            |1024.0 MiB|0.104| 9832.9 MiB/s
xxhash.xxh32   |<class 'xxhash.xxh32'>            |1024.0 MiB|0.184| 5556.0 MiB/s
blake3.blake3  |<class 'builtins.blake3'>         |1024.0 MiB|0.363| 2819.7 MiB/s
zlib.adler32   |<built-in function adler32>       |1024.0 MiB|0.368| 2786.2 MiB/s
zlib.crc32     |<built-in function crc32>         |1024.0 MiB|0.719| 1425.2 MiB/s
hashlib.sha1   |<built-in function openssl_sha1>  |1024.0 MiB|1.219|  840.1 MiB/s
hashlib.md5    |<built-in function openssl_md5>   |1024.0 MiB|1.679|  610.0 MiB/s
hashlib.sha512 |<built-in function openssl_sha512>|1024.0 MiB|1.680|  609.6 MiB/s
hashlib.blake2b|<class '_blake2.blake2b'>         |1024.0 MiB|2.074|  493.6 MiB/s
hashlib.sha256 |<built-in function openssl_sha256>|1024.0 MiB|2.585|  396.1 MiB/s
hashlib.blake2s|<class '_blake2.blake2s'>         |1024.0 MiB|3.207|  319.3 MiB/s
Total time taken: 44.894 seconds
Version: 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)]
```
