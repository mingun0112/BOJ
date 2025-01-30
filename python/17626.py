    import sys
    import math

    input = sys.stdin.readline

    def foursquare(n):
        # n이 완전 제곱수인 경우
        if int(math.sqrt(n)) ** 2 == n:
            return 1

        # n이 두 개의 제곱수 합으로 표현되는 경우
        for i in range(1, int(math.sqrt(n)) + 1):
            if int(math.sqrt(n - i ** 2)) ** 2 == n - i ** 2:
                return 2

        # n이 세 개의 제곱수 합으로 표현되는 경우
        for i in range(1, int(math.sqrt(n)) + 1):
            for j in range(1, int(math.sqrt(n - i ** 2)) + 1):
                if int(math.sqrt(n - i ** 2 - j ** 2)) ** 2 == n - i ** 2 - j ** 2:
                    return 3

        # n이 네 개의 제곱수 합으로 표현되는 경우
        return 4

    n = int(input())
    print(foursquare(n))