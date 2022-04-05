window.addEventListener("load", function () {
  document
    .querySelector('input[type="file"]')
    .addEventListener("change", function () {
      if (this.files && this.files[0]) {
        var img = document.querySelector("img");
        img.onload = () => {
          URL.revokeObjectURL(img.src); // no longer needed, free memory
        };

        img.src = URL.createObjectURL(this.files[0]); // set src to blob url
      }
    });
});

const upload_button = document.querySelector("#upload_image");
upload_button.addEventListener("click", () => {
  const compress_button = document.querySelector("#compress_button");
  compress_button.style.display = "block";
  upload_button.style.display = "none";
});
