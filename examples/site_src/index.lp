# static site page - will be compiled to HTML by `lumpo build`
let title = "Beranda"
let year = 2026

print "<html>"
print "<head><title>${title} - Lumpo Site</title></head>"
print "<body>"
print "<h1>${title}</h1>"
print "<p>website ini di-generate oleh lumpo static site builder.</p>"
print "<ul>"
for i in range(1, 4) {
    print "<li>item ${i}</li>"
}
print "</ul>"
print "<footer>copyright ${year} lumpo</footer>"
print "</body></html>"
