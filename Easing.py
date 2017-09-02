import math

from easing import Mathf


class Easing:
    NATURAL_LOG_OF_2 = 0.693147181

    @staticmethod
    def linear(start, end, value):
        return Mathf.lerp(start, end, value)

    @staticmethod
    def spring(start, end, value):
        value_ = Mathf.clamp01(value)
        value_ = (math.sin(value_ * math.pi * (0.2 + 2.5 * value_ * value_ * value_)) * math.pow(1 - value_, 2.2) + value_) * (1 + (1.2 * (1 - value_)))
        return start + (end - start) * value_

    @staticmethod
    def easeinquad(start, end, value):
        end_ = end - start
        return end_ * value * value + start

    @staticmethod
    def easeoutquad(start, end, value):
        end_ = end - start
        return -end_ * value * (value - 2) + start

    @staticmethod
    def easeinoutquad(start, end, value):
        value_ = value / 0.5
        end_ = end - start

        if value_ < 1:
            return end_ * 0.5 * value_ * value_ + start

        value_ = value_ - 1
        return -end_ * 0.5 * (value_ * (value_ - 2) - 1) + start

    @staticmethod
    def easeincubic(start, end, value):
        end_ = end - start
        return end_ * value * value * value + start

    @staticmethod
    def easeoutcubic(start, end, value):
        value_ = value - 1
        end_ = end - start
        return end_ * (value_ * value_ * value_ + 1) + start

    @staticmethod
    def easeinoutcubic(start, end, value):
        value_ = value / 0.5
        end_ = end - start

        if value_ < 1:
            return end_ * 0.5 * value_ * value_ * value_ + start

        value_ = value_ - 2
        return end_ * 0.5 * (value_ * value_ * value_ + 2) + start

    @staticmethod
    def easeinquart(start, end, value):
        end_ = end - start
        return end_ * value * value * value * value + start

    @staticmethod
    def easeoutquart(start, end, value):
        value_ = value - 1
        end_ = end - start
        return -end_ * (value_ * value_ * value_ * value_ - 1) + start

    @staticmethod
    def easeinoutquart(start, end, value):
        value_ = value / 0.5
        end_ = end - start

        if value_ < 1:
            return end_ * 0.5 * value_ * value_ * value_ * value_ + start

        value_ = value_ - 2
        return -end_ * 0.5 * (value_ * value_ * value_ * value_ - 2) + start

    @staticmethod
    def easeinquint(start, end, value):
        end_ = end - start
        return end_ * value * value * value * value * value + start

    @staticmethod
    def easeoutquint(start, end, value):
        value_ = value - 1
        end_ = end - start
        return end_ * (value_ * value_ * value_ * value_ * value_ + 1) + start

    @staticmethod
    def easeinoutquint(start, end, value):
        value_ = value / 0.5
        end_ = end - start

        if value_ < 1:
            return end_ * 0.5 * value_ * value_ * value_ * value_ * value_ + start

        value_ = value_ - 2
        return end_ * 0.5 * (value_ * value_ * value_ * value_ * value_ + 2) + start

    @staticmethod
    def easeinsine(start, end, value):
        end_ = end - start
        return -end_ * math.cos(value * (math.pi * 0.5)) + end_ + start

    @staticmethod
    def easeoutsine(start, end, value):
        end_ = end - start
        return end_ * math.sin(value * (math.pi * 0.5)) + start

    @staticmethod
    def easeinoutsine(start, end, value):
        end_ = end - start
        return -end_ * 0.5 * (math.cos(math.pi * value) - 1) + start

    @staticmethod
    def easeinexpo(start, end, value):
        end_ = end - start
        return end_ * math.pow(2, 10 * (value - 1)) + start

    @staticmethod
    def easeoutexpo(start, end, value):
        end_ = end - start
        return end_ * (-math.pow(2, -10 * value) + 1) + start

    @staticmethod
    def easeinoutexpo(start, end, value):
        value_ = value / 0.5
        end_ = end - start

        if value_ < 1:
            return end_ * 0.5 * math.pow(2, 10 * (value_ - 1)) + start

        value_ = value_ - 1
        return end_ * 0.5 * (-math.pow(2, -10 * value_) + 2) + start

    @staticmethod
    def easeincirc(start, end, value):
        end_ = end - start
        return -end_ * (math.sqrt(1 - value * value) - 1) + start

    @staticmethod
    def easeoutcirc(start, end, value):
        value_ = value - 1
        end_ = end - start
        return end_ * math.sqrt(1 - value_ * value_) + start

    @staticmethod
    def easeinoutcirc(start, end, value):
        value_ = value / 0.5
        end_ = end - start

        if value_ < 1:
            return -end_ * 0.5 * (math.sqrt(1 - value_ * value_) - 1) + start

        value_ = value_ - 2
        return end_ * 0.5 * (math.sqrt(1 - value_ * value_) + 1) + start

    @staticmethod
    def easeinbounce(start, end, value):
        end_ = end - start
        d = 1.0
        return end_ - Easing.easeoutbounce(0, end_, d - value) + start

    @staticmethod
    def easeoutbounce(start, end, value):
        value_ = value / 1.0
        end_ = end - start

        if value_ < (1 / 2.75):
            return end_ * (7.5625 * value_ * value_) + start
        elif value_ < (2 / 2.75):
            value_ = value_ - (1.5 / 2.75)
            return end_ * (7.5625 * value_ * value_ + .75) + start
        elif value_ < (2.5 / 2.75):
            value_ = value_ - (2.25 / 2.75)
            return end_ * (7.5625 * value_ * value_ + .9375) + start
        else:
            value_ = value_ - (2.625 / 2.75)
            return end_ * (7.5625 * value_ * value_ + .984375) + start

    @staticmethod
    def easeinoutbounce(start, end, value):
        end_ = end - start
        d = 1.0
        if value < d * 0.5:
            return Easing.easeinbounce(0, end_, value * 2) * 0.5 + start
        else:
            return Easing.easeoutbounce(0, end_, value * 2 - d) * 0.5 + end_ * 0.5 + start

    @staticmethod
    def easeinback(start, end, value):
        end_ = end - start
        value_ = value / 1.0
        s = 1.70158
        return end_ * value_ * value_ * ((s + 1) * value_ - s) + start

    @staticmethod
    def easeoutback(start, end, value):
        s = 1.70158
        end_ = end - start
        value_ = value - 1
        return end_ * (value_ * value_ * ((s + 1) * value_ + s) + 1) + start

    @staticmethod
    def easeinoutback(start, end, value):
        s = 1.70158
        end_ = end - start
        value_ = value / 0.5
        if value_ < 1:
            s = s * 1.525
            return end_ * 0.5 * (value_ * value_ * ((s + 1) * value_ - s)) + start
        value_ = value_ - 2
        s = s * 1.525
        return end_ * 0.5 * (value_ * value_ * ((s + 1) * value_ + s) + 2) + start

    @staticmethod
    def easeinelastic(start, end, value):
        end_ = end - start
        d = 1.0
        p = d * 0.3
        s = 0.0
        a = 0.0

        if value == 0:
            return start

        if (value / d) == 1:  # value /= d (what da f*ck?!?)
            return start + end_

        if a == 0 or a < math.fabs(end_):
            a = end
            s = p / 4
        else:
            s = p / (2 * math.pi) * math.asin(end_ / a)

        return -(a * math.pow(2, 10 * (value - 1)) * math.sin((value * d - s) * (2 * math.pi) / p)) + start  # value -= 1 what???!?!?

    @staticmethod
    def easeoutelastic(start, end, value):
        end_ = end - start
        d = 1.0
        p = d * 0.3
        s = 0.0
        a = 0.0

        if value == 0:
            return start

        if (value / d) == 1:
            return start + end_

        if a == 0 or a < math.fabs(end_):
            a = end_
            s = p * 0.25
        else:
            s = p / (2 * math.pi) * math.asin(end_ / a)

        return a * math.pow(2, -10 * value) * math.sin((value * d - s) * (2 * math.pi) / p) + end_ + start

    @staticmethod
    def easeinoutelastic(start, end, value):
        end_ = end - start
        d = 1.0
        p = d * 0.3
        s = 0.0
        a = 0.0

        if value == 0:
            return start

        if (value / d * 0.5) == 2:
            return start + end_

        if a == 0 or a < math.fabs(end_):
            a = end_
            s = p / 4
        else:
            s = p / (2 * math.pi) * math.asin(end_ / a)

        if value < 1:
            return -0.5 * (a * math.pow(2, 10 * (value - 1)) * math.sin((value * d - s) * (2 * math.pi) / p)) + start

        return a * math.pow(2, -10 * (value - 1)) * math.sin((value * d - s) * (2 * math.pi) / p) * 0.5 + end_ + start
