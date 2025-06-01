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
    color: white;
    padding: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

#close-btn {
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    font-size: 18px;
}

#chat-messages {
    flex: 1;
    padding: 15px;
    overflow-y: auto;
}

.bot-message, .user-message {
    margin-bottom: 15px;
    max-width: 80%;
    padding: 10px 15px;
    border-radius: 18px;
    line-height: 1.4;
}

.bot-message {
    background-color: #f0f0f0;
    color: #333;
    border-top-left-radius: 5px;
    align-self: flex-start;
}

.user-message {
    background: linear-gradient(135deg, #9c27b0, #673ab7);
    color: white;
    border-top-right-radius: 5px;
    margin-left: auto;
    text-align: right;
    align-self: flex-end;
    font-weight:bold;
}

.message-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin-bottom: 15px;
}

.options-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 10px;
}

.option-button {
    background-color: #f0f0f0;
    border: 1px solid #ddd;
    border-radius: 15px;
    padding: 8px 12px;
    font-size: 14px;
    color:black;
    font-weight:bold;
    cursor: pointer;
    transition: background-color 0.3s;
}

.option-button:hover {
    background-color: #e0e0e0;
}

.movie-recommendation {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-top: 10px;
    color:black;
    background-color: #f9f9f9;
}

.movie-recommendation img {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 10px;
}

.movie-recommendation h4 {
    font-weight: bold;
    margin-bottom: 5px;
    color: #9c27b0;
}

.movie-recommendation p {
    font-size: 14px;
    color: #555;
    margin-bottom: 8px;
    line-height: 1.4;
}

#user-input-container {
    display: flex;
    padding: 15px;
    border-top: 1px solid #eee;
}

#user-input {
    flex: 1;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 20px;
    outline: none;
    font-size: 14px;
    color:black;
    font-weight:bold;
}

#send-btn {
    background: linear-gradient(135deg, #9c27b0, #673ab7);
    color: white;
    border: none;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-left: 10px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: background 0.3s;
    box-shadow: 0 2px 5px rgba(156, 39, 176, 0.3);
}

#send-btn:hover {
    background: linear-gradient(135deg, #8e24aa, #5e35b1);
}

#quiz-type-selector {
    display: flex;
    justify-content: center;
    margin: 15px 0;
    gap: 10px;
    flex-direction:column;
}

.quiz-type-btn {
    padding: 12px 15px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 500;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    gap: 8px;
    color:black;
}

.quiz-type-btn i {
    font-size: 16px;
}

.quiz-type-btn.active {
    background: linear-gradient(135deg, #9c27b0, #673ab7);
    color: white;
    box-shadow: 0 4px 10px rgba(156, 39, 176, 0.4);
}

#movie-search-results {
    position: absolute;
    bottom: 70px;
    left: 15px;
    right: 15px;
    max-height: 250px;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow-y: auto;
    z-index: 10;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    display: none;
}

.movie-search-item {
    display: flex;
    align-items: center;
    padding: 10px;
    cursor: pointer;
    border-bottom: 1px solid #eee;
}

.movie-search-item:hover {
    background-color: #f5f5f5;
}

.movie-search-item img {
    width: 40px;
    height: 60px;
    object-fit: cover;
    margin-right: 10px;
    border-radius: 3px;
}

.movie-search-item .movie-info {
    flex: 1;
}

.movie-search-item .movie-title {
    font-weight: bold;
    margin-bottom: 3px;
  color:black;
}

.movie-search-item .movie-year {
    font-size: 12px;
    color: #777;
}

.similar-movie {
    display: flex;
    margin-bottom: 12px;
    background-color: #f9f9f9;
    border-radius: 8px;
    overflow: hidden;
}

.similar-movie img {
    width: 80px;
    height: 120px;
    object-fit: cover;
}

.similar-movie-info {
    padding: 10px;
    flex: 1;
}

.similar-movie-title {
    font-weight: bold;
    margin-bottom: 5px;
    color: #9c27b0;
}

.similar-movie-year {
    font-size: 12px;
    color: #777;
    margin-bottom: 5px;
}

.similar-movie-overview {
    font-size: 12px;
    color: #555;
}

.similar-movies-container {
    margin-top: 10px;
    max-height: 300px;
    overflow-y: auto;
}

.content-type-selector {
    display: flex;
    justify-content: center;
    margin: 15px 0;
    gap: 10px;
}

.content-type-toggle {
    display: flex;
    background-color: #f0f0f0;
    border-radius: 25px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.content-type-btn {
    padding: 8px 15px;
    background: none;
    border: none;
    cursor: pointer;
    transition: all 0.3s;
    min-width: 80px;
  color:black;
}

.content-type-btn.active {
    background: linear-gradient(135deg, #9c27b0, #673ab7);
    color: white;
}

@media (max-width: 480px) {
    #chatbot-panel {
        width: 300px;
        bottom: 70px;
        right: 0;
    }
    
    #chatbot-widget {
        width: 50px;
        height: 50px;
    }
}
@media (max-width: 768px) {
  .md:flex-row {
    flex-direction: row;
  }
  #mOptions button{
      max-width:30%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin:0.1% auto;
    }
    #mOptions {
      display:flex;
      flex-direction:row;
      justify-content:center;
    }
}
  </style>
<body class="bg-gradient-to-br from-gray-900 via-brand-dark to-black min-h-screen text-white">
     <!-- Navigation -->
    <nav style="filter:brightness(120%) saturate(200%);" class="fixed top-0 w-full bg-gradient-to-r from-brand-darkpurple to-brand-purple z-50 backdrop-blur-md bg-opacity-90">
        <div class="container mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-8">
                    <h1 class="text-2xl font-bold bg-gradient-to-r from-brand-light to-purple-300 bg-clip-text text-transparent">StreamFlix</h1>
                    <div class="hidden md:flex space-x-6">
                        <a href="#" class="hover:text-brand-light transition-colors">Home</a>
                        <a href="#" class="hover:text-brand-light transition-colors">Movies</a>
                        <a href="#" class="hover:text-brand-light transition-colors">TV Shows</a>
                        <a href="#" class="hover:text-brand-light transition-colors">My List</a>
                    </div>
                </div>
                
                <!-- Search Bar -->
                <div class="flex-1 max-w-xl mx-8">
                    <div class="relative">
                        <input 
                            type="text" 
                            id="search-input"
                            placeholder="Search movies and shows..."
                            class="w-full bg-gray-800 bg-opacity-50 rounded-full px-6 py-2 focus:outline-none focus:ring-2 focus:ring-brand-light placeholder-gray-400"
                        >
                        <button 
                            onclick="searchMovies()"
                            class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-brand-light"
                        >
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    <main style="filter: saturate(200%);" class="container mx-auto px-4 pt-24 pb-8">
        <section class="mb-12">
            <h2 class="text-xl font-semibold mb-6 bg-gradient-to-r from-purple-300 to-brand-light bg-clip-text text-transparent">Featured</h2>
            <div class="featured-carousel relative h-[50vh] rounded-xl overflow-hidden">
            </div>
        </section>
        <section>
            <h2 class="text-xl font-semibold mb-6 bg-gradient-to-r from-purple-300 to-brand-light bg-clip-text text-transparent">Trending Now</h2>
            <div id="movies-grid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4"></div>
        </section>
    </main>

    <div id="player-modal" class="hidden fixed inset-0 z-50 bg-black">
        <button onclick="closePlayer()" class="absolute top-1 left-2 text-white z-10">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
        </button>
        <iframe id="movie-player" class="w-full h-full" frameborder="0" allowfullscreen></iframe>
    </div>

    <div id="details-modal" class="hidden fixed inset-0 z-40 overflow-auto bg-black bg-opacity-90">
        <div class="container mx-auto px-4 py-8">
            <div class="relative bg-gradient-to-br from-gray-900 to-brand-dark rounded-xl overflow-hidden">
                <div id="modal-content" class="p-6"></div>
            </div>
        </div>
    </div>
