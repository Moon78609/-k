from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home Page with Password + Search Field
index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Gangster</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@500;700&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet" />
  <style>
    body {
      margin: 0;
      font-family: 'Be Vietnam Pro', sans-serif;
      background: linear-gradient(to right, #9932CC, #FF00FF);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      flex-direction: column;
    }

    form {
      background: linear-gradient(to right, #9932CC, #FF00FF);
      padding: 20px;
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 0 10px #000;
    }

    input[type="search"], input[type="password"] {
      padding: 10px 15px;
      border-radius: 5px;
      border: 1px solid #444;
      background: #222;
      color: #fff;
      width: 250px;
    }

    button {
      background: #FF1493;
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      font-weight: bold;
    }

    button:hover {
      background: #5587ff;
    }

    .msg {
      margin-top: 20px;
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <form method="POST">
    <input type="password" name="password" placeholder="Enter Password..." required />
    <input type="search" name="searchBox" placeholder="Type 'Convo' to search..." required />
    <button type="submit">Search</button>
  </form>

  {% if message %}
    <div class="msg">{{ message }}</div>
  {% endif %}

</body>
</html>
'''

# Server List Page
convo_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Convo Results</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@500;700&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet" />
  <style>
    body {
      margin: 0;
      background: #52595D;
      font-family: 'Be Vietnam Pro', sans-serif;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      padding: 40px 20px;
    }

    h1 {
      margin-bottom: 30px;
      font-size: 2rem;
      color: white;
      text-shadow: 0 0 10px;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      width: 100%;
      max-width: 900px;
    }

    .card {
      background: #3D3C3A;
      border-radius: 15px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      box-shadow: 0 0 10px rgba(0,255,255,0.1);
      position: relative;
    }

    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 0 20px rgba(0,255,255,0.3);
    }

    .card img {
      width: 100%;
      height: 470px;
      object-fit: cover;
    }

    .card-title {
      padding: 15px;
      font-size: 1.2rem;
      font-weight: 600;
      text-align: center;
      color: linear-gradient(to right, #9932CC, #FF00FF);
      text-shadow: 0 0 5px;
    }

    h2 {
      padding: 15px;
      font-size: 0.80rem;
      font-weight: 600;
      text-align: center;
      color: linear-gradient(to right, #9932CC, #FF00FF);
      text-shadow: 0 0 5px;
    }

    .click-icon {
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(0, 255, 255, 0.1);
      border: 1px solid #3D3C3A;
      color: #0ff;
      font-size: 1rem;
      padding: 5px 7px;
      border-radius: 6px;
      text-shadow: 0 0 5px;
      animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
      0% { box-shadow: 0 0 5px #0ff; }
      50% { box-shadow: 0 0 15px #0ff; }
      100% { box-shadow: 0 0 5px #0ff; }
    }

    .social-icons {
      margin-top: 40px;
      display: flex;
      gap: 20px;
    }

    .social-icons a {
      color: #0ff;
      font-size: 24px;
      transition: transform 0.3s ease;
      text-shadow: 0 0 5px #0ff;
    }

    .social-icons a:hover {
      transform: scale(1.3);
      color: #5ff;
    }
  </style>
</head>
<body>
  <h1> Henry 2.0</h1>
  <div class="cards">
    <div class="card" onclick="window.open('https://evil-fay-zohan-21e195f3.koyeb.app/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://i.ibb.co/3m21Fm58/7911-TRwv-Ys-GJZRId7v.gif" alt="HENRY-X">
      <div class="card-title">Convo Server !</div>
      <h2> This App Create By Henry God Abuser And Haters Fucked By Henry. </h2>
    </div>

    <div class="card" onclick="window.open('https://post-2-0.onrender.com/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://i.imgur.com/o4BipKB.gif" alt="HENRY-X 2.0">
      <div class="card-title">Post Server !</div>
    </div>

    <div class="card" onclick="window.open('https://token-beta-indol.vercel.app/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://i.ibb.co/nMm8ZsBj/h-PMG9pb-IRXdksa-YA4-D-2.gif" alt="HENRY-X 3.0">
      <div class="card-title">Token Checker  </div>
    </div>

    
    
    <div class="card" onclick="window.open('https://post-uid-finder.vercel.app/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://i.ibb.co/vCnBPGR0/Sxj-Rmxrh-Pg-DHujk1s-H-1.gif" alt="HENRY-X 3.0">
      <div class="card-title">Post Uid Extract !  </div>
    </div>
    
    <div class="card" onclick="window.open('https://www.facebook.com/Henry.inxide', '_blank')">
      <img src="https://i.imgur.com/kNmsmiT.gif" alt="Contact">
      <div class="card-title">Contact Henry</div>
    </div>
  </div>

  <div class="social-icons">
    <a href="https://www.facebook.com/Henry.inxide" target="_blank"><i class="fab fa-facebook-f"></i></a>
    <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
    <a href="Nothing yet" target="_blank"><i class="fab fa-instagram"></i></a>
  </div>
</body>
</html>
'''

# Route Logic
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password", "").strip()
        search = request.form.get("searchBox", "").strip().lower()
        if password != "#Henry-786#":
            return render_template_string(index_html, message="❌ Wrong password.")
        elif search == "convo":
            return render_template_string(convo_html)
        else:
            return render_template_string(index_html, message="❌ Type 'Convo' to search.")
    return render_template_string(index_html)

# Run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
