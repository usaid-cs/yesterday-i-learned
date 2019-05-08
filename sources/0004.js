class A {
    constructor() {
        console.log('A.constructor');
    }

    c() {
        console.log('A.c');
    }
}

class B extends A {
    constructor() {
        super();  // Works
        // super.constructor();  // TypeError: Class constructor A cannot be invoked without 'new'
        // new super.constructor();  // ReferenceError: Unsupported reference to 'super'
        console.log('B.constructor');
        this.c();  // Works
        super.c();  // Works
    }

    c() {
        super.c();  // Works
        // super();  // SyntaxError: 'super' keyword unexpected here
        // super.constructor();  // TypeError: Class constructor A cannot be invoked without 'new'
        // new super.constructor();  // ReferenceError: Unsupported reference to 'super'
        console.log('B.c');
    }
}


(new B).c();