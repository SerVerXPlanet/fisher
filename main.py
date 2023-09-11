def main():
    r = 'R'
    n = 'N'
    b = 'B'
    q = 'Q'
    k = 'K'

    ff = [r, n, b, q, k, b, n, r]

    positions = set()

    for i1 in range(8):
        for i2 in range(8):
            if i2 not in (i1,):
                for i3 in range(8):
                    if i3 not in (i1, i2):
                        for i4 in range(8):
                            if i4 not in (i1, i2, i3):
                                for i5 in range(8):
                                    if i5 not in (i1, i2, i3, i4):
                                        for i6 in range(8):
                                            if i6 not in (i1, i2, i3, i4, i5):
                                                for i7 in range(8):
                                                    if i7 not in (i1, i2, i3, i4, i5, i6):
                                                        for i8 in range(8):
                                                            if i8 not in (i1, i2, i3, i4, i5, i6, i7):

                                                                setup = (ff[i1], ff[i2], ff[i3], ff[i4],
                                                                         ff[i5], ff[i6], ff[i7], ff[i8])

                                                                pos_b1 = setup.index(b)
                                                                pos_b2 = setup.index(b, pos_b1 + 1)

                                                                if (pos_b1 - pos_b2) % 2 == 0:
                                                                    continue

                                                                pos_k = setup.index(k)
                                                                pos_r1 = setup.index(r)
                                                                pos_r2 = setup.index(r, pos_r1 + 1)

                                                                if not (pos_r1 < pos_k < pos_r2
                                                                        or pos_r2 < pos_k < pos_r1):
                                                                    continue

                                                                print(''.join(setup))
                                                                positions.add(setup)

    print(f'count = {len(positions)}')


if __name__ == '__main__':
    main()
