function menuButtonSwitch () {
    // Selectors
    const menuButtonAttr = `[af-basic="menu-btn"]`;
    const menuCloseButtonAttr = `[af-basic="close-btn"]`;
    const optionsAttr = `[af-basic="options-wrap"]`;
    const show = 'show';
    const hide = 'hide';
    const flex = 'flex';

    // Element
    const menuOptionWrap = document.querySelector(optionsAttr);
    const menuButton = document.querySelector(menuButtonAttr);
    const menuCloseButton = document.querySelector(menuCloseButtonAttr);

    // on click on the menu button, show or hide menu options
    menuButton?.addEventListener('click', ()=> {
        if (menuOptionWrap && !menuOptionWrap.classList.contains(flex)) menuOptionWrap.classList.add(flex);

        menuButton.classList.add(hide)
        menuCloseButton.classList.remove(hide)
    });

    menuCloseButton?.addEventListener('click', ()=> {
        if (menuOptionWrap && menuOptionWrap.classList.contains(flex)) menuOptionWrap.classList.remove(flex);
        
        menuCloseButton.classList.add(hide)
        menuButton.classList.remove(hide)
    });
}

document.addEventListener('DOMContentLoaded', () => {
    menuButtonSwitch()
});
