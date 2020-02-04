class Addition:

    @staticmethod
    def sum(augend, addend):
        return augend + addend

    @staticmethod
    def sum(valueList):
        result = 0
        for value in valueList:
            result = Addition.sum(result, value)

        return result
