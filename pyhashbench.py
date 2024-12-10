import collections
import hashlib
import time
import zlib
import sys

try:
    import blake3
except ImportError as e:
    print(f"Failed to import blake3: {e}", file=sys.stderr)

try:
    import xxhash
except ImportError as e:
    print(f"Failed to import xxhash: {e}", file=sys.stderr)

# NOTE: this is to force VS Code to not mark these as unused
type((zlib, blake3, xxhash, hashlib))


def format_pretty_table(origdata, rjust=()) -> str:
    data = [None if row is None else tuple(map(str, row)) for row in origdata]
    colcount = max(map(len, (row for row in data if row is not None)))
    maxlens = colcount * [0]
    for row in data:
        if row is None:
            continue
        for i, l1 in enumerate(map(len, row)):
            if l1 > maxlens[i]:
                maxlens[i] = l1
    ret = []
    for row in data:
        if row is None:
            ret.append("|".join("-" * width for width in maxlens))
        else:
            parts = []
            for i, (data, width) in enumerate(zip(row, maxlens)):
                if i in rjust:
                    parts.append(data.rjust(width))
                else:
                    parts.append(data.ljust(width))
            ret.append("|".join(parts))
    return "\n".join(ret)


Result = collections.namedtuple("Result", "source repr size time speed")


def prettify_result(r: Result) -> tuple:
    speed = f" {round(r.speed / 1024 ** 2, 1)} MiB/s"
    return (f" {r.source} ", f" {r.repr} ", f" {r.time:.3f} ", speed)


def main(megs, repetitions):
    starttime = time.time()

    # NOTE: newline for separation
    print(f"{megs} MiB, {repetitions} repetitions, best (lowest) time taken\n")
    algonames = [
        "blake3.blake3",
        "hashlib.sha1",
        "hashlib.sha256",
        "hashlib.sha512",
        "hashlib.blake2b",
        "hashlib.blake2s",
        "hashlib.md5",
        "zlib.crc32",
        "zlib.adler32",
        "xxhash.xxh128",
        "xxhash.xxh64",
        "xxhash.xxh32",
    ]

    algos = []
    for a in algonames:
        m, k = a.split(".")
        if m in sys.modules:
            algos.append((a, getattr(sys.modules[m], k)))
    data = bytes(megs * 1024 * 1024)
    results = []
    for name, algo in algos:
        times = []
        for _ in range(repetitions):
            a = time.perf_counter_ns()
            algo(data)
            b = time.perf_counter_ns()
            times.append(b - a)
        try:
            results.append(
                Result(
                    name,
                    repr(algo),
                    len(data),
                    min(times) / 10**9,
                    10**9 * len(data) / min(times),
                )
            )
        except ZeroDivisionError as err:
            print(name, err, file=sys.stderr)
            # results.append(Result(name, repr(algo), len(data), min(times), math.inf))

    results = sorted(results, key=lambda r: r.time)
    results = list(map(prettify_result, results))
    results = [(" Algorithm ", " Repr ", " Time ", " Speed "), None] + results
    print(format_pretty_table(results, rjust=(2, 3)))  # 2, 3 = Time and Speed

    # NOTE: newline for separation
    print(f"\nTotal time taken: {time.time() - starttime:.3f} seconds")


if __name__ == "__main__":
    print(f"Version: {sys.version}\n")  # NOTE: newline for separation
    main(1024, 3)
