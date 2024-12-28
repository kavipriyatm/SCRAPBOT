async function scrape() {
    const url = document.getElementById('urlInput').value;
    const chatbox = document.getElementById('chatbox');

    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = `User: ${url}`;
    chatbox.appendChild(userMessage);

    try {
        const apiUrl =
("http://127.0.0.1:5000/scrape", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url, type: "static" }),
        });

        const data = await response.json();

        const botMessage = document.createElement('div');
        botMessage.className = 'bot-message';

        if (data.success) {
            botMessage.textContent = `Bot: ${JSON.stringify(data.data, null, 2)}`;
        } else {
            botMessage.textContent = `Bot: Error - ${data.error}`;
        }
        chatbox.appendChild(botMessage);
    } catch (err) {
        const errorMessage = document.createElement('div');
        errorMessage.className = 'bot-message';
        errorMessage.textContent = `Bot: Network Error - ${err.message}`;
        chatbox.appendChild(errorMessage);
    }
}