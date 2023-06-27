class Nav {
    #on;
    #off;
    #menu;
    #displayOn;
    #displayOff;
    #animationOn;
    #animationOff;

    static #inputState;

    constructor(on, off, menu, onStyle = "block", offStyle = "none", animationOn, animationOff) {
        this.#on = on;
        this.#off = off;
        this.#menu = menu;
        this.#displayOn = onStyle;
        this.#displayOff = offStyle;
        this.#animationOn = animationOn;
        this.#animationOff = animationOff;
    }

    get #On            ()      { return this.#on;             }
    get #Off           ()      { return this.#off;            }
    get #Menu          ()      { return this.#menu;           }
    get #DisplayOn     ()      { return this.#displayOn;      }
    get #DisplayOff    ()      { return this.#displayOff;     }
    get #AnimationOn   ()      { return this.#animationOn;    }
    get #AnimationOff  ()      { return this.#animationOff;   }

    set #On            (value) { this.#on           = value;  }
    set #Off           (value) { this.#off          = value;  }
    set #Menu          (value) { this.#menu         = value;  }
    set #DisplayOn     (value) { this.#displayOn    = value;  }
    set #DisplayOff    (value) { this.#displayOff   = value;  }
    set #AnimationOn   (value) { this.#animationOn  = value;  }
    set #AnimationOff  (value) { this.#animationOff = value;  }
    
    TurnOn() {
        Nav.#inputState = "On button is clicked";
        console.log(Nav.#inputState);

        let btnOn  = document.getElementById(this.#on),
            btnOff = document.getElementById(this.#off),
            menu   = document.getElementById(this.#menu);

        btnOn.style.display  = this.#displayOff;
        btnOn.style.animation = this.#animationOn;
        btnOff.style.display = this.#displayOn;
        menu.style.display   = this.#displayOn;
        menu.style.animation = this.#animationOn;
        
        return {
            btnOn,
            btnOff,
            menu
        };
    }
    
    TurnOff() {
        Nav.#inputState = "Off button is clicked";
        console.log(Nav.#inputState);

        let btnOn  = document.getElementById(this.#on),
            btnOff = document.getElementById(this.#off),
            menu   = document.getElementById(this.#menu);

        btnOn.style.display  = this.#displayOn;
        btnOff.style.animation = this.#animationOn;
        btnOff.style.display = this.#displayOff;
        menu.style.animation = this.#animationOff;
        setTimeout(() => {
            menu.style.display = this.#displayOff;
        }, 299);

        return {
            btnOn,
            btnOff,
            menu
        };
    }
}

// IMPLEMENTATION

const btnOnId      = "on";
const btnOffId     = "off";
const menuId       = "nav_menu";
const displayOn    = "flex";
const displayOff   = "none";
const animationOn  = "menu-anim-on 0.3s ease";
const animationOff = "menu-anim-off 0.3s ease";

let nav = new Nav(btnOnId, btnOffId, menuId, displayOn, displayOff, animationOn, animationOff);

const TurnOn  = () => nav.TurnOn();
const TurnOff = () => nav.TurnOff();

const btnON = document.getElementById("on");
const btnOFF = document.getElementById("off");

btnON.addEventListener("click", TurnOn);
btnOFF.addEventListener("click", TurnOff);

