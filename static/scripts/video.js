function showNextSections() {
    document.getElementById('next-sections').style.display = 'block';
    document.getElementById('qa-sections').style.display = 'none';
    
    document.getElementById('next-tab').classList.add('active');
    document.getElementById('qa-tab').classList.remove('active');
}

function showQA() {
    document.getElementById('next-sections').style.display = 'none';
    document.getElementById('qa-sections').style.display = 'block';
    
    document.getElementById('next-tab').classList.remove('active');
    document.getElementById('qa-tab').classList.add('active');
}

function toggle(sectionwrap) {
    const chapterList = sectionwrap.querySelector('.chapter-list');
    const arrowIcon = sectionwrap.querySelector('.arrow-icon');
    const sectionitem = sectionwrap.querySelector('.section-text');
    if (chapterList.style.display === 'none' || chapterList.style.display === '') {
        chapterList.style.display = 'block';
        arrowIcon.style.transform = 'rotate(180deg)';
        sectionitem.classList.add('text-wrap');
    } else {
        chapterList.style.display = 'none';
        arrowIcon.style.transform = 'rotate(0deg)';
        sectionitem.classList.remove('text-wrap');
    }
}
