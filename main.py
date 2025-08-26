from flask import Flask, render_template_string, redirect
app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LOADING PLZ WAIT– Internet Check</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: black;
      font-family: Arial, sans-serif;
      color: white;
      text-align: center;
    }

    /* Bigger Video logo */
    .logo-video {
      width: 200px;
      height: 200px;
      border-radius: 50%;
      overflow: hidden;
      margin-bottom: 20px;
      animation: glowVideo 2s infinite alternate;
    }

    @keyframes glowVideo {
      from { box-shadow: 0 0 10px white; }
      to { box-shadow: 0 0 10px white; }
    }

    .logo-video video {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    /* Logo Name */
    .logo {
      font-size: 28px;
      font-weight: bold;
      margin-bottom: 25px;
      color: #fff;
      letter-spacing: 3px;
      text-transform: uppercase;
      animation: glowText 2s infinite alternate;
    }

    @keyframes glowText {
      from { text-shadow: 0 0 10px #ff4b2b, 0 0 20px #f9d423; }
      to { text-shadow: 0 0 10px #1e90ff, 0 0 40px #ff4b2b; }
    }

    /* Smaller Stylish Loader */
    .loader {
      position: relative;
      width: 50px;
      height: 50px;
      margin-bottom: 15px;
    }

    .ring {
      width: 100%;
      height: 100%;
      border: 4px solid transparent;
      border-top: 4px solid #ff4b2b;
      border-radius: 50%;
      position: absolute;
      top: 0;
      left: 0;
      animation: spin 1.5s linear infinite;
      box-shadow: 0 0 6px #ff4b2b;
    }

    .ring:nth-child(2) {
      border-top-color: #1e90ff;
      animation-delay: 0.3s;
      box-shadow: 0 0 6px #1e90ff;
    }

    .ring:nth-child(3) {
      border-top-color: #f9d423;
      animation-delay: 0.6s;
      box-shadow: 0 0 6px #f9d423;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    /* Counter */
    #counter {
      font-size: 34px;
      font-weight: bold;
      margin-top: 8px;
      animation: pulse 1s infinite alternate;
    }
    @keyframes pulse {
      from { color: #f9d423; text-shadow: 0 0 10px #ff4b2b; }
      to { color: #1e90ff; text-shadow: 0 0 15px #f9d423; }
    }

    /* Status Text */
    #status {
      margin-top: 12px;
      font-size: 16px;
      color: #bbb;
      animation: fade 2s infinite alternate;
    }
    @keyframes fade {
      from { opacity: 0.6; }
      to { opacity: 1; }
    }
  </style>
</head>
<body>
  <!-- Bigger Video Logo -->
  <div class="logo-video">
    <video autoplay muted loop playsinline>
      <source src="https://raw.githubusercontent.com/serverxdt/Approval/main/GOJO%20OR%20JIN-WOO.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>

  <!-- Logo Name -->
  <div class="logo">Loading Please Wait</div>

  <!-- Smaller Loader -->
  <div class="loader">
    <div class="ring"></div>
    <div class="ring"></div>
    <div class="ring"></div>
  </div>

  <!-- Countdown Display -->
  <div id="counter">3</div>

  <!-- Checking Status -->
  <div id="status">Checking Internet Connection...</div>

  <script>
    let seconds = 3;
    const counterElement = document.getElementById("counter");
    const statusElement = document.getElementById("status");

    const countdown = setInterval(() => {
      seconds--;
      counterElement.textContent = seconds;
      if (seconds <= 0) {
        clearInterval(countdown);
        checkInternet();
      }
    }, 1000);

    function checkInternet() {
      fetch("https://www.google.com/favicon.ico", { mode: 'no-cors' })
        .then(() => {
          window.location.href = "https://wispy-abagail-henrykingherw-ad0900ed.koyeb.app/";
        })
        .catch(() => {
          statusElement.textContent = "⚠️ Please Check Your Internet Connection";
          counterElement.style.display = "none";
        });
    }
  </script>
</body>
</html> """
@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
