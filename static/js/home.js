
document.addEventListener("DOMContentLoaded", function () {
    /* Main Animation */
    // Main heading
    anime({
        targets: "#title-main",
        translateY: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad"
    });

    // Subtitles
    anime({
        targets: "#subtitle-1",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 250
    });

    anime({
        targets: "#subtitle-2",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 500
    });

    anime({
        targets: "#subtitle-3",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 750
    });

    // Sign Up button
    anime({
        targets: "#title-button",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 1000
    });
    
    /* Features Animation */
    // Features heading
    anime({
        targets: "#heading-features",
        translateY: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 1250
    });

    // Animate the feature boxes
    anime({
        targets: "#feature-1",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 1350
    });

    anime({
        targets: "#feature-2",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 1450
    });

    anime({
        targets: "#feature-3",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 1550
    });

    anime({
        targets: "#feature-4",
        translateX: [-50, 0],
        opacity: [0, 1],
        duration: 1000,
        easing: "easeInOutQuad",
        delay: 1650
    });
});
