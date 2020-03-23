class Foo {
    a = () => {
        console.log('a');
        console.log(this);
    }
    b() {
        console.log('b');
        console.log(this);
    }
}

class Bar extends Foo {
    a = () => {
        super.a();  // Can't do this (a standalone function has no super)
    };

    b() {
        super.b();
    }
}

const foo = new Foo();
foo.a();
foo.b();

const bar = new Bar();
bar.a();
bar.b();
