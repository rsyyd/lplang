# examples/unit_test.lp - unit test example

fn test_math() {
    assert(10 * 10 == 100, "multiplication 10x10")
    assert(100 / 4 == 25, "division 100/4")
    assert(7 % 3 == 1, "modulo")
}

fn test_strings() {
    let greeting = "hello" + " " + "world"
    assert(len(greeting) == 11, "string length")
    assert(upper("lumpo") == "LUMPO", "upper case")
    assert(lower("LUMPO") == "lumpo", "lower case")
    assert(trim("  clean  ") == "clean", "trim whitespace")
}

fn test_lists() {
    let arr = [1, 2, 3]
    push(arr, 4)
    assert(len(arr) == 4, "list length after push")
    let popped = pop(arr)
    assert(popped == 4, "pop value")
    assert(len(arr) == 3, "list length after pop")
}

test_math()
test_strings()
test_lists()

print "all .lp unit tests passed!"
