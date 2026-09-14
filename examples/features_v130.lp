# examples/fitur_v130.lp — demo fitur baru LPLang 1.3.0
# (switch, break/continue, compound assign, block comment, null-coalescing, ternary)

/* ini komentar blok
   multi-baris, baru di v1.3.0
   tidak akan dieksekusi */

# ── switch ──
let skor = 85
switch skor {
    case 90 { print "grade A" }
    case 80 { print "grade B" }
    case 70 { print "grade C" }
    default { print "grade D" }
}

# switch pada string
let warna = "merah"
switch warna {
    case "merah" { print "berhenti" }
    case "kuning" { print "hati-hati" }
    case "hijau" { print "jalan" }
    default { print "lampu rusak" }
}

# ── compound assignment ──
let counter = 10
counter += 5
print "counter setelah +=5: ${counter}"
counter -= 3
print "counter setelah -=3: ${counter}"
counter *= 2
print "counter setelah *=2: ${counter}"
counter /= 4
print "counter setelah /=4: ${counter}"

# ── break & continue ──
let ketemu = 0
for i in range(1, 20) {
    if i > 50 { break }
    if i % 2 != 0 { continue }   # lewati angka ganjil
    ketemu += 1
}
print "banyak angka genap 1..19: ${ketemu}"

let langkah = 0
while true {
    langkah += 1
    if langkah == 7 { break }
}
print "berhenti di langkah: ${langkah}"

# ── null-coalescing ──
let user_input = null
let nama_final = user_input ?? "anonymous"
print "nama: ${nama_final}"

let sudah_ada = "renz"
print "nama: ${sudah_ada ?? 'anonymous'}"

# ── ternary ──
let umur = 20
let kategori = umur >= 18 ? "dewasa" : "anak"
print "kategori: ${kategori}"

let angka = 7
print "${angka} itu ${angka % 2 == 0 ? 'genap' : 'ganjil'}"

# ── range dengan step ──
let out = []
for i in range(0, 20, 3) {
    push(out, i)
}
print "range(0,20,3): ${join(out, ',')}"

# ── string methods baru ──
let s = "lumpo"
print "starts_with(s,'lum'): ${starts_with(s, 'lum')}"
print "ends_with(s,'po'): ${ends_with(s, 'po')}"
print "repeat('ab',3): ${repeat('ab', 3)}"
print "pad_left('7',3,'0'): ${pad_left('7', 3, '0')}"
print "index_of('hello','ll'): ${index_of('hello', 'll')}"
print "index_of tidak ketemu: ${index_of('hello', 'zz')}"

print "demo v1.3.0 selesai!"