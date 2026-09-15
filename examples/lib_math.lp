# lib_math.lp - local library imported by other examples (.lp)
# called via: import "./lib_math.lp"

fn double(n) {
    return n * 2
}

fn square(n) {
    return n * n
}

const PHI = 1.618
let VERSION = "lib_math-1.0"

print "lib_math loaded (this stdout only appears when executed directly)"