<div id="chatbot-container">
        <div id="chatbot-widget">
            <i class="fas fa-film"></i>
        </div>
        
        <div id="chatbot-panel">
            <div id="chatbot-header">
              <h3><b>Flicky</b></h3>
                <button id="close-btn"><i class="fas fa-times"></i></button>
            </div>
            
            <div id="chat-messages">
            </div>
            
            <div id="user-input-container">
                <input type="text" id="user-input" placeholder="Type your answer here...">
                <button id="send-btn"><i class="fas fa-paper-plane"></i></button>
            </div>
        </div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>

    <script>
        const TMDB_API_KEY = 'e479c27ddf18512de2bbc883c3612637';
        const TMDB_BASE_URL = 'https://api.themoviedb.org/3';
let currentMediaType = 'movie';
let currentShowDetails = null;
let currentPlayerSource = 'vidsrc.su';
let currentSeason = 1;
        async function fetchMovies() {
    showLoading();
    try {
        const [movieResponse, showResponse] = await Promise.all([
            fetch(`${TMDB_BASE_URL}/trending/movie/week?api_key=${TMDB_API_KEY}`),
            fetch(`${TMDB_BASE_URL}/trending/tv/week?api_key=${TMDB_API_KEY}`)
        ]);
                const movieData = await movieResponse.json();
        const showData = await showResponse.json();

        movies = [...movieData.results.map(movie => ({
            id: movie.id,
            title: movie.title,
            year: new Date(movie.release_date).getFullYear(),
            description: movie.overview,
            poster_path: movie.poster_path,
            backdrop_path: movie.backdrop_path,
            rating: movie.vote_average,
            media_type: 'movie'
        })),
        ...showData.results.map(show => ({
            id: show.id,
            title: show.name,
            year: new Date(show.first_air_date).getFullYear(),
            description: show.overview,
            poster_path: show.poster_path,
            backdrop_path: show.backdrop_path,
            rating: show.vote_average,
            media_type: 'tv'
        }))];
        
        renderMovies();
        renderFeatured(movies[0]);
    } catch (error) {
        showError('Failed to load content');
    } finally {
        hideLoading();
    }
}


function renderMovies() {
  const grid = document.getElementById('movies-grid');
  grid.innerHTML = movies.map(media => `
    <div onclick="selectMedia(${media.id}, '${media.media_type}')" 
         class="relative group cursor-pointer transform hover:scale-105 transition-transform duration-200">
      <div class="absolute inset-0 bg-gradient-to-t from-black to-transparent opacity-0 group-hover:opacity-100 transition-opacity rounded-lg"></div>
      <img src="https://image.tmdb.org/t/p/w500${media.poster_path}" 
           alt="${media.title}" 
           class="w-full aspect-[2/3] object-cover rounded-lg" 
           loading="lazy">
      <div class="absolute bottom-0 left-0 right-0 p-4 opacity-0 group-hover:opacity-100 transition-opacity">
        <h3 class="text-white text-sm font-semibold text-ellipsis">${media.title}</h3>
        <div class="flex items-center justify-between mt-1">
          <div class="flex items-center">
            <span class="text-yellow-400 text-xs">★</span>
            <span class="ml-1 text-white text-xs">${media.rating.toFixed(1)}</span>
          </div>
          <span class="text-white text-xs uppercase">${media.media_type}</span>
        </div>
      </div>
    </div>
  `).join('');
}

function renderFeatured(media) {
  const featured = document.querySelector('.featured-carousel');
  featured.innerHTML = `
    <div class="relative w-full h-full">
      <div class="absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent"></div>
      <img src="https://image.tmdb.org/t/p/original${media.backdrop_path}" 
           alt="${media.title}" 
           class="w-full h-full object-cover">
      <div class="absolute bottom-0 left-0 right-0 p-8">
        <h2 class="text-4xl font-bold mb-2 text-ellipsis">${media.title}</h2>
        <p class="text-gray-200 max-w-2xl mb-4 description-ellipsis">${media.description}</p>
        <button onclick="selectMedia(${media.id}, '${media.media_type}')" 
                class="bg-brand-light hover:bg-brand-purple px-6 py-3 rounded-full transition-colors">
          Watch Now
        </button>
      </div>
    </div>
  `;
}
        async function selectMedia(mediaId, mediaType) {
    const details = await fetchMediaDetails(mediaId, mediaType);
    if (details) {
        currentMediaType = mediaType;
        currentShowDetails = details;
        showMediaDetails(details);
    }
}

