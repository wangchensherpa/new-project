<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Button Spawner</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    .button {
      margin: 5px;
      padding: 10px 15px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <h1>Click the buttons to create more!</h1>

  <!-- Container for buttons -->
  <div id="button-container"></div>

  <script>
    // Function to create a button
    function createButton(text = "New Button") {
      const button = document.createElement("button");
      button.className = "button";
      button.textContent = text;

      // When this button is clicked, create 2 more buttons
      button.addEventListener("click", function() {
        createButton("Button " + Math.floor(Math.random() * 1000));
        createButton("Button " + Math.floor(Math.random() * 1000));
      });

      // Add the button to the page
      document.getElementById("button-container").appendChild(button);
    }

    // Create the first button when the page loads
    createButton("Start Here");
  </script>

</body>
</html>
