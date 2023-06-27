class Test {
    constructor(...messages) {
        this.messages = messages;
    }
    output() {
        let messages = 'messages',
            length   = 'length';

        return {
            [messages]: [...this.messages],
            [length]: this.messages.length,
        };
    }
    addToEnd(...values) {
        this.messages.push.call(this.messages, ...values);
    }
    addToStart(...values) {
        this.messages.unshift.call(this.messages, ...values);
    }
    removeLast() {
        this.messages.pop.call(this.messages);
    }
    removeStart() {
        this.messages.shift.call(this.messages);
    }
}

export { Test };