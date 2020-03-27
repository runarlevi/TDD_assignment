class Error(Exception):
    pass

class Calculator(object):
    @staticmethod
    def Add(input: str) -> int:
        if input == "":
            return 0

        if "-" in input:
            errorStr = "Negative numbers not allowed: "
            inputSplitted = input.split(",")
            for index, num in enumerate(inputSplitted):
                if "-" in num:
                    errorStr += inputSplitted[index] + ", "
                    errorStr = errorStr[:-2]
            raise Error(errorStr)

        if "," in input and "\n" not in input:
            inputSplitted = input.split(",")
            if all(int(i) <= 1000 for i in inputSplitted):
                return sum([int(i) for i in inputSplitted])
            for index, num in enumerate(inputSplitted):
                if int(num) > 1000:
                    inputSplitted.pop(index)
            return sum([int(i) for i in inputSplitted])

        if "\n" in input:
            input = input.replace("\n", ",")
            inputSplitted = input.split(",")
            if all(int(i) <= 1000 for i in inputSplitted):
                return sum([int(i) for i in inputSplitted])
            for index, num in enumerate(inputSplitted):
                if int(num) > 1000:
                    inputSplitted.pop(index)
            return sum([int(i) for i in inputSplitted])

        return int(input)