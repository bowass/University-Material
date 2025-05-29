def to(p, q):
    return (not p) or q

for i in range(2):
    for j in range(2):
        for k in range(2):
            p, q, r = bool(i), bool(j), bool(k)
            lhs = to(q, (r and (not p)))
            rhs = to(r, to(p, q))
            if lhs != rhs:
                print(f"different: p={p}, q={q}, r={r}")
                exit(0)

print("ok")