function showMediaDetails(media) {
  const modal = document.getElementById('details-modal');
  const content = document.getElementById('modal-content');
  
  const playButton = media.media_type === 'movie' 
    ? `<div class="flex flex-col items-center">
         <button onclick="playMedia(${media.id}, '${media.media_type}')" 
                 class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-brand-light hover:bg-brand-purple w-16 h-16 rounded-full flex items-center justify-center transition-colors">
           <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
           </svg>
         </button>
<div id="mOptions" class="absolute bottom-20 flex justify-center w-full space-x-2 md:flex-row flex-col">
  <br>
  <button onclick="setPlayerSource('player.videasy.net')" class="px-3 py-1 bg-brand-dark bg-opacity-90 hover:bg-brand-purple rounded text-sm player-btn active">
    videasy
  </button>
  <button onclick="setPlayerSource('vidsrc.su')" class="px-3 py-1 bg-brand-dark bg-opacity-90 hover:bg-brand-purple rounded text-sm player-btn">
    vidsrc
  </button>
  <button onclick="setPlayerSource('embed.su')" class="px-3 py-1 bg-brand-dark bg-opacity-90 hover:bg-brand-purple rounded text-sm player-btn">
    embed
  </button>
</div>
       </div>`
    : `
<div id="mOptions" class="absolute bottom-20 flex justify-center w-full space-x-2 md:flex-row flex-col">
          <br>
          <button onclick="setPlayerSource('player.videasy.net')" class="px-3 py-1 bg-brand-dark bg-opacity-90 hover:bg-brand-purple rounded text-sm player-btn active">
             player.videasy.net
           </button>
           <br>
           <button onclick="setPlayerSource('vidsrc.su')" class="px-4 py-2 bg-brand-light hover:bg-brand-purple rounded text-sm player-btn">
           vidsrc.su
         </button>
         <br>
         <button onclick="setPlayerSource('embed.su')" class="px-4 py-2 bg-brand-light hover:bg-brand-purple rounded text-sm player-btn">
           embed.su
         </button>
       </div>`;

  content.innerHTML = `
    <button style="z-index:2; border-radius:50%; background: rgba(51, 51, 51, 0.6);" 
            onclick="closeDetails()" 
            class="absolute top-4 right-4 text-white">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
    </button>
    <div class="relative h-[50%] mb-6">
      <div class="absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent"></div>
      <img src="https://image.tmdb.org/t/p/original${media.backdrop_path}" 
           alt="${media.title}" 
           class="w-full h-80 object-cover">
      ${playButton}
    </div>
    <div class="space-y-4">
      <h2 class="text-3xl font-bold text-ellipsis">${media.title}</h2>
      <div class="flex flex-wrap items-center gap-4">
        <span>${media.year}</span>
        <span>${media.length}</span>
        ${media.media_type === 'tv' ? `<span>${media.seasons} Seasons</span>` : ''}
        <span class="flex items-center">
          <svg class="w-4 h-4 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
          </svg>
          <span class="ml-1">${media.rating}</span>
        </span>
      </div>
      <p class="text-gray-300 description-ellipsis">${media.description}</p>
      
      ${media.media_type === 'tv' ? renderEpisodeList(media) : ''}
    </div>
  `;
  
  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

      async function changeSeason(showId, seasonNumber) {
    currentSeason = seasonNumber;
    try {
        const seasonResponse = await fetch(
            `${TMDB_BASE_URL}/tv/${showId}/season/${seasonNumber}?api_key=${TMDB_API_KEY}`
        );
        const seasonData = await seasonResponse.json();
        
        currentShowDetails.seasonData = seasonData.episodes.map(ep => ({
            episode_number: ep.episode_number,
            name: ep.name,
            overview: ep.overview,
            still_path: ep.still_path,
            runtime: ep.runtime,
            air_date: ep.air_date
        }));
        
        const episodeListContainer = document.querySelector('.episode-grid').parentElement;
        episodeListContainer.innerHTML = renderEpisodeList(currentShowDetails);
    } catch (error) {
        console.error('Error changing season:', error);
        showError('Failed to load season data');
    }
}

function renderEpisodeList(show) {
    let seasonSelector = '<div class="flex items-center mb-4">';
    seasonSelector += '<label class="mr-2 text-sm">Season:</label>';
    seasonSelector += '<div class="flex space-x-2 overflow-x-auto pb-2">';
    
    for (let i = 1; i <= show.seasons; i++) {
        seasonSelector += `
            <button onclick="changeSeason(${show.id}, ${i})" 
                    class="px-3 py-1 bg-gray-800 rounded-md text-sm ${currentSeason === i ? 'bg-brand-light' : 'hover:bg-gray-700'}">
                ${i}
            </button>
        `;
    }
    
    seasonSelector += '</div></div>';

    return `
        <div class="mt-8">
            <h3 class="text-xl font-semibold mb-4">Episodes</h3>
            ${seasonSelector}
            <div class="episode-grid grid gap-4 max-h-96 overflow-y-auto pr-2">
                ${show.seasonData.map(ep => `
                    <div class="episode-card bg-gray-800 rounded-lg overflow-hidden cursor-pointer transform hover:scale-102 transition-transform duration-200"
                         onclick="playMedia(${show.id}, 'tv', ${ep.episode_number})">
                        <div class="flex flex-col md:flex-row">
                            <div class="md:w-1/3 relative">
                                <img src="${ep.still_path ? `https://image.tmdb.org/t/p/w300${ep.still_path}` : '/placeholder-episode.jpg'}" 
                                     alt="Episode ${ep.episode_number}" 
                                     class="w-full h-full object-cover"
                                     onerror="this.onerror=null; this.src='https://via.placeholder.com/300x170?text=No+Image';">
                                <div class="absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent opacity-60"></div>
                                <div class="absolute bottom-2 left-2 bg-brand-light text-white text-xs px-2 py-1 rounded-md">
                                    EP ${ep.episode_number}
                                </div>
                                <div class="absolute top-2 right-2">
                                    <button class="bg-brand-light hover:bg-brand-purple rounded-full w-8 h-8 flex items-center justify-center">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                            <div class="p-3 md:w-2/3">
                                <h4 class="font-medium text-lg">${ep.name}</h4>
                                <p class="text-gray-400 text-sm my-1">${ep.runtime ? ep.runtime + ' min' : ''}</p>
                                <p class="text-sm text-gray-300 line-clamp-2">${ep.overview || 'No description available.'}</p>
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

      
      function showMovieDetails(movie) {
            const modal = document.getElementById('details-modal');
            const content = document.getElementById('modal-content');
            
            content.innerHTML = `
                <button onclick="closeDetails()" class="absolute top-4 right-4 text-white">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                    </svg>
                </button>
                
                <div class="relative h-[50vh] mb-6">
                    <div class="absolute inset-0 bg-gradient-to-t from-gray-900 to-transparent"></div>
                    <img 
                        src="https://image.tmdb.org/t/p/original${movie.backdrop_path}"
                        alt="${movie.title}"
                        class="w-full h-full object-cover"
                    >
                    <button 
                        onclick="playMovie(${movie.id})"
                        class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-brand-light hover:bg-brand-purple w-16 h-16 rounded-full flex items-center justify-center transition-colors"
                    >
                        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                    </button>
                </div>
                
                <div class="space-y-4">
                    <h2 class="text-3xl font-bold">${movie.title}</h2>
                    <div class="flex items-center space-x-4">
                        <span>${movie.year}</span>
                        <span>${movie.length}</span>
                        <span class="flex items-center">
                            <svg class="w-4 h-4 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                            </svg>
                            <span class="ml-1">${movie.rating}</span>
                        </span>
                    </div>
                    <p class="text-gray-300">${movie.description}</p>
                    
                </div>
            `;
            
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }

async function fetchMediaDetails(id, mediaType) {
    try {
        const response = await fetch(
            `${TMDB_BASE_URL}/${mediaType}/${id}?api_key=${TMDB_API_KEY}&append_to_response=credits`
        );
        const data = await response.json();

        if (mediaType === 'tv') {
            const seasonResponse = await fetch(
                `${TMDB_BASE_URL}/tv/${id}/season/${currentSeason}?api_key=${TMDB_API_KEY}`
            );
            const seasonData = await seasonResponse.json();

            return {
                id: data.id,
                title: data.name,
                year: new Date(data.first_air_date).getFullYear(),
                description: data.overview,
                backdrop_path: data.backdrop_path,
                poster_path: data.poster_path,
                rating: data.vote_average,
                length: `${data.episode_run_time[0] || 'N/A'} min per ep`,
                media_type: 'tv',
                seasons: data.number_of_seasons,
                episodes: seasonData.episodes.length,
                seasonData: seasonData.episodes.map(ep => ({
                    episode_number: ep.episode_number,
                    name: ep.name,
                    overview: ep.overview,
                    still_path: ep.still_path,
                    runtime: ep.runtime,
                    air_date: ep.air_date
                }))
            };
        } else {
            return {
                id: data.id,
                title: data.title,
                year: new Date(data.release_date).getFullYear(),
                description: data.overview,
                backdrop_path: data.backdrop_path,
                poster_path: data.poster_path,
                rating: data.vote_average,
                length: `${data.runtime} min`,
                media_type: 'movie'
            };
        }
    } catch (error) {
        console.error('Error fetching media details:', error);
        showError('Failed to load details');
        return null;
    }
}
      
function setPlayerSource(source) {
  currentPlayerSource = source;
  
  document.querySelectorAll('.player-btn').forEach(btn => {
    btn.classList.remove('bg-brand-purple');
    if (btn.textContent.trim() === source) {
      btn.classList.add('bg-brand-purple');
    }
  });
}

function playMedia(mediaId, mediaType, episodeNumber = null) {
  const player = document.getElementById('player-modal');
  const iframe = document.getElementById('movie-player');
  const chatbotWidget = document.getElementById('chatbot-container');
    const chatbotPanel = document.getElementById('chatbot-panel');

  if (mediaType === 'tv') {
    let episode = episodeNumber;
    if (!episode) {
      const episodeSelect = document.getElementById('episode-select');
      if (episodeSelect) {
        episode = episodeSelect.value;
      } else {
        episode = 1; 
      }
    }
    
    if (currentPlayerSource === 'vidsrc.su') {
      iframe.src = `https://vidsrc.su/embed/tv/${mediaId}/${currentSeason}/${episode}`;
    } else if (currentPlayerSource === 'embed.su') {
      iframe.src = `https://embed.su/embed/tv/${mediaId}/${episode}`;
    } else if (currentPlayerSource === 'player.videasy.net') {
      iframe.src = `https://player.videasy.net/tv/${mediaId}/${currentSeason}/${episode}?nextEpisode=true&autoplayNextEpisode=true&episodeSelector=true&color=8B5CF6`;
    }
  } else {
    if (currentPlayerSource === 'vidsrc.su') {
      iframe.src = `https://vidsrc.su/embed/movie/${mediaId}`;
    } else if (currentPlayerSource === 'embed.su') {
      iframe.src = `https://embed.su/embed/movie/${mediaId}`;
    } else if (currentPlayerSource === 'player.videasy.net') {
      iframe.src = `https://player.videasy.net/movie/${mediaId}?nextEpisode=true&autoplayNextEpisode=true&episodeSelector=true&color=8B5CF6`;
    }
  }
  
  if (chatbotWidget) {
    chatbotWidget.style = 'transform:scale(0);';
    chatbotPanel.style = 'visibility:hidden;';
  }
  
  player.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

      
const additionalStyles = document.createElement('style');
additionalStyles.textContent = `
    .episode-grid {
        display: grid;
        grid-template-columns: 1fr;
    }
    
    @media (min-width: 640px) {
        .episode-grid {
            grid-template-columns: repeat(1, 1fr);
        }
    }
    
    .line-clamp-2 {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    
    /* Custom scrollbar for episode list */
    .episode-grid::-webkit-scrollbar {
        width: 4px;
    }
    
    .episode-grid::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    .episode-grid::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }
    
    .episode-grid::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.3);
    }
    
    /* Season selector scrollbar */
    div.flex.space-x-2.overflow-x-auto::-webkit-scrollbar {
        height: 4px;
    }
    
    div.flex.space-x-2.overflow-x-auto::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    div.flex.space-x-2.overflow-x-auto::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }
`;
document.head.appendChild(additionalStyles);
      
function closePlayer() {
  const player = document.getElementById('player-modal');
  const iframe = document.getElementById('movie-player');
  const chatbotWidget = document.getElementById('chatbot-container');
  const chatbotPanel = document.getElementById('chatbot-panel');

  if (chatbotWidget) {
    chatbotWidget.style = 'transform:scale(1);';
    chatbotPanel.style = 'visibility:visible;';
  }
  
  iframe.src = '';
  player.classList.add('hidden');
  document.body.style.overflow = '';
}

function closeDetails() {
  const modal = document.getElementById('details-modal');
  const chatbotWidget = document.getElementById('chatbot-container');
  const chatbotPanel = document.getElementById('chatbot-panel');

  if (chatbotWidget) {
    chatbotWidget.style = "transform:scale(1);";
    chatbotPanel.style = 'visibility:visible;';
  }
  
  modal.classList.add('hidden');
  document.body.style.overflow = '';
}
window.addEventListener("message", function (event) {
  console.log("Message received from the player: ", JSON.parse(event.data)); // Message received from player
  if (typeof event.data === "string") {
    var messageArea = document.querySelector("#messageArea");
    messageArea.innerText = event.data;
  }
});

async function searchMovies() {
    const query = document.getElementById('search-input').value.trim();
    if (!query) return;

    showLoading();
    try {
        const [movieResponse, tvResponse] = await Promise.all([
            fetch(`${TMDB_BASE_URL}/search/movie?api_key=${TMDB_API_KEY}&query=${encodeURIComponent(query)}`),
            fetch(`${TMDB_BASE_URL}/search/tv?api_key=${TMDB_API_KEY}&query=${encodeURIComponent(query)}`)
        ]);
        
        const movieData = await movieResponse.json();
        const tvData = await tvResponse.json();
        
        const moviesWithDetails = await Promise.all(movieData.results.map(async (movie) => {
            try {
                const detailsResponse = await fetch(
                    `${TMDB_BASE_URL}/movie/${movie.id}?api_key=${TMDB_API_KEY}&append_to_response=credits`
                );
                const detailsData = await detailsResponse.json();
                return {
                    id: movie.id,
                    title: movie.title,
                    year: movie.release_date ? new Date(movie.release_date).getFullYear() : 'N/A',
                    description: movie.overview,
                    poster_path: movie.poster_path,
                    backdrop_path: detailsData.backdrop_path || movie.backdrop_path,
                    rating: detailsData.vote_average || movie.vote_average,
                    media_type: 'movie'
                };
            } catch (e) {
                return {
                    id: movie.id,
                    title: movie.title,
                    year: movie.release_date ? new Date(movie.release_date).getFullYear() : 'N/A',
                    description: movie.overview,
                    poster_path: movie.poster_path,
                    backdrop_path: movie.backdrop_path,
                    rating: movie.vote_average,
                    media_type: 'movie'
                };
            }
        }));
        
        const showsWithDetails = await Promise.all(tvData.results.map(async (show) => {
            try {
                const detailsResponse = await fetch(
                    `${TMDB_BASE_URL}/tv/${show.id}?api_key=${TMDB_API_KEY}&append_to_response=credits`
                );
                const detailsData = await detailsResponse.json();
                return {
                    id: show.id,
                    title: show.name,
                    year: show.first_air_date ? new Date(show.first_air_date).getFullYear() : 'N/A',
                    description: show.overview,
                    poster_path: show.poster_path,
                    backdrop_path: detailsData.backdrop_path || show.backdrop_path,
                    rating: detailsData.vote_average || show.vote_average,
                    media_type: 'tv'
                };
            } catch (e) {
                return {
                    id: show.id,
                    title: show.name,
                    year: show.first_air_date ? new Date(show.first_air_date).getFullYear() : 'N/A',
                    description: show.overview,
                    poster_path: show.poster_path,
                    backdrop_path: show.backdrop_path,
                    rating: show.vote_average,
                    media_type: 'tv'
                };
            }
        }));
        
        movies = [...moviesWithDetails, ...showsWithDetails].filter(item => item.poster_path);
        
        renderMovies();
        if (movies.length > 0) {
            renderFeatured(movies[0]);
        } else {
            showError('No results found');
        }
    } catch (error) {
        console.error('Search error:', error);
        showError('Failed to search content');
    } finally {
        hideLoading();
    }
}

        function toggleMobileMenu() {
            const mobileMenu = document.querySelector('.mobile-menu');
            mobileMenu.classList.toggle('hidden');
        }

        function showLoading() {
            const spinner = document.createElement('div');
            spinner.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
            spinner.innerHTML = `
                <div class="relative">
                    <div class="w-16 h-16 border-4 border-brand-light border-t-transparent rounded-full animate-spin"></div>
                    <div class="absolute inset-0 flex items-center justify-center">
                        <div class="w-8 h-8 bg-brand-light rounded-full"></div>
                    </div>
                </div>
            `;
            document.body.appendChild(spinner);
        }

        function hideLoading() {
            const spinner = document.querySelector('.bg-black.bg-opacity-50');
            if (spinner) spinner.remove();
        }

        function showError(message) {
            const toast = document.createElement('div');
            toast.className = 'fixed top-4 right-4 bg-red-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 animate-fade-in';
            toast.innerHTML = message;
            document.body.appendChild(toast);
            setTimeout(() => {
                toast.remove();
            }, 3000);
        }

        document.addEventListener('DOMContentLoaded', () => {
            fetchMovies();
            
            document.getElementById('search-input').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    searchMovies();
                }
            });

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    closePlayer();
                    closeDetails();
                }
            });

            window.addEventListener('resize', () => {
                if (window.innerWidth >= 768) {
                    document.querySelector('.mobile-menu')?.classList.add('hidden');
                }
            });
        });

        const customStyles = document.createElement('style');
        customStyles.textContent = `
            @keyframes fade-in {
                from { opacity: 0; transform: translateY(-1rem); }
                to { opacity: 1; transform: translateY(0); }
            }
            .animate-fade-in {
                animation: fade-in 0.3s ease-out;
            }
            .movie-card-hover {
                transition: transform 0.3s ease-out;
            }
            .movie-card-hover:hover {
                transform: scale(1.05);
            }
            .modal-enter {
                animation: modal-enter 0.3s ease-out;
            }
            @keyframes modal-enter {
                from { opacity: 0; transform: scale(0.95); }
                to { opacity: 1; transform: scale(1); }
            }
        `;
        document.head.appendChild(customStyles);

