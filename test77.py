def fn(n=4,k=2):
    l = []


def fo(i=1,j=4,k=2):
    for n in range(i,j):
        if k != 0:
            fo(n+1,j,k-1)
        yield n
if __name__ == '__main__':
    print(list(fo()))
