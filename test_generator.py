def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data 
def main():
    g = (i+1 for i in range(5))
    for data in g:
        print(data)
        if data > 2:
            break
if __name__=="__main__":
    main()