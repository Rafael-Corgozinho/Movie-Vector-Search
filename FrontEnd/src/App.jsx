// App.jsx
import React, { useState } from 'react';
import { Search, Popcorn, Film, Star, X } from 'lucide-react';
import './App.css';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async (e) => {
    if (e) e.preventDefault();

    if (!searchTerm.trim()) {
      clearSearch();
      return;
    }

    setIsSearching(true);
    setHasSearched(true);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/search?query=${encodeURIComponent(
          searchTerm
        )}&limit=9`
      );

      const data = await response.json();
      setSearchResults(data.results || []);
    } catch (error) {
      console.error("Erro na requisição:", error);
      setSearchResults([]);
    } finally {
      setIsSearching(false);
    }
  };

  const clearSearch = () => {
    setSearchTerm('');
    setSearchResults([]);
    setIsSearching(false);
    setHasSearched(false);
  };

  const formatRating = (similarity) => {
    const score = ((similarity + 1) / 2) * 5;
    return Math.max(0, Math.min(5, score)).toFixed(1);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="logo-section" onClick={clearSearch} style={{cursor: 'pointer'}}>
          <div className="logo-icon"><Popcorn size={28} color="#e50914" /></div>
          <div>
            <h1 className="logo-text">Movie Searcher</h1>
            <span className="logo-subtitle">Semantic AI Movie Discovery</span>
          </div>
        </div>
        
        <div className="search-section">
          <form className="search-bar-modern" onSubmit={handleSearch}>
            <input
              type="text"
              className="search-input"
              placeholder="Ex: romance triste, viagem no tempo, sobrevivência..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              disabled={isSearching}
            />
            {searchTerm && (
              <button type="button" className="clear-button" onClick={clearSearch} disabled={isSearching}>
                <X size={18} />
              </button>
            )}
            <button type="submit" className="search-button-icon" disabled={isSearching || !searchTerm.trim()}>
              <Search size={20} />
            </button>
          </form>
        </div>
      </header>

      <main className="app-content">
        {!hasSearched && !isSearching && (
          <div className="discovery-mode">
            <div className="hero-icon">
              <Film size={48} />
            </div>
            <div className="intro-text">
              <h2>Descubra filmes usando busca semântica</h2>
              <p className="instruction-text-lg">
                Digite emoções, cenas, histórias ou conceitos. Nossa IA encontra os filmes mais relevantes para você com base no conteúdo, não apenas no título.
              </p>
            </div>
          </div>
        )}

        {isSearching && (
          <div className="loading-container">
            <div className="spinner"></div>
            <p>Analisando o banco vetorial...</p>
          </div>
        )}

        {hasSearched && !isSearching && (
          <div className="search-results-mode">
            <div className="results-header">
              <h3>Resultados para: <span className="searchTermDisplay">"{searchTerm}"</span></h3>
              <p className="ai-description-sm">
                {searchResults.length} filmes encontrados no banco vetorial.
              </p>
            </div>

            {searchResults.length > 0 ? (
              <div className="movie-grid">
                {searchResults.map((movie, index) => (
                  <div key={index} className="movie-card">
                    <div className="poster-placeholder">
                      <span className="poster-title">{movie.title}</span>
                    </div>
                    <div className="movie-info">
                      <div className="movie-header-info">
                        <h4 className="movie-title">{movie.title}</h4>
                        <div className="movie-rating-pill" title="Nível de similaridade">
                          <Star size={12} fill="currentColor" />
                          <span>{formatRating(movie.similarity)}</span>
                        </div>
                      </div>
                      <div className="movie-genre-container">
                        <span className="movie-genre-tag">{movie.genre}</span>
                      </div>
                      <p className="movie-description-sm">{movie.description}</p>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="no-results-view">
                <Film size={64} className="no-results-icon" />
                <h4 className="no-results-title">Nenhum filme encontrado</h4>
                <p>Tente descrever a cena, a emoção ou o conceito de uma forma diferente.</p>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;