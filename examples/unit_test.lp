# test_math_and_logic_test.lp

fn test_math() {
    assert(10 * 10 == 100, "perkalian 10x10")
    assert(100 / 4 == 25, "pembagian 100/4")
    assert(7 % 3 == 1, "modulo")
}

fn test_strings() {
    let greeting = "halo" + " " + "dunia"
    assert(len(greeting) == 10, "panjang string")
    assert(upper("lumpo") == "LUMPO", "upper case")
    assert(lower("LUMPO") == "lumpo", "lower case")
    assert(trim("  bersih  ") == "bersih", "trim whitespace")
}

fn test_lists() {
    let arr = [1, 2, 3]
    push(arr, 4)
    assert(len(arr) == 4, "panjang list setelah push")
    let popped = pop(arr)
    assert(popped == 4, "pop value")
    assert(len(arr) == 3, "panjang list setelah pop")
}

test_math()
test_strings()
test_lists()

print "semua unit test .lp lulus!"