const API_KEY = 'e479c27ddf18512de2bbc883c3612637';
const BASE_URL = 'https://api.themoviedb.org/3';
const IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500';
const AI21_API_KEY = 'vKUeSkCw6NILYXg7GZ4ls7iNmiJCqBpG';

const chatbotWidget = document.getElementById('chatbot-widget');
const chatbotPanel = document.getElementById('chatbot-panel');
const closeBtn = document.getElementById('close-btn');
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

      let chatHistory = [
    {
        "role": "system",
        "content": "You are Flicky, a friendly and totally cool entertainment-focused AI assistant. Your primary goal is to help users find movies and TV shows that are, like, totally awesome. Keep responses smooth, conversational, and sound cool and use slang. You can discuss entertainment topics in depth, but you're also happy to chat about other subjects when the user wants to. When responding, feel free to use the following emojis: 😎, 🍿, 🎬, 🎥, and 👍 to add some flair and keep your responses fresh, fun, and movie-tastic!"
    }
];
      
let quizState = {
    currentStep: 0,
    userResponses: {
        genre: '',
        mood: '',
        era: ''
    },
    quizType: 'preferences', 
    contentType: 'movie', 
    selectedMovie: null
};

function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

const quizFlow = [
    {
        question: "Hi there! I'm **Flicky**, your personal entertainment matchmaker. Let me find the perfect content for you! What genre are you in the mood for today?",
        options: ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Adventure", "Fantasy"],
        responseKey: "genre"
    },
    {
        question: "Great choice! Now, what kind of mood are you in?",
        options: ["Uplifting", "Intense", "Thought-provoking", "Relaxing", "Emotional"],
        responseKey: "mood"
    },
    {
        question: "Last question: Do you prefer modern content or classics?",
        options: ["Modern (2000s and newer)", "Classics (pre-2000s)", "Both are fine"],
        responseKey: "era"
    }
];

