// Todo App

class Component {
    #display;
    #width;
    #height;
    #backgroundColor;
    #color;
    #fontSize;
    #title;
    #description;
    #titleContent;
    #descriptionContent;
    #blockPadding;
    #titlePadding;
    #descriptionPadding;
    #borderRadius;
    #blockMargin;

    constructor(
        display = "flex", width = "100%", height = "100%",
        backgroundColor = "#fff", color = "#000",
        fontSize = "2rem", title = "h2", description = "p",
        titleContent = "Test Content", descriptionContent = "This is test description",
        blockPadding = "0 0 0 0", titlePadding = "0 0 0 0", descriptionPadding = "0 0 0 0",
        borderRadius = "1px", blockMargin = "1rem"
    ) {
        this.#display = display;
        this.#width = width;
        this.#height = height;
        this.#backgroundColor = backgroundColor;
        this.#color = color;
        this.#fontSize = fontSize;
        this.#title = title;
        this.#titleContent = titleContent;
        this.#description = description;
        this.#descriptionContent = descriptionContent;
        this.#blockPadding = blockPadding;
        this.#titlePadding = titlePadding;
        this.#descriptionPadding = descriptionPadding;
        this.#borderRadius = borderRadius;
        this.#blockMargin = blockMargin;
    }

    set Display(value) { this.#display = value; }
    set Width(value) { this.#width = value; }
    set Height(value) { this.#height = value; }
    set BGColor(value) { this.#backgroundColor = value; }
    set Color(value) { this.#color = value; }
    set FontSize(value) { this.#fontSize = value; }
    set Title(value) { this.#title = value; }
    set TitleContent(value) { this.#titleContent = value; }
    set Description(value) { this.#description = value; }
    set DescriptionContent(value) { this.#descriptionContent = value; }
    set BlockPadding(value) { this.#blockPadding = value; }
    set TitlePadding(value) { this.#titlePadding = value; }
    set DescriptionPadding(value) { this.#descriptionPadding = value; }
    set BorderRadius(value) { this.#borderRadius = value; }
    set BlockMargin(value) { this.#blockMargin = value; }

    err() {
        try {
            if (typeof arguments !== "string") {
                throw new Error("Values can be only string type values");
            }
        } catch (err) {
            console.log(`${err.name}: ${err.type}`);
        }
    }

    setStateBlock(display = this.#display, err = this.err()) {
        this.#display = display;
        console.log(err);
    }

    setBlockSize(width = this.#width, height = this.#height) {
        this.#width = width;
        this.#height = height;
    }

    setBGCCFS(bgColor = this.#backgroundColor, color = this.#color, fontSize = this.#fontSize) {
        this.#backgroundColor = bgColor;
        this.#color = color;
        this.#fontSize = this.#fontSize;
    }
    
    setBack(value) {
        this.#backgroundColor = value;
    }
    
    createComponent() {
        let block = document.createElement("li");
        let title = document.createElement(this.#title);
        let description = document.createElement(this.#description);

        block.append(title);
        block.append(description);

        title.textContent = this.#titleContent;
        description.textContent = this.#descriptionContent;

        block.setAttribute("class", "block");
        title.setAttribute("class", "block-title");
        description.setAttribute("class", "block-description");

        block.style.display = this.#display;
        block.style.width = this.#width;
        block.style.height = this.#height;
        block.style.backgroundColor = this.#backgroundColor;
        block.style.color = this.#color;
        block.style.fontSize = this.#fontSize;
        block.style.padding = this.#blockPadding;
        title.style.padding = this.#titlePadding;
        description.style.padding = this.#descriptionPadding;
        block.style.borderRadius = this.#borderRadius;
        block.style.margin = this.#blockMargin;

        return document.querySelector(".todo-list").append(block);
    }
}

const addBtn = document.querySelector("#create_c");
const deleteBtn = document.querySelector("#delete_c");

let components = [];

function createComponent() {
    try {
        for (let i = 0; i < 1; i++) {
            if (i % 2 === 0) {
                components.push(new Component("block", "", "", "white", "black", "1.3rem", "h3", "p", "JavaScript", "JavaScript is a programming language", "1rem", "0 0 2rem 0", "1rem", "2rem", "1rem"));
                components[i].createComponent();
            } else {
                components.push(new Component("block", "", "", "black", "white", "1.3rem", "h3", "p", "JavaScript", "JavaScript", "1rem", "0 0 1rem 0", "1rem", "2rem", "1rem"));
                components[i].createComponent();
            }
            console.log("Component added");
        }
    } catch (err) {
        console.log(`${err.name}: ${err.message}`);
    }
    console.log(components);
}
addBtn.addEventListener("click", createComponent);

function deleteComponent() {
    try {
        components.pop();
        let last = document.querySelector(".block");
        last.remove();
        console.log("Last created component is deleted");
        console.log(components);
    } catch (err) {
        console.log(`${err.name}: ${err.message}`);
    }
}
deleteBtn.addEventListener("click", deleteComponent);

console.log(components);

function sizeOfWindow() {
    let windowHeight = window.innerHeight;
    let windowWidth = window.innerWidth;
    let vh = document.querySelector(".window-height");
    let vw = document.querySelector(".window-width");
    vh.textContent = `Height of window: ${windowHeight}`;
    vw.textContent = `Width of window: ${windowWidth}`;
    let result = document.querySelector(".window");
    result.append(vh, vw);
    return { result };
}

window.addEventListener("resize", sizeOfWindow);