def solve_towers(n,_from, _to, _spare):
    if n>0:
        solve_towers(n-1,_from, _spare, _to)
        print(f"{n}번 원반을 {_from}에서 {_to}로 옮김")
        solve_towers(n-1,_spare, _to, _from)


n =3
solve_towers(n, 'from', 'to', 'spare')