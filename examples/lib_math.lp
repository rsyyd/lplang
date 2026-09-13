# lib_math.lp — library lokal yang di-import contoh lain (.lp)
# dipanggil via: import "./lib_math.lp"

fn double(n) {
    return n * 2
}

fn kuadrat(n) {
    return n * n
}

const PHI = 1.618
let VERSION = "lib_math-1.0"

print "lib_math dimuat (ini stdout hanya saat dieksekusi langsung)"