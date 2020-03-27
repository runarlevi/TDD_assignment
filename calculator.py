class Calculator(object):
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0
        return int(input)