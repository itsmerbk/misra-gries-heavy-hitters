def heavy_hitters(stream, k):
    counters = {}
    for x in stream:
        if x in counters: counters[x] += 1
        elif len(counters) < k - 1: counters[x] = 1
        else:
            for key in list(counters):
                counters[key] -= 1
                if counters[key] == 0: del counters[key]
    return list(counters.keys())

if __name__ == "__main__":
    data = ["a"]*50 + ["b"]*40 + ["c"]*5 + ["d"]*5
    assert set(heavy_hitters(data, 3)) == {"a", "b"}
    print("[PASS] 026_misra_gries_heavy_hitters")
