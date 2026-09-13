# about page
let title = "Tentang Lumpo"
print "<html><head><title>${title}</title></head>"
print "<body>"
print "<h1>${title}</h1>"
print "<p>Lumpo adalah bahasa pemrograman yang dirancang untuk membangun website.</p>"
print "<p>Fitur utama:</p>"
let features = ["web-first", "ringan", "stabil", "mudah dipahami", "multifungsi"]
print "<ul>"
for f in features {
    print "<li>${f}</li>"
}
print "</ul>"
print "<a href='index.html'>kembali</a>"
print "</body></html>"
