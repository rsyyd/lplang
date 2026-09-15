# examples/language_features.lp - demo core LPLang 1.2 features
# (variables, functions, string interpolation, collections, functional builtins)

# ── variables & basic types ──
let name = "renz"
let age = 25
let height = 1.75
let active = true
let empty_data = null

print "hello ${name}, age ${age}, height ${height}m, active=${active}, empty=${empty_data}"

# ── list & map ──
let fruits = ["apple", "banana", "mango"]
push(fruits, "durian")
print "fruits: ${join(fruits, ', ')} (${len(fruits)} items)"

let config = {host: "localhost", port: 8080, debug: true}
print "host=${config.host} port=${config.port}"

# ── functions ──
fn add(a, b) {
    return a + b
}
fn factorial(n) {
    if n <= 1 { return 1 }
    return n * factorial(n - 1)
}
print "5! = ${factorial(5)}"
print "10 + 32 = ${add(10, 32)}"

# ── control flow ──
let score = 87
if score >= 90 {
    print "grade: A"
} else if score >= 75 {
    print "grade: B"
} else {
    print "grade: C"
}

let total = 0
for i in range(1, 11) {
    total = total + i
}
print "sum 1..10 = ${total}"

let n = 5
while n > 0 {
    print "countdown: ${n}"
    n = n - 1
}

# ── functional builtins ──
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let evens = filter(numbers, fn(x) { return x % 2 == 0 })
print "evens: ${join(evens, ',')}"

let squares = map(numbers, fn(x) { return x * x })
print "squares: ${join(squares, ',')}"

let total_sum = reduce(numbers, fn(acc, x) { return acc + x }, 0)
print "sum of all = ${total_sum}"

let first_match = find(numbers, fn(x) { return x > 5 })
print "first number > 5: ${first_match}"

print "any > 9? ${any(numbers, fn(x) { return x > 9 })}"
print "all > 0? ${all(numbers, fn(x) { return x > 0 })}"

# ── string methods ──
let message = "  Lumpo is AWESOME  "
print "upper: ${upper(trim(message))}"
print "lower: ${lower(trim(message))}"
print "replace: ${replace(message, 'AWESOME', 'GREAT')}"
print "substr(0,5): ${substr(trim(message), 0, 5)}"
print "contains 'AWESOME': ${contains(trim(message), 'AWESOME')}"

print "demo complete!"
