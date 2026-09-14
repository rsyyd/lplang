# examples/features_v130.lp — demo new LPLang 1.3.0 features
# (switch, break/continue, compound assign, block comment, null-coalescing, ternary)

/* this is a block comment
   multi-line, new in v1.3.0
   will not be executed */

# ── switch ──
let score = 85
switch score {
    case 90 { print "grade A" }
    case 80 { print "grade B" }
    case 70 { print "grade C" }
    default { print "grade D" }
}

# switch on string
let color = "red"
switch color {
    case "red" { print "stop" }
    case "yellow" { print "caution" }
    case "green" { print "go" }
    default { print "broken signal" }
}

# ── compound assignment ──
let counter = 10
counter += 5
print "counter after +=5: ${counter}"
counter -= 3
print "counter after -=3: ${counter}"
counter *= 2
print "counter after *=2: ${counter}"
counter /= 4
print "counter after /=4: ${counter}"

# ── break & continue ──
let found = 0
for i in range(1, 20) {
    if i > 50 { break }
    if i % 2 != 0 { continue }   # skip odd numbers
    found += 1
}
print "even numbers 1..19: ${found}"

let steps = 0
while true {
    steps += 1
    if steps == 7 { break }
}
print "stopped at step: ${steps}"

# ── null-coalescing ──
let user_input = null
let final_name = user_input ?? "anonymous"
print "name: ${final_name}"

let already_exists = "renz"
print "name: ${already_exists ?? 'anonymous'}"

# ── ternary ──
let age = 20
let category = age >= 18 ? "adult" : "minor"
print "category: ${category}"

let num = 7
print "${num} is ${num % 2 == 0 ? 'even' : 'odd'}"

# ── range with step ──
let out = []
for i in range(0, 20, 3) {
    push(out, i)
}
print "range(0,20,3): ${join(out, ',')}"

# ── new string methods ──
let s = "lumpo"
print "starts_with(s,'lum'): ${starts_with(s, 'lum')}"
print "ends_with(s,'po'): ${ends_with(s, 'po')}"
print "repeat('ab',3): ${repeat('ab', 3)}"
print "pad_left('7',3,'0'): ${pad_left('7', 3, '0')}"
print "index_of('hello','ll'): ${index_of('hello', 'll')}"
print "index_of not found: ${index_of('hello', 'zz')}"

print "demo v1.3.0 complete!"
