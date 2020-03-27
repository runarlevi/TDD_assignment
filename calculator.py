class Calculator(object):
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0
        if "," in input:
            inputSplitted = input.split(",")
            return int(inputSplitted[0]) + int(inputSplitted[1])
        return int(input)