def exe(a,b,c):
    return c(a,b)

if __name__=="__main__":
    exe([1,2,3],4,lambda x,y:max(x)+y)
    exe([1,2,3],4,lambda x,y:min(x)-y)

