class MathSamples:

    @staticmethod
    def factorial(n):
        if n <= 2:
            return n
        else:
            return n * MathSamples.factorial(n - 1)