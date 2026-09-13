# examples/error_handling.lp — demo try/catch/throw di LPLang 1.2

# ── throw & catch manual ──
fn bagi(a, b) {
    if b == 0 {
        throw "tidak bisa bagi dengan nol"
    }
    return a / b
}

print bagi(10, 2)          # 5

try {
    print bagi(10, 0)      # throw "tidak bisa bagi dengan nol"
} catch e {
    print "error tertangkap: ${e}"
}

# ── catch error runtime otomatis ──
try {
    let x = variabel_tidak_ada + 1
} catch e {
    print "runtime error tertangkap: ${e}"
}
print "program tetap lanjut"

# ── try tanpa error: blok catch di-skip ──
try {
    print "blok try jalan normal"
} catch e {
    print "tidak akan pernah tampil"
}

# ── import file lokal .lp ──
import "./lib_math.lp"
print "double(21) = ${double(21)}"

# ── math & time module ──
import "math"
import "time"

print "sqrt(144) = ${math.sqrt(144)}"
print "pow(2, 8) = ${math.pow(2, 8)}"
print "floor(3.9) = ${math.floor(3.9)}  ceil(3.1) = ${math.ceil(3.1)}  round(3.5) = ${math.round(3.5)}"

let mulai = time.now()
time.sleep(0.1)
let selesai = time.now()
print "sleep 0.1s terukur: ${math.round((selesai - mulai) * 1000)}ms"
print "waktu ISO: ${time.iso()}"

print "demo error + modul selesai!"