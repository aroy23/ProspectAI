function uploadProfilePic() {
    const fileInput = document.getElementById('fileInput');
    const profilePic = document.getElementById('profilePic');

    // Check if a file was selected
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        // Set the src of the profile picture to the uploaded file
        reader.onload = function(e) {
            profilePic.src = e.target.result; // Set the image source to the uploaded file
        }

        // Read the uploaded file as a data URL
        reader.readAsDataURL(fileInput.files[0]);
    }
}
