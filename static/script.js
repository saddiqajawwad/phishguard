// script.js
// We keep JS minimal.
// Just a small UI effect so it feels interactive.

document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".btn");

  buttons.forEach((btn) => {
    btn.addEventListener("mousemove", (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      btn.style.boxShadow = `0 0 0 4px rgba(77, 225, 255, 0.08),
                             0 20px 60px rgba(0,0,0,0.35)`;
      btn.style.transform = "translateY(-1px)";
    });

    btn.addEventListener("mouseleave", () => {
      btn.style.boxShadow = "";
      btn.style.transform = "";
    });
  });
});
