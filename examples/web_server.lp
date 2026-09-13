# web server example — lumpo (full featured)
import "http"
import "db"
import "json"
import "crypto"
import "env"
import "log"

# in-memory DB untuk demo
let db = db.open(":memory:")
db.execute("CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, title TEXT, done INTEGER)")

fn seed_data() {
    db.execute("INSERT INTO todos (title, done) VALUES (?, ?)", ["beli kopi", 1])
    db.execute("INSERT INTO todos (title, done) VALUES (?, ?)", ["ngoding", 0])
    log.info("seeded 2 todos")
}

seed_data()

fn home_page(req) {
    let name = req.query.get("name", ["world"])[0]
    let rows = db.query("SELECT COUNT(*) AS c FROM todos")
    let total = int(rows[0]["c"])
    let body = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Lumpo App</title>
<style>body{font-family:system-ui;max-width:800px;margin:40px auto;padding:0 20px;background:#fafafa}.header{text-align:center;border-bottom:2px solid #2563eb;padding-bottom:16px}.todo-item{display:flex;justify-content:space-between;align-items:center;padding:8px;border-bottom:1px solid #eee}.btn{background:#2563eb;color:#fff;border:none;padding:6px 12px;border-radius:4px;cursor:pointer}</style>
</head>
<body>
<div class="header">
<h1>Selamat datang, ${name}!</h1>
<p>ini aplikasi lumpo yang berjalan di server ini.</p>
<p>total todo: ${total}</p>
</div>
<a href="/api/todos">lihat API data</a>
</body>
</html>
"""
    return [200, "text/html;charset=utf-8", body]
}

fn api_list_todos(req) {
    let todos = db.query("SELECT id, title, done FROM todos ORDER BY id DESC")
    return [200, "application/json", json.stringify(todos)]
}

fn api_create_todo(req) {
    let title = req.query.get("title", ["untitled"])[0]
    let row_id = db.execute("INSERT INTO todos (title, done) VALUES (?, 0)", [title])
    return [201, "application/json", json.stringify({status: "created", id: int(row_id), title: title})]
}

fn api_health(req) {
    return [200, "application/json", json.stringify({status: "ok", engine: "lumpo"})]
}

router.get("/", home_page)
router.get("/api/todos", api_list_todos)
router.post("/api/todos", api_create_todo)
router.get("/api/health", api_health)

print "starting app on port 8080..."
http.listen(8080, router.handle)
