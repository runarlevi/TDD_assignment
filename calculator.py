class Calculator(object):
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0

        if "," in input and "\n" not in input:
            inputSplitted = input.split(",")
            return sum([int(i) for i in inputSplitted])

        if "\n" in input:
            input = input.replace("\n", ",")
            inputSplitted = input.split(",")
            return sum([int(i) for i in inputSplitted])
        
        return int(input)