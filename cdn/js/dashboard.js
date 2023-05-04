function menuButtonSwitch () {
    // Selectors
    const menuButtonAttr = `[af-dashboard="menu-open-btn"]`;
    const menuCloseButtonAttr = `[af-dashboard="menu-close-btn"]`;
    const menuWrapperAttr = `[af-dashboard="menu-wrapper"]`;
    const hide = 'hide';
    const basicPosition = 'basic-position'

    // Element
    const menuWrapper = document.querySelector(menuWrapperAttr);
    const menuButton = document.querySelector(menuButtonAttr);
    const menuCloseButton = document.querySelector(menuCloseButtonAttr);

    // on click on the menu button, show or hide menu options
    menuButton?.addEventListener('click', ()=> {
        if (menuWrapper && !menuWrapper.classList.contains(basicPosition)) menuWrapper.classList.add(basicPosition);

        menuButton.classList.add(hide)
        menuCloseButton.classList.remove(hide)
    });

    menuCloseButton?.addEventListener('click', ()=> {
        if (menuWrapper && menuWrapper.classList.contains(basicPosition)) menuWrapper.classList.remove(basicPosition);
        
        menuCloseButton.classList.add(hide)
        menuButton.classList.remove(hide)
    });
}

function longBox() {
    // Selectors
    const buttonAttr = `[af-dashboard="long-box-btn"]`;
    const wrapperAttr = `[af-dashboard="long-box-wrapper"]`;
    const containerAttr = `[af-dashboard="long-box-container"]`;
    const hide = 'hide';

    // Element
    const containers = document.querySelectorAll(containerAttr);

    containers.forEach((container) => {
        const wrapper = container.querySelector(wrapperAttr);
        const actionButton = container.querySelector(buttonAttr);
        actionButton?.addEventListener('click', ()=> {
            if (wrapper && wrapper.classList.contains(hide)) {
                actionButton.textContent = "Minimize";
                wrapper.classList.remove(hide)
            } else if (wrapper && !wrapper.classList.contains(hide)) {
                actionButton.textContent = "view more";
                wrapper.classList.add(hide)
            }
        });
        wrapper?.classList.add(hide);
    });

}

function tabBox() {
    // Selectors
    const tabAttr = `af-tab`;
    const tabBoxAttr = `[${tabAttr}="box"]`;
    const tabContentAttr = `[${tabAttr}="tab-content"]`;
    const tabOptionAttr = `[${tabAttr}="tab-option"]`;
    const hide = 'hide';

    // All tab boxs
    const tabBoxs = document.querySelectorAll(tabBoxAttr);

    tabBoxs.forEach((tab) => {
        // get all tab menu options element
        const options = tab.querySelectorAll(tabOptionAttr);
        // get all tab contents element
        const contents = tab.querySelectorAll(tabContentAttr);
        // set tab content visibility base on tab options
        for (let index = 0; index < options.length; index++) {
            const button = options[index];
            const tabContent = contents[index];
            if (tabContent) {
                button.addEventListener("click", ()=> {
                    contents.forEach((content) => {
                        if (content === tabContent) content.classList.remove(hide);
                        else content.classList.add(hide)
                    });
                });
                if (index === 0) tabContent.classList.remove(hide);
                else tabContent.classList.add(hide);
            }
        }
    });

}

document.addEventListener('DOMContentLoaded', ()=> {
    menuButtonSwitch();
    longBox();
    tabBox();
});
