# Lumpo v0.5.0 - ergonomics and resource safety

fn add(a, b) { return a + b }
let double = x => x * 2
print 5 |> double |> add(10)

let user = {"profile": {"name": "Renz"}}
print user?.profile?.name
print null?.profile?.name

let [first, second] = [10, 20]
let {name, role} = {"name": "Lumpo", "role": "language"}
print "${first}, ${second}: ${name} (${role})"

let events = []
fn work() {
    append(events, "work")
    defer append(events, "cleanup")
}
work()
print join(events, ", ")
