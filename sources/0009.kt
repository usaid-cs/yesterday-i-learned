
fun main() {
    val a = Foo()
    print("Hello, ")
    a foo "World!!!"
}

class Foo {
    infix fun foo(a: String) {
        println(a.toString())
    }
}
