 def middle(self, a, b, c):
        #code here
        if((a>b and a<c) or (a<b and a>c)):
            return a
        elif((b>a and b<c) or (b<a and b>c)):
            return b
        elif((c>a and c<b) or (c<a and c>b)):
            return c
