document.getElementById("generate").addEventListener("click", async () => {
  const topic = document.getElementById("topic").value;

  const res = await fetch("https://linkedin-bot-4qg7.onrender.com/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ topic })
  });

  const data = await res.json();

  document.getElementById("about").innerText = data.about;
  document.getElementById("linkedin").innerText = data.linkedin;
});