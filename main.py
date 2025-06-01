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
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StreamFlix</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script type="importmap">
        {
            "imports": {
                "tmdb-api": "https://cdn.jsdelivr.net/npm/@markmotieno/tmdb-api@1.0.2/+esm"
            }
        }
    </script>
<script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'brand': {
                            'purple': '#6E2594',
                            'light': '#8A4FFF',
                            'dark': '#4d1bc8',
                            'darkpurple': '#341256'
                        }
                    }
                }
            }
        }
    </script>
</head>
  <style>
  .relative.bg-gradient-to-br.from-gray-900.to-brand-dark.rounded-xl.overflow-hidden {
    top: 10vh;
}
@media (max-width: 640px) {
  .container {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
  
  .featured-carousel {
    height: 40vh !important;
  }
  
  h2.text-3xl {
    font-size: 1.5rem;
  }
  
  #modal-content p {
    font-size: 0.875rem;
  }
  
  #chat-panel {
    width: 90% !important;
    right: 5% !important;
  }
}

.text-ellipsis {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.description-ellipsis {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (max-width: 768px) {
  .text-4xl {
    font-size: 1.75rem;
  }
  
  .text-3xl {
    font-size: 1.5rem;
  }
  
  .text-xl {
    font-size: 1.25rem;
  }
  
  .text-lg {
    font-size: 1.125rem;
  }
}
@media (max-width: 768px) {
  nav button.bg-gradient-to-r.from-brand-purple.to-brand-light {
    display: none !important;
  }
}
    #chatbot-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    transition: transform 0.3s ease;
}

#chatbot-widget {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #9c27b0, #673ab7);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(156, 39, 176, 0.4);
    transition: transform 0.3s ease;
}

#chatbot-widget:hover {
    transform: scale(1.1);
}

#chatbot-widget i {
    color: white;
    font-size: 24px;
}

#chatbot-panel {
    position: absolute;
    bottom: 80px;
    right: 0;
    width: 350px;
    height: 500px;
    background-color: rgba(0,0,0,0.6);
    backdrop-filter:blur(2rem);
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
    transform: translateY(120%);
    transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    overflow: hidden;
}

#chatbot-panel.active {
    transform: translateY(0);
}

#chatbot-header {
    background: linear-gradient(135deg, #9c27b0, #673ab7);
    color: white;<!DOCTYPE html>
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
            <h3 class="text-xl font-semibold mb-2">ShadowSync VPN</h3>
            <p class="text-white/80 mb-4">Secure and fast VPN service for anonymous browsing.</p>
            <a href="/shadowsync-vpn" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">Quantum Encryptor</h3>
            <p class="text-white/80 mb-4">Advanced encryption software for secure communications.</p>
            <a href="/quantum-encryptor" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">CyberShield Antivirus</h3>
            <p class="text-white/80 mb-4">Next-gen antivirus protection for all your devices.</p>
            <a href="/cybershield-antivirus" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">Neural Analytics Suite</h3>
            <p class="text-white/80 mb-4">AI-powered data analytics for actionable insights.</p>
            <a href="/neural-analytics" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">StreamFlix Premium</h3>
            <p class="text-white/80 mb-4">Ad-free streaming with exclusive content access.</p>
            <a href="/streamflix-premium" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowCloud Storage</h3>
            <p class="text-white/80 mb-4">Secure cloud storage with unlimited bandwidth.</p>
            <a href="/shadowcloud-storage" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">CodeMaster IDE</h3>
            <p class="text-white/80 mb-4">Integrated development environment for coders.</p>
            <a href="/codemaster-ide" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">AI Chatbot Pro</h3>
            <p class="text-white/80 mb-4">Customizable AI chatbot for business automation.</p>
            <a href="/aichatbot-pro" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">DarkNet Firewall</h3>
            <p class="text-white/80 mb-4">Robust firewall for advanced network security.</p>
            <a href="/darknet-firewall" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">Quantum Backup</h3>
            <p class="text-white/80 mb-4">Automated backup solution for data protection.</p>
            <a href="/quantum-backup" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowExecutor Pro</h3>
            <p class="text-white/80 mb-4">Advanced script execution tool for developers.</p>
            <a href="/shadowexecutor-pro" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">CryptoGuard Wallet</h3>
            <p class="text-white/80 mb-4">Secure cryptocurrency wallet for all major coins.</p>
            <a href="/cryptoguard-wallet" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">SmartHome Hub</h3>
            <p class="text-white/80 mb-4">Centralized control for your smart home devices.</p>
            <a href="/smarthome-hub" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">ShadowVPN Router</h3>
            <p class="text-white/80 mb-4">Pre-configured router for instant VPN protection.</p>
            <a href="/shadowvpn-router" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">DevOps Toolkit</h3>
            <p class="text-white/80 mb-4">Comprehensive tools for streamlined DevOps workflows.</p>
            <a href="/devops-toolkit" class="text-accent-text">Order Now</a>
          </div>
          <div class="card">
            <h3 class="text-xl font-semibold mb-2">AR Developer Kit</h3>
            <p class="text-white/80 mb-4">Tools and SDK for building augmented reality apps.</p>
            <a href="/ar-developer-kit" class="text-accent-text">Order Now</a>
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
