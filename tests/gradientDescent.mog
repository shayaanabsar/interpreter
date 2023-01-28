xData = [5, 2, 3]
yData = [20, 8, 12]

weight = -1020
LFACTOR = 0.0001

while (True) {
    i = 0

    loss = 0

    lossDiff = 0

    diff = 0.000000001

    while (i < 3) {
        estimate = xData[i] * weight
        loss = loss + ((estimate - yData[i]) * (estimate - yData[i]))

        estimate = xData[i] * (weight + diff)

        lossDiff = lossDiff + ((estimate - yData[i]) * (estimate - yData[i]))

        i = i + 1
    }

    gradient = (lossDiff - loss) / diff
    weight = weight + (LFACTOR * -gradient)

    stdout weight
}
