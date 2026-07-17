const sendButton = document.getElementById("sendBtn")

const queryInput = document.getElementById("queryInput")

const responseText = document.getElementById("responseText")

async function sendQuery() {
    const query = queryInput.value.trim()

    if (!query) {
        return;
    }

    responseText.textContent = "Thinking...";

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: query
            })
        });

        const data = await response.json();

        responseText.textContent = data.answer;

        queryInput.value = "";

    } catch (error) {

        responseText.textContent = "Something went wrong.";
        console.error(error);

    }
}

sendButton.addEventListener("click", sendQuery)

queryInput.addEventListener("keydown", (event) => {

    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendQuery();
    }
});