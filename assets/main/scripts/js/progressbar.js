const bodyEl = document.body;
const barEl = document.querySelector('.bar');

function updateBar() {
    let scrollPos = (window.scrollY /
        (bodyEl.scrollHeight - window.innerHeight)) * 100;
    barEl.style.width = `${scrollPos}%`;  // Change 'progress' to 'scrollPos'
    requestAnimationFrame(updateBar);
}

updateBar();