maxn = 500
n = int()
g = [[0]*maxn for _ in range(maxn)]
best_cost = 1000000000
best_cut = list()

def mincut():
    v = [[] for _ in range(maxn)]
    for i in range(n):
        v[i].append(i)
    w = []
    exist = [True* maxn for _ in range(maxn)]
    in_a = []
    for ph in range (n - 1):
         for i in range(len(in_a)):
            in_a[i] = False
         for i in range(len(w)):
             w[i] = 0
         for it in range (n - ph):
             sel = -1
             for i in range (n):
                 if ((exist[i] == True) and (in_a[i] == False) and (sel == -1 or w[i] > w[sel])):
                    sel = i
             if (it == n - ph - 1):
                if (w[sel] < best_cost):
                     best_cost = w[sel]
                     best_cut = v[sel]
                v[sel - 1].insert(v[sel - 1].end(), v[sel].begin(), v[sel].end())
                for i in range (n):
                    g[sel - 1][i] += g[sel][i]
                    g[i][sel - 1] += g[sel][i]
                exist[sel] = False
             else:
                 in_a[sel] = True
                 for i in range (n):
                     w[i] += g[sel][i]









#n = int(input())
#m = '+___ '
#print(m * n)
#b = '|__\\ '
#c = '|'
#for i in range(1, n + 1):
#    print('|', i, ' /', sep='', end=' ')
#print()
#print(b * n, sep='', end=' ')
#print()
#print('    '.join(map(str, c * n)))
