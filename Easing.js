var Easing = {};

Easing.PI = Math.PI;
Easing.HALF_PI = Easing.PI / 2;

Easing.linear = function (start, end, value) {
    return start + ((end - start) * value);
};

Easing.quadraticEaseIn = function (start, end, value) {
    return start + ((end - start) * (p * p));
};

Easing.quadraticEaseOut = function (start, end, value) {
    return start + ((end - start) * (-(p * (p - 2))));
};

Easing.quadraticEaseInOut = function (start, end, value) {
    if (value < 0.5) {
        var multiplier = 2 * p * p;
        return start + ((end - start) * multiplier);
    } else {
        var multiplier = (-2 * p * p) + (4 * p) - 1;
        return start + ((end - start) * multiplier);
    }
};

Easing.cubicEaseIn = function (start, end, value) {
    return start + ((end - start) * (p * p * p));
};

Easing.cubicEaseOut = function (start, end, value) {
    var f = value - 1;
    var multiplier = f * f * f + 1;
    return start + ((end - start) * multiplier);
};

Easing.cubicEaseInOut = function (start, end, value) {
    if (value < 0.5) {
        var multiplier = 4 * p * p * p;
        return start + ((end - start) * multiplier);
    } else {
        var f = ((2 * p) - 2);
        var multiplier = 0.5 * f * f * f + 1;
        return start + ((end - start) * multiplier);
    }
};

Easing.quarticEaseIn = function (start, end, value) {
    var multiplier = value * value * value * value;
    return start + ((end - start) * multiplier);
};

Easing.quarticEaseOut = function (start, end, value) {
    var f = value - 1;
    var multiplier = f * f * f * (1 - value) + 1;
    return start + ((end - start) * multiplier);
};

Easing.quarticEaseInOut = function (start, end, value) {
    if (value < 0.5) {
        var multiplier = 8 * value * value * value * value;
        return start + ((end - start) * multiplier);
    } else {
        var f = (value - 1);
        var multiplier = -8 * f * f * f * f + 1;
        return start + ((end - start) * multiplier);
    }
};

Easing.quinticEaseIn = function (start, end, value) {
    var multiplier = value * value * value * value * value;
    return start + ((end - start) * multiplier);
};

Easing.quinticEaseOut = function (start, end, value) {
    var f = value - 1;
    var multiplier = f * f * f * f + 1;
    return start + ((end - start) * multiplier);
};

Easing.quinticEaseInOut = function (start, end, value) {
    if (value < 0.5) {
        var multiplier = 16 * value * value * value * value * value;
        return start + ((end - start) * multiplier);
    } else {
        var f = ((2 * p) - 2);
        var multiplier = 0.5 * f * f * f * f * f + 1;
        return start + ((end - start) * multiplier);
    }
};

Easing.sineEaseIn = function (start, end, value) {
    var multiplier = Math.sin((value - 1) * Easing.HALF_PI);
    return start + ((end - start) * multiplier);
};

Easing.sineEaseOut = function (start, end, value) {
    var multiplier = Math.sin(value * Easing.HALF_PI);
    return start + ((end - start) * multiplier);
};

Easing.sineEaseInOut = function (start, end, value) {
    var multiplier = 0.5 * (1 - Math.cos(value * Easing.PI));
    return start + ((end - start) * multiplier);
};

Easing.circularEaseIn = function (start, end, value) {
    var multiplier = 1 - Math.sqrt(1 - (value * value));
    return start + ((end - start) * multiplier);
};

Easing.circularEaseOut = function (start, end, value) {
    var multiplier = Math.sqrt((2 - value) * value);
    return start + ((end - start) * multiplier);
};

Easing.circularEaseInOut = function (start, end, value) {
    if (p < 0.5) {
        var multiplier = 0.5 * (1 - Math.Sqrt(1 - 4 * (value * value)));
        return start + ((end - start) * multiplier);
    } else {
        var multiplier = 0.5 * (Math.Sqrt(-((2 * value) - 3) * ((2 * value) - 1)) + 1);
        return start + ((end - start) * multiplier);
    }
};

