with open('hello.txt', 'w') as f:
    for i in range(100):
        f.write('hello')
    f.close()
