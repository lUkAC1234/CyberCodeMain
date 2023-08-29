const tabs = [
    { btn: document.getElementById('about-the-jobBtn'), content: document.querySelector('.about-the-job-content') },
    { btn: document.getElementById('responsibilitiesBtn'), content: document.querySelector('.responsibilities-content') },
    { btn: document.getElementById('requirementsBtn'), content: document.querySelector('.requirements-content') }
];

tabs.forEach(tab => {
    tab.btn.addEventListener('click', () => {
        tabs.forEach(otherTab => {
            otherTab.btn.classList.remove('active');
            otherTab.content.classList.remove('active'); // Убираем класс "active" у контента
        });

        tab.btn.classList.add('active');
        tab.content.classList.add('active'); // Добавляем класс "active" контенту

        // Сохраняем ID активной вкладки в Local Storage
        localStorage.setItem('activeTab', tab.btn.id);
    });
});

// Проверяем наличие сохраненной активной вкладки в Local Storage
const activeTabId = localStorage.getItem('activeTab');
if (activeTabId) {
    const activeTab = tabs.find(tab => tab.btn.id === activeTabId);
    if (activeTab) {
        tabs.forEach(tab => {
            if (tab !== activeTab) {
                tab.content.classList.remove('active');
            }
        });
        activeTab.btn.click(); // Вызываем клик, чтобы активировать сохраненную вкладку
    }
}
