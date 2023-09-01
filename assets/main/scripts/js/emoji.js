document.addEventListener('DOMContentLoaded', function () {
    const emojiButton = document.querySelector('.emoji-button');
    const emojiList = document.querySelector('.emoji-list');
    const messageInput = document.querySelector('#message-input');
    const messengerSearchBtn = document.querySelector('.messenger-header-search-btn');
    const messengerSearchAfter = document.querySelector('.messenger-search-after-container');
    const messengerXmarkBtn = document.querySelector('.messenger-search-after-cancel-btn');
    const messengerGoBack = document.querySelector('.messenger-go-back-container');

    let messengerSearchVisible = false;

    messengerSearchBtn.addEventListener('click', () => {
        if (!messengerSearchVisible) {
            messengerSearchAfter.style.display = 'flex';
            messengerSearchVisible = true;
        } else {
            messengerSearchAfter.style.display = 'none';
            messengerSearchVisible = false;
        }
    })

    messengerXmarkBtn.addEventListener('click', () => {
        messengerSearchAfter.style.display = 'none';
        messengerSearchVisible = false;
    })

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

    // Scroll to the bottom of the chat when the page loads
    const messengerContent = document.querySelector('.messenger-content-section');
    messengerContent.scrollTop = messengerContent.scrollHeight;
});
