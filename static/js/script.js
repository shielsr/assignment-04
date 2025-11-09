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


document.addEventListener('DOMContentLoaded', () => {
    // Get all selects with the class 'order-status'
    const selects = document.querySelectorAll('select.order-status');

    selects.forEach(select => {
        const status = (select.getAttribute('data-status') || '').trim();
        if (!status) return;

        // Case-insensitive match
        Array.from(select.options).forEach(option => {
            if (option.value.toLowerCase() === status.toLowerCase()) {
                option.selected = true;
            }
        });
    });
});