# examples/fitur_bahasa.lp — demo fitur inti LPLang 1.2
# (variabel, fungsi, string interpolation, collections, functional builtins)

# ── variabel & tipe dasar ──
let nama = "renz"
let umur = 25
let tinggi = 1.75
let aktif = true
let data_kosong = null

print "halo ${nama}, umur ${umur}, tinggi ${tinggi}m, aktif=${aktif}, kosong=${data_kosong}"

# ── list & map ──
let buah = ["apel", "pisang", "mangga"]
push(buah, "durian")
print "buah: ${join(buah, ', ')} (${len(buah)} item)"

let config = {host: "localhost", port: 8080, debug: true}
print "host=${config.host} port=${config.port}"

# ── fungsi ──
fn tambah(a, b) {
    return a + b
}
fn faktorial(n) {
    if n <= 1 { return 1 }
    return n * faktorial(n - 1)
}
print "5! = ${faktorial(5)}"
print "10 + 32 = ${tambah(10, 32)}"

# ── control flow ──
let nilai = 87
if nilai >= 90 {
    print "grade: A"
} else if nilai >= 75 {
    print "grade: B"
} else {
    print "grade: C"
}

let total = 0
for i in range(1, 11) {
    total = total + i
}
print "jumlah 1..10 = ${total}"

let n = 5
while n > 0 {
    print "mundur: ${n}"
    n = n - 1
}

# ── functional builtins ──
let angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let genap = filter(angka, fn(x) { return x % 2 == 0 })
print "genap: ${join(genap, ',')}"

let kuadrat = map(angka, fn(x) { return x * x })
print "kuadrat: ${join(kuadrat, ',')}"

let jumlah_total = reduce(angka, fn(acc, x) { return acc + x }, 0)
print "jumlah semua = ${jumlah_total}"

let pertama = find(angka, fn(x) { return x > 5 })
print "angka pertama > 5: ${pertama}"

print "ada > 9? ${any(angka, fn(x) { return x > 9 })}"
print "semua > 0? ${all(angka, fn(x) { return x > 0 })}"

# ── string methods ──
let pesan = "  Lumpo is AWESOME  "
print "upper: ${upper(trim(pesan))}"
print "lower: ${lower(trim(pesan))}"
print "replace: ${replace(pesan, 'AWESOME', 'KEREN')}"
print "substr(0,5): ${substr(trim(pesan), 0, 5)}"
print "contains 'sih': ${contains(trim(pesan), 'AWESOME')}"

print "demo selesai!"