const presetMovies = {
    action: ["Die Hard", "John Wick", "The Dark Knight", "Mad Max: Fury Road", "Mission: Impossible"],
    comedy: ["Superbad", "The Hangover", "Bridesmaids", "Anchorman", "Step Brothers"],
    drama: ["The Shawshank Redemption", "The Godfather", "Schindler's List", "Forrest Gump", "The Social Network"],
    horror: ["The Exorcist", "Hereditary", "Get Out", "The Shining", "A Quiet Place"],
    scifi: ["Inception", "The Matrix", "Interstellar", "Blade Runner", "Arrival"],
    romance: ["The Notebook", "Pride and Prejudice", "La La Land", "Eternal Sunshine of the Spotless Mind", "When Harry Met Sally"],
    adventure: ["Indiana Jones", "The Lord of the Rings", "Pirates of the Caribbean", "Jurassic Park", "Avatar"],
    fantasy: ["Harry Potter", "The Lord of the Rings", "Pan's Labyrinth", "The Princess Bride", "The Chronicles of Narnia"]
};

const presetTVShows = {
    action: ["Game of Thrones", "The Boys", "Daredevil", "24", "Vikings"],
    comedy: ["The Office", "Friends", "Brooklyn Nine-Nine", "Parks and Recreation", "The Good Place"],
    drama: ["Breaking Bad", "The Wire", "The Crown", "Succession", "Better Call Saul"],
    horror: ["Stranger Things", "The Haunting of Hill House", "American Horror Story", "Black Mirror", "The Walking Dead"],
    scifi: ["Westworld", "The Expanse", "Stranger Things", "Black Mirror", "Doctor Who"],
    romance: ["Bridgerton", "Normal People", "Outlander", "Jane the Virgin", "Lovesick"],
    adventure: ["The Mandalorian", "Lost", "The Witcher", "Stranger Things", "His Dark Materials"],
    fantasy: ["Game of Thrones", "The Witcher", "Shadow and Bone", "The Umbrella Academy", "Locke & Key"]
};

chatbotWidget.addEventListener('click', toggleChatPanel);
closeBtn.addEventListener('click', toggleChatPanel);
sendBtn.addEventListener('click', handleUserInput);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleUserInput();
    }
});

function toggleChatPanel() {
    chatbotPanel.classList.toggle('active');
}

function initChatbot() {
    const quizTypeMessage = document.createElement('div');
    quizTypeMessage.className = 'message-container';
    
    const botMessage = document.createElement('div');
    botMessage.className = 'bot-message';
    botMessage.innerHTML = "Welcome to <b>Flicky</b>! First, choose what type of content you'd like recommendations for:";
    quizTypeMessage.appendChild(botMessage);
    
    const contentTypeSelector = document.createElement('div');
    contentTypeSelector.className = 'content-type-selector';
    
    const contentTypeToggle = document.createElement('div');
    contentTypeToggle.className = 'content-type-toggle';
    
    const movieBtn = document.createElement('button');
    movieBtn.className = 'content-type-btn active';
    movieBtn.innerHTML = '<i class="fas fa-film"></i> Movies';
    movieBtn.addEventListener('click', () => {
        switchContentType('movie');
        movieBtn.classList.add('active');
        tvBtn.classList.remove('active');
    });
    
    const tvBtn = document.createElement('button');
    tvBtn.className = 'content-type-btn';
    tvBtn.innerHTML = '<i class="fas fa-tv"></i> TV Shows';
    tvBtn.addEventListener('click', () => {
        switchContentType('tv');
        tvBtn.classList.add('active');
        movieBtn.classList.remove('active');
    });
    
    contentTypeToggle.appendChild(movieBtn);
    contentTypeToggle.appendChild(tvBtn);
    contentTypeSelector.appendChild(contentTypeToggle);
    quizTypeMessage.appendChild(contentTypeSelector);
    
    const quizSelectionMessage = document.createElement('div');
    quizSelectionMessage.className = 'bot-message';
    quizSelectionMessage.style.marginTop = '15px';
    quizSelectionMessage.textContent = "Now, how would you like to get recommendations?";
    quizTypeMessage.appendChild(quizSelectionMessage);
    
    const quizTypeSelector = document.createElement('div');
    quizTypeSelector.id = 'quiz-type-selector';
    
    const preferencesBtn = document.createElement('button');
    preferencesBtn.className = 'quiz-type-btn active';
    preferencesBtn.innerHTML = '<i class="fas fa-question-circle"></i> Answer quiz questions';
    preferencesBtn.addEventListener('click', () => {
        startPreferencesQuiz();
        preferencesBtn.classList.add('active');
        similarBtn.classList.remove('active');
        summaryBtn.classList.remove('active');
        chatBtn.classList.remove('active');
    });
    
    const similarBtn = document.createElement('button');
    similarBtn.className = 'quiz-type-btn';
    similarBtn.innerHTML = '<i class="fas fa-heart"></i> Tell me what you like';
    similarBtn.addEventListener('click', () => {
        startSimilarMoviesQuiz();
        similarBtn.classList.add('active');
        preferencesBtn.classList.remove('active');
        summaryBtn.classList.remove('active');
        chatBtn.classList.remove('active');
    });
    
    const summaryBtn = document.createElement('button');
    summaryBtn.className = 'quiz-type-btn';
    summaryBtn.innerHTML = '<i class="fas fa-info-circle"></i> Get a summary';
    summaryBtn.addEventListener('click', () => {
        startSummaryMode();
        summaryBtn.classList.add('active');
        preferencesBtn.classList.remove('active');
        similarBtn.classList.remove('active');
        chatBtn.classList.remove('active');
    });
    
    const chatBtn = document.createElement('button');
    chatBtn.className = 'quiz-type-btn';
    chatBtn.innerHTML = '<i class="fas fa-comment"></i> General Chat';
    chatBtn.addEventListener('click', () => {
        startGeneralChatMode();
        chatBtn.classList.add('active');
        preferencesBtn.classList.remove('active');
        similarBtn.classList.remove('active');
        summaryBtn.classList.remove('active');
    });
    
    quizTypeSelector.appendChild(preferencesBtn);
    quizTypeSelector.appendChild(similarBtn);
    quizTypeSelector.appendChild(summaryBtn);
    quizTypeSelector.appendChild(chatBtn);
    
    quizTypeMessage.appendChild(quizTypeSelector);
    chatMessages.appendChild(quizTypeMessage);
}
      
