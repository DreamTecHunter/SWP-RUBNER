def do(lambda_expression, l: list):
    for i in range(len(l)):
        l[i] = lambda_expression(l[i])
    return l


if __name__ == "__main__":
    l = [i for i in range(-100, 100, 10)]
    print(l)
    do(lambda_expression=lambda a: a + 2, l=l)
    print(l)