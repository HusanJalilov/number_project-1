class Number:
    def __init__(self, value):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value%2!=0

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value%2==0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        num=self.value
        ans = False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    ans = True
                    break
        return ans
        

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        num=self.value

        s=1
        m=[]
        while num!=s:
            if num%s==0:
                m.append(s)
            s+=1
        print(m)

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(self.value)

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        num=self.value
        s=0
        while num!=0:
            s+=num%10
            num=num//10
        return s
        

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        num = self.value
        return int(str(num)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        str=self.value
        for i in range(0, len(str)//2):
            if str[i] != str[len(str)-i-1]:
                return False
           
        # If the above loop doesn't
        #return then it is palindrome
        return True

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        s=[int(i) for i in str(self.value)]
        return s
        
    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        s=[int(i) for i in str(self.value)]
        return max(s)

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        s=[int(i) for i in str(self.value)]
        return min(s)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        s=[int(i) for i in str(self.value)]
        return sum(s)/len(s)

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(3)