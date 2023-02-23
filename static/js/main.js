window.addEventListener("load", ()=>{
    // aos init
    AOS.init({
        offset: 50,
        delay: 100,
        duration: 800,
        easing: 'ease',
        once: false,
        mirror: false,
        anchorPlacement: 'top-bottom'
    })

    const menuBtn = document.querySelector(".menu-btn")
    const closeBtn = document.querySelector(".close-btn")
    const menu = document.querySelector(".mobile-nav")
    const navLinks = document.querySelectorAll(".mobile-nav a")

    menuBtn.addEventListener("click", openNav)
    closeBtn.addEventListener("click", closeNav)

    navLinks.forEach(link => {
        link.addEventListener("click", closeNav)
    });

    function openNav() {
        menu.classList.add("active")
    }
    function closeNav() {
        menu.classList.remove("active")
    }

})