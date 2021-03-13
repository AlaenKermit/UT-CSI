def torm(x):
    kilomeetritekstunnis = x * 3.6
    if kilomeetritekstunnis >= 63:
        return "on torm"
        print("=======LÕPP=======")
    else:
        return "pole tormi"
        
print(torm(155.4))