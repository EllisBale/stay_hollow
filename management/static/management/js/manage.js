document.addEventListener("DOMContentLoaded", () => {

   const deleteBtns = document.querySelectorAll(".delete-btn");

   deleteBtns.forEach(deleteBtn => {
    deleteBtn.addEventListener("click", event => {
        if (!confirm("Are You Sure You Want to Delete This User?")) {
            event.preventDefault();
        }
    });
   });
});