function switchContentType(type) {
    quizState.contentType = type;
    userInput.placeholder = type === 'movie' ? 
        "Type a movie title..." : 
        "Type a TV show title...";
}

 function startGeneralChatMode() {
    quizState.quizType = 'general';
    
    // Reset chat history to just the system message
    chatHistory = [
        {
            "role": "system",
            "content": "You are Flicky, a friendly and totally cool entertainment-focused AI assistant. Your primary goal is to help users find movies and TV shows that are, like, totally awesome. Keep responses smooth, conversational, and sound cool and use slang. You can discuss entertainment topics in depth, but you're also happy to chat about other subjects when the user wants to. When responding, feel free to use the following emojis: 😎, 🍿, 🎬, 🎥, and 👍 to add some flair and keep your responses fresh, fun, and movie-tastic!"
        }
    ];
    
    clearMessagesExceptFirst();
    
    setTimeout(() => {
        addBotMessage("Hi there! I'm **Flicky**, your entertainment companion. Feel free to chat with me about movies, TV shows, or anything else you'd like to discuss.");
        
        if (document.getElementById('movie-search-results')) {
            document.getElementById('movie-search-results').style.display = 'none';
        }
    }, 500);
}
      
function startPreferencesQuiz() {
    quizState.quizType = 'preferences';
    quizState.currentStep = 0;
    
    clearMessagesExceptFirst();
    
    setTimeout(() => {
        const contentType = quizState.contentType === 'movie' ? 'movie' : 'TV show';
        
        const firstQuestion = quizFlow[0].question.replace('content', contentType);
        addBotMessage(firstQuestion, quizFlow[0].options);
    }, 500);
    
    if (document.getElementById('movie-search-results')) {
        document.getElementById('movie-search-results').style.display = 'none';
    }
}

function startSimilarMoviesQuiz() {
    quizState.quizType = 'similar';
    
    clearMessagesExceptFirst();
    
    setTimeout(() => {
        const contentType = quizState.contentType === 'movie' ? 'movie' : 'TV show';
        addBotMessage(`Great! Tell me a ${contentType} you like, and I'll suggest similar ones.`);
        
        let searchResults = document.getElementById('movie-search-results');
        if (!searchResults) {
            searchResults = document.createElement('div');
            searchResults.id = 'movie-search-results';
            document.getElementById('user-input-container').appendChild(searchResults);
        } else {
            searchResults.style.display = 'none';
            searchResults.innerHTML = '';
        }
        
        userInput.addEventListener('input', debounce(handleMovieSearch, 500));
    }, 500);
}

function startSummaryMode() {
    quizState.quizType = 'summary';
    
    clearMessagesExceptFirst();
    
    setTimeout(() => {
        const contentType = quizState.contentType === 'movie' ? 'movie' : 'TV show';
        addBotMessage(`Tell me which ${contentType} you'd like a summary for.`);
        
        let searchResults = document.getElementById('movie-search-results');
        if (!searchResults) {
            searchResults = document.createElement('div');
            searchResults.id = 'movie-search-results';
            document.getElementById('user-input-container').appendChild(searchResults);
        } else {
            searchResults.style.display = 'none';
            searchResults.innerHTML = '';
        }
        
        userInput.addEventListener('input', debounce(handleMovieSearch, 500));
    }, 500);
}

function clearMessagesExceptFirst() {
    while (chatMessages.children.length > 1) {
        chatMessages.removeChild(chatMessages.lastChild);
    }
}

async function handleMovieSearch() {
    const searchText = userInput.value.trim();
    const searchResults = document.getElementById('movie-search-results');
    
    if (searchText.length < 2) {
        searchResults.style.display = 'none';
        searchResults.innerHTML = '';
        return;
    }
    
    try {
        const searchType = quizState.contentType === 'movie' ? 'movie' : 'tv';
        const response = await fetch(
            `${BASE_URL}/search/${searchType}?api_key=${API_KEY}&query=${encodeURIComponent(searchText)}&page=1`
        );
        
        const data = await response.json();
        
        searchResults.innerHTML = '';
        
        if (data.results && data.results.length > 0) {
            const topResults = data.results.slice(0, 5);
            
            topResults.forEach(item => {
                const resultItem = document.createElement('div');
                resultItem.className = 'movie-search-item';
                
                const poster = document.createElement('img');
                poster.src = item.poster_path 
                    ? `${IMAGE_BASE_URL}${item.poster_path}`
                    : 'https://via.placeholder.com/40x60?text=No+Image';
                poster.alt = item.title || item.name;
                
                const info = document.createElement('div');
                info.className = 'movie-info';
                
                const title = document.createElement('div');
                title.className = 'movie-title';
                title.textContent = item.title || item.name;
                
                const year = document.createElement('div');
                year.className = 'movie-year';
                
                if (quizState.contentType === 'movie') {
                    year.textContent = item.release_date 
                        ? `Released: ${item.release_date.split('-')[0]}`
                        : 'Release date unknown';
                } else {
                    year.textContent = item.first_air_date 
                        ? `First aired: ${item.first_air_date.split('-')[0]}`
                        : 'Air date unknown';
                }
                
                info.appendChild(title);
                info.appendChild(year);
                
                resultItem.appendChild(poster);
                resultItem.appendChild(info);
                
                resultItem.addEventListener('click', () => {
                    selectMovie(item);
                });
                
                searchResults.appendChild(resultItem);
            });
            
            searchResults.style.display = 'block';
        } else {
            searchResults.style.display = 'none';
        }
    } catch (error) {
        console.error(`Error searching for ${quizState.contentType}:`, error);
    }
}

function selectMovie(item) {
    quizState.selectedMovie = item;
    userInput.value = item.title || item.name;
    document.getElementById('movie-search-results').style.display = 'none';
    
    addUserMessage(item.title || item.name);
    
    if (quizState.quizType === 'similar') {
        getSimilarMovies(item.id);
    } else if (quizState.quizType === 'summary') {
        getContentSummary(item);
    }
}

async function getSimilarMovies(itemId) {
    try {
        addBotMessage(`Looking for ${quizState.contentType}s similar to your selection...`);
        
        const contentType = quizState.contentType;
        const recommendationEndpoint = contentType === 'movie'
            ? `${BASE_URL}/movie/${itemId}/recommendations?api_key=${API_KEY}`
            : `${BASE_URL}/tv/${itemId}/recommendations?api_key=${API_KEY}`;
        
        const response = await fetch(recommendationEndpoint);
        const data = await response.json();
        
        if (data.results && data.results.length > 0) {
            displaySimilarMovies(data.results.slice(0, 5));
        } else {
            const similarEndpoint = contentType === 'movie'
                ? `${BASE_URL}/movie/${itemId}/similar?api_key=${API_KEY}`
                : `${BASE_URL}/tv/${itemId}/similar?api_key=${API_KEY}`;
            
            const similarResponse = await fetch(similarEndpoint);
            const similarData = await similarResponse.json();
            
            if (similarData.results && similarData.results.length > 0) {
                displaySimilarMovies(similarData.results.slice(0, 5));
            } else {
                addBotMessage(`I couldn't find any similar ${contentType}s. Would you like to try a different ${contentType}?`);
            }
        }
    } catch (error) {
        console.error(`Error fetching similar ${quizState.contentType}s:`, error);
        addBotMessage(`Sorry, there was an error finding similar ${quizState.contentType}s. Please try again later.`);
    }
}

async function getContentSummary(item) {
    try {
        addBotMessage(`Looking up the summary for "${item.title || item.name}"...`);
        
        const contentType = quizState.contentType;
        const endpoint = `${BASE_URL}/${contentType}/${item.id}?api_key=${API_KEY}`;
        
        const response = await fetch(endpoint);
        const data = await response.json();
        
        if (data && data.overview) {
            const initialSummary = `TMDB Description: ${data.overview}`;
            
            addBotMessage("Generating an AI-enhanced summary...");
            await generateAISummary(data, item.title || item.name);
        } else {
            addBotMessage(`Sorry, I couldn't find a detailed summary for "${item.title || item.name}".`);
        }
    } catch (error) {
        console.error(`Error fetching ${quizState.contentType} summary:`, error);
        addBotMessage(`Sorry, there was an error getting the summary. Please try again later.`);
    }
}

