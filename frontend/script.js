async function getRec() {
  const movie = document.getElementById("movie").value;
  const list = document.getElementById("result");
  const status = document.getElementById("status");

  list.innerHTML = "";
  status.innerText = "Fetching recommendations...";

  if (!movie) {
    status.innerText = "Please enter a movie name.";
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ movie })
    });

    const data = await response.json();

    status.innerText = "";

    if (data.error) {
      status.innerText = data.error;
      return;
    }

    data.recommendations.forEach(m => {
      const li = document.createElement("li");
      li.innerText = m;
      list.appendChild(li);
    });

  } catch (error) {
    status.innerText = "Unable to connect to backend.";
    console.error(error);
  }
}
