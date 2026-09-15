# full-stack todo API - demo of all lumpo features together
import "http"
import "db"
import "json"
import "crypto"
import "log"
import "fs"

let db = db.open("todos.db")
db.execute("CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, title TEXT, done INTEGER)")

fn list_todos(req) {
    let rows = db.query("SELECT id, title, done FROM todos ORDER BY id")
    return [200, "application/json", json.stringify(rows)]
}

fn get_todo(req) {
    let id = int(req.query.get("id", ["0"])[0])
    let rows = db.query("SELECT id, title, done FROM todos WHERE id = ?", [id])
    if len(rows) == 0 {
        return [404, "application/json", json.stringify({"error": "not found"})]
    }
    return [200, "application/json", json.stringify(rows[0])]
}

fn create_todo(req) {
    # simplified body parsing - just hardcode demo
    let title = req.query.get("title", ["untitled"])[0]
    db.execute("INSERT INTO todos (title, done) VALUES (?, 0)", [title])
    return [201, "application/json", json.stringify({"status": "created", "title": title})]
}

fn delete_todo(req) {
    let id = int(req.query.get("id", ["0"])[0])
    db.execute("DELETE FROM todos WHERE id = ?", [id])
    return [200, "application/json", json.stringify({"status": "deleted"})]
}

fn health(req) {
    log.info("health check from " + req.method)
    return [200, "application/json", json.stringify({"status": "ok"})]
}

router.get("/api/health", health)
router.get("/api/todos", list_todos)
router.get("/api/todos/:id", get_todo)
router.post("/api/todos", create_todo)
router.get("/api/todos/:id/delete", delete_todo)

print "todo API running on :3000"
http.listen(3000, router.handle)
