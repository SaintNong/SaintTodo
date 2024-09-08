
document.addEventListener("DOMContentLoaded", function () {
    // Initialize tsParticles
    tsParticles.load("tsparticles", {
        particles: {
            number: {
                value: 30,
            },
            size: {
                value: 2,
            },
            move: {
                enable: true,
                speed: 0.6,
            },
            line_linked: {
                enable: true,
                distance: 250,
            },
        },
    });
});
