// Mantém o foco no primeiro campo após o carregamento da página.
document.addEventListener('DOMContentLoaded', () => {
    const titleField = document.querySelector('#titulo');
    if (titleField) {
        titleField.focus();
    }
});
