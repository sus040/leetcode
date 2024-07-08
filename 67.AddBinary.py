class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum_value = 0
        for i in range(len(a)-1, -1, -1):
            for j in range(len(b)-1, -1, -1):
                if int(a[i]) + int(b[j]) == 10:
                    sum_value = int(a[i]) + int(b[j])
                    print(f"Partial sum at a[{i}] + b[{j}]: {sum_value}")
