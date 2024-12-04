check = (levels) => {
    sorted = levels.slice().sort()
    inc_or_dec = [sorted.slice().reverse().join(), sorted.join()].includes(levels.join())
    rules = levels.every((a, i) => {
        b = levels[i - 1]
        return i == 0 || Math.abs(a - b) >= 1 && Math.abs(a - b) <= 3
    })
    return rules && inc_or_dec
}

sum1 = sum2 = 0
process.stdin.on('data', data => {
    data.toString().trim().split('\n').map(line => line.split(' ')).forEach(levels => {
        if (check(levels)) {
            sum1 += 1
            sum2 += 1
        } else {
            sum2 += levels.some((_, i) => check(levels.slice(0, i).concat(levels.slice(i + 1))))
        }
    })
    console.log(sum1, sum2)
})

