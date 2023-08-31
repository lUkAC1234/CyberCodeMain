document.addEventListener('DOMContentLoaded', function () {
    const emojiButton = document.querySelector('.emoji-button');
    const emojiList = document.querySelector('.emoji-list');
    const messageInput = document.querySelector('#message-input');

    let isEmojiListVisible = false;

    // Toggle emoji list when emoji button is clicked
    emojiButton.addEventListener('click', (event) => {
        event.stopPropagation();
        if (!isEmojiListVisible) {
            emojiList.style.display = 'block';
            isEmojiListVisible = true;
        } else {
            emojiList.style.display = 'none';
            isEmojiListVisible = false;
        }
    });

    // Close emoji list when clicking outside
    document.addEventListener('click', () => {
        if (isEmojiListVisible) {
            emojiList.style.display = 'none';
            isEmojiListVisible = false;
        }
    });

    // Prevent emoji list from closing when clicked inside
    emojiList.addEventListener('click', (event) => {
        event.stopPropagation();
    });

    // Insert selected emoji into the message input
    document.querySelectorAll('.emoji').forEach(emoji => {
        emoji.addEventListener('click', () => {
            messageInput.value += emoji.textContent;
        });
    });
});
