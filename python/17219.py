import sys

input = sys.stdin.readline

n ,m = map(int, input().split())
password_note = dict()
for _ in range(n):
    domain, passwd = input().split()
    # print(domain, passwd)
    password_note[domain] = passwd
# print(password_note['startlink.io'])

for _ in range(m):
    domain = input().strip()
    print(password_note[domain])
