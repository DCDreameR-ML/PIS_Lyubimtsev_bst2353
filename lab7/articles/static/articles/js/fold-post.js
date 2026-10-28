document.querySelectorAll('.fold-button').forEach(button => {
    button.addEventListener('click', event => {
        const button = event.currentTarget;
        console.log('you clicked', button);
        const post = button.closest('.one-post');
        const folded = post.classList.toggle('folded');
        button.textContent = folded ? 'развернуть' : 'свернуть';
        button.setAttribute('aria-expanded', String(!folded));
    });
});
