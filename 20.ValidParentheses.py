class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Set an empty list 
        list = []
        # Set a dictionary to map open brackets to close bracket
        dic = { ')' : '(',
                '}' : '{',
                ']' : '['}
        # Iterate through string 
        for char in s:
            # Check if the character is open bracket 
            if char in dic.values():
            # Add in the empty bracket
                list.append(char)
            # Check the close bracket
            elif char in dic.keys():
                # Pop can remove the lastest string in the list
                if list == [] or dic[char] != list.pop():
                    # Return false if list is empty or no mapping bracket
                    return False
            # Return false if it is no braket
            else:   
               return False
        # Return TRUE if stack is empty
        # This means all the brackets are mapped each other accordingly.
        return list == []
