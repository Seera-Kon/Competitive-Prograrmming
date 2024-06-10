class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        if len(num) <= 2:
            return False
        
        def fun(i,part):

            if i == len(num):

                if len(part) < 3:
                    return False

                j, k = 0, 1

                while k+1 < len(part):

                    if part[j] + part[k] != part[k+1]:
                        return False

                    j += 1
                    k += 1

                print(part)
                return True

            for j in range(i,len(num)):

                string = num[i:j+1]

                if len(string) > 1 and string[0] == '0':
                    continue

                val = int(string)

                part.append(val)
                if fun(j+1,part):
                    return True
                part.pop()

        return fun(0,[])
            

