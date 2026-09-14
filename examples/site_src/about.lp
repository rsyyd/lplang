# about page
let title = "About Lumpo"
print "<html><head><title>${title}</title></head>"
print "<body>"
print "<h1>${title}</h1>"
print "<p>Lumpo is a programming language designed for building websites.</p>"
print "<p>Key features:</p>"
let features = ["web-first", "lightweight", "stable", "easy to understand", "versatile"]
print "<ul>"
for f in features {
    print "<li>${f}</li>"
}
print "</ul>"
print "<a href='index.html'>back</a>"
print "</body></html>"
