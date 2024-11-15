
    document.addEventListener('DOMContentLoaded', function() {
        const actionBtns = document.querySelectorAll('.action-btn');
        const containers = document.querySelectorAll('.container');
        const closeBtns = document.querySelectorAll('.fechar');

        actionBtns.forEach(function(button, index) {
            button.addEventListener('click', function() {                containers[index].classList.add('show');
            });
        });
        closeBtns.forEach(function(button, index) {
            button.addEventListener('click', function() {
                containers[index].classList.remove('show');
            });
        });
    });