async function generateAISummary(contentData, title) {
    try {
        const description = contentData.overview;
        
        if (!description || description.trim() === '') {
            addBotMessage(`Sorry, there's no detailed description available for "${title}".`);
            return;
        }
        
        const prompt = `Give me a description on this ${quizState.contentType} "${title}" here's the ${quizState.contentType} description: "${description}"`;
        
        const response = await fetch('https://api.ai21.com/studio/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${AI21_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "model": "jamba-large-1.6",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }],                
                maxTokens: 2000,
                temperature: 0.7,
                topP: 1,
                stopSequences: []
            })
        });
        
        const data = await response.json();
        var run = true;
if (data && data.choices && data.choices[0] && data.choices[0].message.content) {
    displayAISummary(contentData, data.choices[0].message.content.trim(), title);
        } else {
            addBotMessage(`Here's the official description for "${title}": ${contentData.overview}`);
            addBotMessage("Would you like to get a summary for another title?", ["Yes, please", "No, thank you"]);
        }
    } catch (error) {
        console.error("Error generating AI summary:", error);
        
        addBotMessage(`Here's the official description for "${title}": ${contentData.overview}`);
        addBotMessage("Would you like to get a summary for another title?", ["Yes, please", "No, thank you"]);
    }
}

function displayAISummary(contentData, aiSummary, title) {
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message-container';
    
    const botMessage = document.createElement('div');
    botMessage.className = 'bot-message';
    
    const summaryContainer = document.createElement('div');
    summaryContainer.className = 'movie-recommendation';
    
    if (contentData.poster_path) {
        const poster = document.createElement('img');
        poster.src = `${IMAGE_BASE_URL}${contentData.poster_path}`;
        poster.alt = title;
        summaryContainer.appendChild(poster);
    }
    
    const titleElement = document.createElement('h4');
    titleElement.textContent = title;
    summaryContainer.appendChild(titleElement);
    
    const releaseInfo = document.createElement('p');
    if (quizState.contentType === 'movie') {
        releaseInfo.textContent = `Released: ${contentData.release_date ? contentData.release_date.split('-')[0] : 'Unknown'}`;
    } else {
        releaseInfo.textContent = `First aired: ${contentData.first_air_date ? contentData.first_air_date.split('-')[0] : 'Unknown'}`;
    }
    summaryContainer.appendChild(releaseInfo);
    
    const summaryHeading = document.createElement('p');
    summaryHeading.textContent = "AI-Enhanced Summary:";
    summaryHeading.style.fontWeight = "bold";
    summaryHeading.style.marginTop = "10px";
    summaryContainer.appendChild(summaryHeading);
    
    const summaryContent = document.createElement('div');
    if (typeof marked !== 'undefined') {
        summaryContent.innerHTML = marked.parse(aiSummary);
    } else {
        summaryContent.textContent = aiSummary;
    }
    summaryContainer.appendChild(summaryContent);
    
    messageContainer.appendChild(summaryContainer);
    chatMessages.appendChild(messageContainer);
    
    setTimeout(() => {
        addBotMessage("Would you like to get a summary for another title?", ["Yes, please", "No, thank you"]);
    }, 1000);
    
    scrollToBottom();
}
      
function displaySimilarMovies(items) {
    const contentType = quizState.contentType;
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message-container';
    
    const botMessage = document.createElement('div');
    botMessage.className = 'bot-message';
    botMessage.textContent = `Based on your selection, I recommend these similar ${contentType}s:`;
    messageContainer.appendChild(botMessage);
    
    const similarMoviesContainer = document.createElement('div');
    similarMoviesContainer.className = 'similar-movies-container';
    
    items.forEach(item => {
        const similarItem = document.createElement('div');
        similarItem.className = 'similar-movie';
        
        const poster = document.createElement('img');
        poster.src = item.poster_path 
            ? `${IMAGE_BASE_URL}${item.poster_path}`
            : 'https://via.placeholder.com/80x120?text=No+Image';
        poster.alt = item.title || item.name;
        similarItem.appendChild(poster);
        
        const itemInfo = document.createElement('div');
        itemInfo.className = 'similar-movie-info';
        
        const title = document.createElement('div');
        title.className = 'similar-movie-title';
        title.textContent = item.title || item.name;
        itemInfo.appendChild(title);
        
        const year = document.createElement('div');
        year.className = 'similar-movie-year';
        
        if (contentType === 'movie') {
            year.textContent = item.release_date 
                ? `Released: ${item.release_date.split('-')[0]}`
                : 'Release date unknown';
        } else {
            year.textContent = item.first_air_date 
                ? `First aired: ${item.first_air_date.split('-')[0]}`
                : 'Air date unknown';
        }
        
        itemInfo.appendChild(year);
        
        const overview = document.createElement('div');
        overview.className = 'similar-movie-overview';
        overview.textContent = item.overview.length > 100 
            ? item.overview.substring(0, 100) + '...' 
            : item.overview;
        itemInfo.appendChild(overview);
        
        similarItem.appendChild(itemInfo);
        similarMoviesContainer.appendChild(similarItem);
    });
    
    messageContainer.appendChild(similarMoviesContainer);
    chatMessages.appendChild(messageContainer);
    
    setTimeout(() => {
        addBotMessage(`Would you like to search for another ${contentType}?`, ["Yes, another search", "No, thank you"]);
    }, 1000);
    
    scrollToBottom();
}

function handleUserInput() {
    const text = userInput.value.trim();
    if (text !== '') {
        if (quizState.quizType === 'preferences' && quizState.currentStep < quizFlow.length) {
            addUserMessage(text);
            processUserInput(text);
            userInput.value = '';
        } else if (quizState.quizType === 'similar' && quizState.selectedMovie) {
            quizState.selectedMovie = null;
            userInput.value = '';
        } else if (quizState.quizType === 'general') {
            addUserMessage(text);
            userInput.value = '';
            handleGeneralConversation(text);
        } else {
            const searchResults = document.getElementById('movie-search-results');
            if (searchResults && searchResults.children.length > 0) {
                searchResults.children[0].click();
            } else {
                addUserMessage(text);
                userInput.value = '';
                addBotMessage("I couldn't find that movie. Please try another search.");
            }
        }
    }
}
async function handleGeneralConversation(text) {
    addBotMessage("Thinking...");
    
    // Add user message to chat history
    chatHistory.push({
        "role": "user",
        "content": text
    });
    
    try {
        const response = await fetch('https://api.ai21.com/studio/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${AI21_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "model": "jamba-large-1.6",
                "messages": chatHistory,
                maxTokens: 800,
                temperature: 0.7,
                topP: 1
            })
        });
        
        const data = await response.json();
        
        chatMessages.removeChild(chatMessages.lastChild);
        
        if (data && data.choices && data.choices[0] && data.choices[0].message.content) {
            const aiResponse = data.choices[0].message.content.trim();
            addBotMessage(aiResponse);
            
            // Add AI response to chat history
            chatHistory.push({
                "role": "assistant",
                "content": aiResponse
            });
            
            // Manage chat history length to prevent it from growing too large
            if (chatHistory.length > 20) {
                // Keep the system message and the 19 most recent messages
                chatHistory = [
                    chatHistory[0],
                    ...chatHistory.slice(chatHistory.length - 19)
                ];
            }
        } else {
            addBotMessage("I'm sorry, I'm having trouble understanding. Could you rephrase that or ask something else?");
        }
    } catch (error) {
        console.error("Error generating AI response:", error);
        
        chatMessages.removeChild(chatMessages.lastChild);
        
        addBotMessage("Sorry, I'm having trouble connecting to my brain right now. Please try again in a moment.");
    }
}
      
