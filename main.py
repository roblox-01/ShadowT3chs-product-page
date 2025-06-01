from flask import Flask, Response, render_template_string, send_from_directory, request, send_file
import os

app = Flask(__name__)
app.config['SERVER_NAME'] = 'shadowt3ch.site'  # Replace with your main domain

@app.before_request
def log_request():
    print(f"Request received: {request.url}")

# Home page route
@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ShadowT3ch | Order Products</title>
  <meta name="description" content="Transforming Digital Possibilities with Premium Products">
  <link
    rel="icon"
    href="https://i.postimg.cc/y87h3x7y/0dc15569002a714e09ef3b03da9ac43d-removebg-preview.png"
    type="image/gif"
  />
  <link href="https://fonts.googleapis.com/css2?family=Play:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
  <style>
    #products .grid {
      display: grid;
      gap: 2rem;
      max-width: 60rem;
      margin: 0 auto;
    }
    #products .card {
      padding: 1.5rem;
      position: relative;
      transition: transform 0.1s ease;
    }
    #products .card:hover {
      animation: glitch 0.3s linear;
    }
    @keyframes glitch {
      0% { transform: translate(0); }
      20% { transform: translate(-2px, 2px); }
      40% { transform: translate(2px, -2px); }
      60% { transform: translate(-2px, 0); }
      80% { transform: translate(2px, 0); }
      100% { transform: translate(0); }
    }
    @media (min-width: 640px) { #products .grid { grid-template-columns: repeat(2, 1fr); } }
  </style>
</head>
<body>
  <div id="particles-js" class="fixed inset-0 z-0 size-full"></div>
  <div x-data="{ isNavOpen: false }">
    <nav>
      <div class="flex">
        <a href="/" class="text-2xl font-bold">ShadowT3ch</a>
        <button @click="isNavOpen = !isNavOpen" class="md:hidden text-white">
          <i class="fas fa-bars"></i>
        </button>
        <div class="nav-links" :class="{ 'show': isNavOpen }" x-cloak>
          <a href="/about">About</a>
          <div class="dropdown" x-data="{ isOpen: false }" @click.outside="isOpen = false">
            <div class="dropdown-toggle" @click="isOpen = !isOpen">
              Projects <i class="fas fa-caret-down"></i>
            </div>
            <div class="dropdown-menu" :class="{ 'show': isOpen }" x-cloak>
              <a href="/project-alpha">Project Alpha</a>
              <a href="/neural-net">Neural Net Playground</a>
              <a href="/cyber-dashboard">Cyber Dashboard</a>
              <a href="/shadow-executor">Shadow Executor</a>
              <a href="/streamflix">StreamFlix</a>
            </div>
          </div>
          <a href="/skills">Skills</a>
          <a href="/contact">Contact</a>
          <div class="dropdown" x-data="{ isOpen: false }" @click.outside="isOpen = false">
            <div class="dropdown-toggle" @click="isOpen = !isOpen">
              More <i class="fas fa-caret-down"></i>
            </div>
            <div class="dropdown-menu" :class="{ 'show': isOpen }" x-cloak>
              <div class="dropdown" x-data="{ isDeltaOpen: false }" @click.outside="isDeltaOpen = false">
                <div class="dropdown-toggle" @click="isDeltaOpen = !isDeltaOpen">
                  Delta <i class="fas fa-caret-down"></i>
                </div>
                <div class="dropdown-menu" :class="{ 'show': isDeltaOpen }" x-cloak>
                  <a href="/delta">Download</a>
                  <a href="/delta-status">Status</a>
                  <a href="/howto">How-To</a>
                </div>
              </div>
              <a href="/scripts">Scripts</a>
              <a href="/products">Products</a>
              <a href="/more">Other</a>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section id="products">
      <div>
        <h2 class="text-4xl font-bold mb-8 text-center">Order Products</h2>
        <div class="grid">
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowV3 Premium</h3>
            <p class="text-white/80 mb-4">Unlock exclusive features with ShadowV3 Premium subscription.</p>
            <a href="/shadowv3-premium" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowNuker 1 Month</h3>
            <p class="text-white/80 mb-4">Access ShadowNuker for 1 month with full features.</p>
            <a href="/shadownuker-1month" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowNuker 1 Week</h3>
            <p class="text-white/80 mb-4">Try ShadowNuker with a 1-week subscription.</p>
            <a href="/shadownuker-1week" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowNuker 1 Year</h3>
            <p class="text-white/80 mb-4">Get ShadowNuker for a full year at a discounted rate.</p>
            <a href="/shadownuker-1year" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowNuker Lifetime</h3>
            <p class="text-white/80 mb-4">Lifetime access to ShadowNuker with all updates included.</p>
            <a href="/shadownuker-lifetime" class="text-accent-text">Order Now</a>
          </div>
        </div>
      </div>
    </section>

    <footer>
      <p class="text-white/80">© 2025 ShadowT3ch</p>
    </footer>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.14.3/dist/cdn.min.js" integrity="sha256-aJ9ROXjRHWn00zeU9ylsmlhqLlXeebtEfN28P0dPnwc=" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js" integrity="sha256-7S7O87G2nAEPuwOKHszi0nERsH8O2rIHGVenRwtMgKk=" crossorigin="anonymous"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      particlesJS({
        particles: { number: { value: 50, density: { enable: true, value_area: 800 } }, color: { value: '#6571ff' }, opacity: { value: 0.5 }, size: { value: 3, random: true }, line_linked: { enable: true, distance: 150, color: '#6571ff', opacity: 0.4, width: 1 }, move: { enable: true, speed: 1, direction: 'none', out_mode: 'out' } },
        interactivity: { detect_on: 'canvas', events: { onhover: { enable: false }, onclick: { enable: false }, resize: true } },
        retina_detect: true
      });
    });
  </script>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
