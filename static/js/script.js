document.addEventListener("DOMContentLoaded", function () {
  // Select all checkboxes with the class .show-passwords
  const toggles = document.querySelectorAll(".show-password");

  toggles.forEach(toggle => {
    toggle.addEventListener("change", function () {
      const show = this.checked;
      // Select all password fields on the current page
      const passwordFields = document.querySelectorAll(".password-field");
      passwordFields.forEach(input => {
        input.type = show ? "text" : "password";
      });
    });
  });
});