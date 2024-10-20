const menuIcon = document.querySelector('.menuicon');
const mobileMenu = document.querySelector('.mobile-menu');
const crossicon = document.querySelector('.crossicon');

crossicon.style.display = "none";

menuIcon.addEventListener('click', () => {
    mobileMenu.classList.toggle('active');
    setTimeout(()=>{
        crossicon.style.display = "block";
    },300);
    
  });
crossicon.addEventListener('click', () => {
    mobileMenu.classList.remove('active');
    crossicon.style.display = "none";
  });

  document.addEventListener('DOMContentLoaded', () => {
    const chapters = document.querySelectorAll('.chapter');
    
    chapters.forEach(chapter => {
        chapter.addEventListener('click', () => {
            // Close any other expanded chapter
            chapters.forEach(chap => {
                if (chap !== chapter) {
                    chap.classList.remove('expanded');
                }
            });
            
            // Toggle the clicked chapter
            chapter.classList.toggle('expanded');
        });
    });
});