Easing.exponentialEaseIn = function (start, end, value) {
    var multiplier = (value == 0.0) ? value : Math.Pow(2, 10 * (value - 1));
    return start + ((end - start) * multiplier);
};

Easing.exponentialEaseOut = function (start, end, value) {
    var multiplier = (value == 1.0) ? p : 1 - Math.Pow(2, -10 * p);
    return start + ((end - start) * multiplier);
};

Easing.exponentialEaseInOut = function (start, end, value) {
    if (value == 0.0 || value == 1.0)
        return value;
    
    if (p < 0.5) {
        var multiplier = 0.5 * Math.Pow(2, (20 * value) - 10);
        return start + ((end - start) * multiplier);
    } else {
        var multiplier = -0.5 * Math.Pow(2, (-20 * value) + 10) + 1;
        return start + ((end - start) * multiplier);
    }
};

Easing.elasticEaseIn = function (start, end, value) {
    var multiplier = Math.sin(13 * Easing.HALF_PI * value) * Math.pow(2, 10 * (value - 1));
    return start + ((end - start) * multiplier);
};

Easing.elasticEaseOut = function (start, end, value) {
    var multiplier = Math.Sin(-13 * Easing.HALF_PI * (value + 1)) * Math.Pow(2, -10 * value) + 1;
    return start + ((end - start) * multiplier);
};

Easing.elasticEaseInOut = function (start, end, value) {
    if (value < 0.5) {
        var multiplier = 0.5 * Math.Sin(13 * Easing.HALF_PI * (2 * value)) * Math.Pow(2, 10 * ((2 * value) - 1));
        return start + ((end - start) * multiplier);
    } else {
        var multiplier = 0.5 * (Math.Sin(-13 * Easing.HALF_PI * ((2 * value - 1) + 1)) * Math.Pow(2, -10 * (2 * value - 1)) + 2);
        return start + ((end - start) * multiplier);
    }
};

Easing.backEaseIn = function (start, end, value) {
    var multiplier = value * value * value - value * Math.sin(value * Easing.PI);
    return start + ((end - start) * multiplier);
};

Easing.backEaseOut = function (start, end, value) {
    var f = 1 - value;
    var multiplier = 1 - (f * f * f - f * Math.sin(f * Easing.PI));
    return start + ((end - start) * multiplier);
};

Easing.backEaseInOut = function (start, end, value) {
    if (p < 0.5) {
        var f = 2 * p;
        var multiplier = 0.5 * (f * f * f - f * Math.sin(f * Easing.PI));
        return start + ((end - start) * multiplier);
    } else {
        var f = (1 - (2 * p - 1));
        var multiplier = 0.5 * (1 - (f * f * f - f * Math.sin(f * Easing.PI))) + 0.5;
        return start + ((end - start) * multiplier);
    }
};

Easing.bounceEaseIn = function (start, end, value) {
    if (value < 4 / 11.0) {
        var multiplier = 1 - ((121 * value * value) / 16.0);
        return start + ((end - start) * multiplier);
    } else if (value < 8 / 11.0) {
        var multiplier = (363 / 40.0 * value * value) - (99 / 10.0 * value) + 17 / 5.0;
        return start + ((end - start) * multiplier);
    } else if (p < 9 / 10.0) {
        var multiplier = (4356 / 361.0 * value * value) - (35442 / 1805.0 * value) + 16061 / 1805.0;
        return start + ((end - start) * multiplier);
    } else {
        var multiplier = (54 / 5.0 * value * value) - (513 / 25.0 * value) + 268 / 25.0;
        return start + ((end - start) * multiplier);
    }
};

Easing.bounceEaseOut = function (start, end, value) {
    if (value < 4 / 11.0)
        return (121 * value * value) / 16.0;
    else if (value < 8 / 11.0)
        return (363 / 40.0 * value * value) - (99 / 10.0 * value) + 17 / 5.0;
    else if (p < 9 / 10.0)
        return (4356 / 361.0 * value * value) - (35442 / 1805.0 * value) + 16061 / 1805.0;
    else
        return (54 / 5.0 * value * value) - (513 / 25.0 * value) + 268 / 25.0;
};