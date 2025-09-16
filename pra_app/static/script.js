const passwordInput = document.getElementById("password");
    const toggleButton = document.getElementById("togglePassword");
    toggleButton.addEventListener("click", () => {
        passwordInput.type =
        passwordInput.type === "password" ? "text" : "password";
        toggleIcon.innerHTML = isPassword ? "close" : "open";
    });
    
    
    function copyPassword(id) {
        const passwordInput = document.getElementById("password_" + id);
        passwordInput.type = "text"; // Temporarily show password for copying
        passwordInput.select();
        passwordInput.setSelectionRange(0, 99999); // For mobile devices
    
        navigator.clipboard.writeText(passwordInput.value)
        .then(() => {
            passwordInput.type = "password"; // Hide password again
        })
        .catch(err => console.error("Error copying password: ", err));
    }
    