function processUserInput(text) {
    const currentQuestion = quizFlow[quizState.currentStep];
    
    quizState.userResponses[currentQuestion.responseKey] = text;
    
    quizState.currentStep++;
    
    if (quizState.currentStep < quizFlow.length) {
        setTimeout(() => {
            addBotMessage(quizFlow[quizState.currentStep].question, quizFlow[quizState.currentStep].options);
        }, 1000);
    } else {
        
        setTimeout(() => {
            addBotMessage("Thanks for your answers! Let me find the perfect content for you...");
            getMovieRecommendation();
        }, 1000);
    }
}

function addBotMessage(message, options = null) {
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message-container';
    
    const botMessage = document.createElement('div');
    botMessage.className = 'bot-message';
    
    // Use marked to parse markdown in the message
    if (typeof marked !== 'undefined') {
        botMessage.innerHTML = marked.parse(message);
    } else {
        // Fallback if marked is not loaded
        botMessage.textContent = message;
    }
    
    messageContainer.appendChild(botMessage);
    
    if (options) {
        const optionsContainer = document.createElement('div');
        optionsContainer.className = 'options-container';
        
        options.forEach(option => {
            const button = document.createElement('button');
            button.className = 'option-button';
            button.textContent = option;
            button.addEventListener('click', () => {
                userInput.value = option;
                handleUserInput();
            });
            optionsContainer.appendChild(button);
        });
        
        messageContainer.appendChild(optionsContainer);
    }
    
    chatMessages.appendChild(messageContainer);
    scrollToBottom();
}
      
function addUserMessage(message) {
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message-container';
    
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = message;
    messageContainer.appendChild(userMessage);
    
    chatMessages.appendChild(messageContainer);
    scrollToBottom();
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function getMovieRecommendation() {
    try {
        
        const genreMap = {
            'action': 28,
            'adventure': 12,
            'comedy': 35,
            'drama': 18,
            'horror': 27,
            'romance': 10749,
            'sci-fi': 878,
            'fantasy': 14
        };
        
        
        const tvGenreMap = {
            'action': 10759, 
            'adventure': 10759,
            'comedy': 35,
            'drama': 18,
            'horror': 9648, 
            'romance': 10749,
            'sci-fi': 10765,
            'fantasy': 10765
        };
        
        const userGenre = quizState.userResponses.genre.toLowerCase();
        const contentType = quizState.contentType;
        
        const genreId = contentType === 'movie' 
            ? genreMap[userGenre] || '' 
            : tvGenreMap[userGenre] || '';
        
        let yearParam = '';
        if (contentType === 'movie') {
            if (quizState.userResponses.era.toLowerCase().includes('modern')) {
                yearParam = '&primary_release_date.gte=2000-01-01';
            } else if (quizState.userResponses.era.toLowerCase().includes('classics')) {
                yearParam = '&primary_release_date.lte=1999-12-31';
            }
        } else {
            if (quizState.userResponses.era.toLowerCase().includes('modern')) {
                yearParam = '&first_air_date.gte=2000-01-01';
            } else if (quizState.userResponses.era.toLowerCase().includes('classics')) {
                yearParam = '&first_air_date.lte=1999-12-31';
            }
        }
        
        const endpointPath = contentType === 'movie' ? 'movie' : 'tv';
        const response = await fetch(
            `${BASE_URL}/discover/${endpointPath}?api_key=${API_KEY}&with_genres=${genreId}${yearParam}&sort_by=popularity.desc&page=1`
        );
        
        const data = await response.json();
        
        if (data.results && data.results.length > 0) {
            const randomIndex = Math.floor(Math.random() * Math.min(10, data.results.length));
            const item = data.results[randomIndex];
            
            const itemDetails = await fetch(
                `${BASE_URL}/${endpointPath}/${item.id}?api_key=${API_KEY}`
            );
            
            const itemData = await itemDetails.json();
            
            displayMovieRecommendation(itemData);
        } else {
            addBotMessage(`I couldn't find a ${contentType} matching your preferences. Please try again with different options.`);
        }
    } catch (error) {
        console.error(`Error fetching ${quizState.contentType} recommendation:`, error);
        addBotMessage(`Sorry, there was an error finding a ${quizState.contentType} recommendation. Please try again later.`);
    }
}

function displayMovieRecommendation(item) {
    const contentType = quizState.contentType;
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message-container';
    
    const botMessage = document.createElement('div');
    botMessage.className = 'bot-message';
    botMessage.textContent = `Based on your preferences, I recommend this ${contentType}:`;
    messageContainer.appendChild(botMessage);
    
    const recommendation = document.createElement('div');
    recommendation.className = 'movie-recommendation';
    
    if (item.poster_path) {
        const poster = document.createElement('img');
        poster.src = `${IMAGE_BASE_URL}${item.poster_path}`;
        poster.alt = item.title || item.name;
        recommendation.appendChild(poster);
    }
    
    const title = document.createElement('h4');
    title.textContent = item.title || item.name;
    recommendation.appendChild(title);
    
    const releaseInfo = document.createElement('p');
    if (contentType === 'movie') {
        releaseInfo.textContent = `Released: ${item.release_date ? item.release_date.split('-')[0] : 'Unknown'}`;
    } else {
        releaseInfo.textContent = `First aired: ${item.first_air_date ? item.first_air_date.split('-')[0] : 'Unknown'}`;
    }
    recommendation.appendChild(releaseInfo);
    
    const rating = document.createElement('p');
    rating.textContent = `Rating: ${item.vote_average}/10`;
    recommendation.appendChild(rating);
    
    if (item.overview) {
        const overview = document.createElement('p');
        overview.textContent = item.overview.length > 150 
            ? item.overview.substring(0, 150) + '...' 
            : item.overview;
        recommendation.appendChild(overview);
    }
    
    messageContainer.appendChild(recommendation);
    chatMessages.appendChild(messageContainer);
    
    setTimeout(() => {
        addBotMessage("Would you like another recommendation?", ["Yes, please!", "No, thank you"]);
    }, 1000);
    
    scrollToBottom();
}

document.addEventListener('click', function(e) {
    if (e.target && e.target.className === 'option-button') {
        if (e.target.textContent === "Yes, please!") {
            quizState.currentStep = 0;
            quizState.userResponses = {
                genre: '',
                mood: '',
                era: ''
            };
            
            setTimeout(() => {
                const contentType = quizState.contentType === 'movie' ? 'movie' : 'TV show';
                addBotMessage(`Great! Let's find another ${contentType} for you. What genre would you like this time?`, quizFlow[0].options);
            }, 500);
        } else if (e.target.textContent === "Yes, another search") {
            quizState.selectedMovie = null;
            
            setTimeout(() => {
                const contentType = quizState.contentType === 'movie' ? 'movie' : 'TV show';
                addBotMessage(`Great! Tell me another ${contentType} you like.`);
                const searchResults = document.getElementById('movie-search-results');
                if (searchResults) {
                    searchResults.style.display = 'none';
                    searchResults.innerHTML = '';
                }
                userInput.value = '';
            }, 500);
        } else if (e.target.textContent === "Yes, please") {
            quizState.selectedMovie = null;
            
            setTimeout(() => {
                const contentType = quizState.contentType === 'movie' ? 'movie' : 'TV show';
                addBotMessage(`Great! Tell me another ${contentType} you'd like a summary for.`);
                const searchResults = document.getElementById('movie-search-results');
                if (searchResults) {
                    searchResults.style.display = 'none';
                    searchResults.innerHTML = '';
                }
                userInput.value = '';
            }, 500);
        } else if (e.target.textContent === "No, thank you") {
            addUserMessage("No, thank you");
            setTimeout(() => {
                addBotMessage("You're welcome! Feel free to come back when you're looking for more entertainment recommendations. Enjoy!");
            }, 500);
        }
    }
});

if (typeof marked !== 'undefined') {
    marked.setOptions({
        sanitize: true,
        breaks: true,
        gfm: true
    });
}
      
initChatbot();
    </script>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
