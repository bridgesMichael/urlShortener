// Add event listener to the encode form
document
  .getElementById("encodeForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault(); // prevent default so POST request can be sent

    // Get the full URL from the input field
    const fullUrl = document.getElementById("encodeurl").value;

    // Send a POST request to the /encode/ URL to encode the URL
    const response = await fetch("/encode/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0]
          .value,
      },
      body: JSON.stringify({ full_url: fullUrl }), // converts to JSON for request
    });

    // If the response is successful, update the encoded URL text content
    if (response.ok) {
      const data = await response.json(); // get JSON data from response
      document.getElementById("encodedUrl").textContent = data.short_url; // update text content of HTML element
    } else {
      alert("Error encoding the URL."); // display an error message if the response is not successful
    }
  });

// Add event listener to the decode form
document
  .getElementById("decodeForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault(); // prevent default form submission behavior

    // Get the short URL from the input field
    const shortUrl = document.getElementById("decodeurl").value;

    // Send a POST request to the /decode/ URL to decode the URL
    const response = await fetch("/decode/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0]
          .value,
      },
      body: JSON.stringify({ short_url: shortUrl }), // converts to JSON for request
    });

    // If the response is successful, update the decoded URL text content
    if (response.ok) {
      const data = await response.json(); // get JSON data from response
      document.getElementById("decodedUrl").textContent = data.full_url; // update text content of HTML element
    } else {
      alert("Error decoding the URL."); // display an error message if the response is not successful
    }
  });
