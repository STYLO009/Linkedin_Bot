document.getElementById("generateBtn").addEventListener("click", generate);
document.getElementById("copyAbout").addEventListener("click", () => copyText("about"));
document.getElementById("copyLinkedin").addEventListener("click", () => copyText("linkedin"));

async function generate() {
  const topic = document.getElementById("topic").value;
  const loader = document.getElementById("loader");

  if (!topic) {
    alert("Enter a topic!");
    return;
  }

  loader.style.display = "block";

  try {
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

  } catch (err) {
    alert("API error!");
  }

  loader.style.display = "none";
}

function copyText(id) {
  const text = document.getElementById(id).innerText;
  navigator.clipboard.writeText(text);
  alert("Copied!");
}