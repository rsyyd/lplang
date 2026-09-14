# examples/error_handling.lp — demo try/catch/throw in LPLang 1.2

# ── manual throw & catch ──
fn divide(a, b) {
    if b == 0 {
        throw "cannot divide by zero"
    }
    return a / b
}

print divide(10, 2)          # 5

try {
    print divide(10, 0)      # throws "cannot divide by zero"
} catch e {
    print "error caught: ${e}"
}

# ── catch automatic runtime errors ──
try {
    let x = undefined_variable + 1
} catch e {
    print "runtime error caught: ${e}"
}
print "program continues"

# ── try without error: catch block skipped ──
try {
    print "try block runs normally"
} catch e {
    print "will never display"
}

# ── import local .lp file ──
import "./lib_math.lp"
print "double(21) = ${double(21)}"

# ── math & time modules ──
import "math"
import "time"

print "sqrt(144) = ${math.sqrt(144)}"
print "pow(2, 8) = ${math.pow(2, 8)}"
print "floor(3.9) = ${math.floor(3.9)}  ceil(3.1) = ${math.ceil(3.1)}  round(3.5) = ${math.round(3.5)}"

let start = time.now()
time.sleep(0.1)
let end = time.now()
print "sleep 0.1s measured: ${math.round((end - start) * 1000)}ms"
print "ISO time: ${time.iso()}"

print "demo error + modules complete!"
