// The 'Show password' checkboxes

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


/* Changing the status on the /admin page. 
This (indirectly) checks the order.status from the db 
and, in the HTML select dropdown, adds the 'selected' attribute to it. */

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


/* Login error message */

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("login-form");
  const errorMessage = document.getElementById("error-message");

  if (!form || !errorMessage) return;  // This stops the listener causing an error on other pages

  form.addEventListener("submit", async (e) => {
    e.preventDefault(); // Stop normal form submission

    // Clear any previous message
    errorMessage.textContent = "";

    try {
      const formData = new FormData(form);

      const response = await fetch("/login", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!data.success) {
        // Pulling in the message from app.py
        errorMessage.textContent = data.message;

      } else {
        // Redirect to the page from Flask
        window.location.href = data.redirect;
      }
    } catch (err) {
      console.error("Login error:", err);
      errorMessage.textContent = "Something went wrong. Please try again.";
    }
  });
});