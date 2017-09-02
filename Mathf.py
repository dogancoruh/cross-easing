class Mathf:
    @staticmethod
    def lerp(start, end, value):
        return (start + value * (end - start))

    @staticmethod
    def clamp01(value):
        if value < 0:
            return 0
        elif value > 1:
            return 1
        else:
            return value
