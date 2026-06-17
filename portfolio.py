import streamlit as st

st.set_page_config(
    page_title="Robert Ploski – Portfolio",
    page_icon="⚡",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0b0e11;
    color: #eaecef;
}

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

.hero {
    padding: 60px 0 40px 0;
    border-bottom: 1px solid #2b3139;
    margin-bottom: 48px;
}

.hero-name {
    font-size: 2.8rem;
    font-weight: 700;
    color: #eaecef;
    margin: 0;
    line-height: 1.1;
}

.hero-title {
    font-size: 1.1rem;
    color: #FCD535;
    font-weight: 600;
    margin: 8px 0 16px 0;
    letter-spacing: 0.03em;
}

.hero-bio {
    color: #707a8a;
    font-size: 0.95rem;
    max-width: 600px;
    line-height: 1.6;
}

.contact-row {
    display: flex;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
}

.contact-item {
    color: #929aa5;
    font-size: 0.85rem;
}

.contact-item a {
    color: #FCD535;
    text-decoration: none;
}

.contact-item a:hover {
    color: #f0b90b;
}

.section-header {
    font-size: 0.75rem;
    font-weight: 600;
    color: #707a8a;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 20px;
    padding-bottom: 8px;
    border-bottom: 1px solid #2b3139;
}

.project-card {
    background: #1e2329;
    border: 1px solid #2b3139;
    border-radius: 12px;
    padding: 28px;
    margin-bottom: 20px;
    transition: border-color 0.2s;
}

.project-card:hover {
    border-color: #FCD535;
}

.project-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #eaecef;
    margin: 0 0 4px 0;
}

.project-subtitle {
    font-size: 0.85rem;
    color: #FCD535;
    font-weight: 500;
    margin: 0 0 14px 0;
}

.project-desc {
    color: #929aa5;
    font-size: 0.9rem;
    line-height: 1.65;
    margin-bottom: 16px;
}

.tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 16px;
}

.tag {
    background: #2b3139;
    color: #eaecef;
    font-size: 0.75rem;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 9999px;
    border: 1px solid #3a3f48;
}

.tag-yellow {
    background: #3a3a1f;
    color: #FCD535;
    border-color: #FCD535;
}

.feature-list {
    list-style: none;
    padding: 0;
    margin: 0 0 8px 0;
}

.feature-list li {
    color: #929aa5;
    font-size: 0.88rem;
    padding: 4px 0;
    padding-left: 16px;
    position: relative;
    line-height: 1.5;
}

.feature-list li::before {
    content: "—";
    position: absolute;
    left: 0;
    color: #FCD535;
}

.skill-group {
    background: #1e2329;
    border: 1px solid #2b3139;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 12px;
}

.skill-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #707a8a;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
}

.divider {
    border: none;
    border-top: 1px solid #2b3139;
    margin: 40px 0;
}
</style>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <p class="hero-name">Robert Ploski</p>
    <p class="hero-title">Software Developer · AI Specialization</p>
    <p class="hero-bio">
        14 years of operational leadership at Malmö Airport, now building AI-driven software.
        Graduated June 2026. Background in structured problem-solving, team coordination and
        high-pressure decision-making — applied to backend systems, machine learning and full-stack development.
    </p>
    <div class="contact-row">
        <span class="contact-item">📧 <a href="mailto:robert.ploski90@gmail.com">robert.ploski90@gmail.com</a></span>
        <span class="contact-item">📞 +46 70 518 00 33</span>
        <span class="contact-item">🔗 <a href="https://linkedin.com" target="_blank">LinkedIn</a></span>
        <span class="contact-item">🐙 <a href="https://github.com/plosgit/VoxSR" target="_blank">GitHub – VoxSR</a></span>
    </div>
</div>
""", unsafe_allow_html=True)


# ── PROJECTS ──────────────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Projects</p>', unsafe_allow_html=True)

# VoxSR
st.markdown("""
<div class="project-card">
    <p class="project-title">VoxSR</p>
    <p class="project-subtitle">Text-to-Speech & Voice Cloning · Thesis Project · 2025–2026</p>
    <p class="project-desc">
        Full-stack web application for speech synthesis and voice cloning.
        Covers the entire pipeline from text input to finished audio, including preprocessing,
        custom model training and audio analysis. Built as a thesis project with the goal of
        owning every layer of the stack.
    </p>
    <ul class="feature-list">
        <li>17-language TTS and voice cloning via XTTS-v2</li>
        <li>Custom VITS model trained from scratch on VCTK corpus (109 speakers, 44k utterances)</li>
        <li>Audiobook generation — split, generate and merge long-form text</li>
        <li>Mel spectrogram visualization and quality metrics (MCD, voice similarity, pitch correlation)</li>
        <li>Azure Blob Storage for generated files, PostgreSQL for user data</li>
        <li>User auth via email and Google OAuth</li>
    </ul>
    <div class="tag-row">
        <span class="tag tag-yellow">React</span>
        <span class="tag tag-yellow">Python</span>
        <span class="tag tag-yellow">FastAPI</span>
        <span class="tag">Azure</span>
        <span class="tag">PostgreSQL</span>
        <span class="tag">XTTS-v2</span>
        <span class="tag">VITS</span>
        <span class="tag">PyTorch</span>
        <span class="tag">Vite</span>
        <span class="tag">Tailwind CSS</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Podmanager
st.markdown("""
<div class="project-card">
    <p class="project-title">Podmanager.ai</p>
    <p class="project-subtitle">Internship · Full Stack Developer · Remote · Sep 2025 – May 2026</p>
    <p class="project-desc">
        Worked as a full-stack developer in a production-ready team building an AI-powered platform.
        Primary focus on the RealVoice feature set — text-to-speech, transcription and translation
        integrated directly into the product UI.
    </p>
    <ul class="feature-list">
        <li>Backend development with Python and FastAPI — API design, implementation and integration</li>
        <li>Database work with MongoDB — data modelling and data cleaning</li>
        <li>Frontend development in Next.js with React and TypeScript</li>
        <li>Implemented and integrated AI features into the user interface</li>
        <li>Debugging, refactoring and performance improvements on existing codebase</li>
    </ul>
    <div class="tag-row">
        <span class="tag tag-yellow">Next.js</span>
        <span class="tag tag-yellow">React</span>
        <span class="tag tag-yellow">TypeScript</span>
        <span class="tag tag-yellow">FastAPI</span>
        <span class="tag">MongoDB</span>
        <span class="tag">Python</span>
        <span class="tag">AI Integration</span>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── SKILLS ────────────────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-group">
        <p class="skill-label">Languages</p>
        <div class="tag-row">
            <span class="tag">Python</span><span class="tag">JavaScript</span>
            <span class="tag">TypeScript</span><span class="tag">SQL</span>
            <span class="tag">C#</span><span class="tag">HTML</span><span class="tag">CSS</span>
        </div>
    </div>
    <div class="skill-group">
        <p class="skill-label">Frontend</p>
        <div class="tag-row">
            <span class="tag">React</span><span class="tag">Next.js</span>
            <span class="tag">Tailwind CSS</span><span class="tag">Vite</span>
        </div>
    </div>
    <div class="skill-group">
        <p class="skill-label">Backend & Databases</p>
        <div class="tag-row">
            <span class="tag">FastAPI</span><span class="tag">Node.js</span>
            <span class="tag">PostgreSQL</span><span class="tag">MongoDB</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-group">
        <p class="skill-label">AI & Data</p>
        <div class="tag-row">
            <span class="tag">PyTorch</span><span class="tag">Machine Learning</span>
            <span class="tag">AI API Integration</span><span class="tag">Speech Synthesis</span>
        </div>
    </div>
    <div class="skill-group">
        <p class="skill-label">Cloud & Tools</p>
        <div class="tag-row">
            <span class="tag">Azure</span><span class="tag">Git</span><span class="tag">Docker</span>
        </div>
    </div>
    <div class="skill-group">
        <p class="skill-label">Methodology</p>
        <div class="tag-row">
            <span class="tag">Agile</span><span class="tag">Scrum</span>
            <span class="tag">Testing & QA</span><span class="tag">REST APIs</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── BACKGROUND ────────────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Background</p>', unsafe_allow_html=True)

st.markdown("""
<div class="project-card">
    <p class="project-title">Load Supervisor</p>
    <p class="project-subtitle">Aviator Airport Services AB · Malmö Airport · 2012 – Present</p>
    <ul class="feature-list">
        <li>Responsible for aircraft loading and weight distribution — safety-critical decisions under time pressure</li>
        <li>Led and coordinated ground teams to meet tight turnaround deadlines</li>
        <li>Trained new staff in safety procedures and operational processes</li>
        <li>Certifications: Dangerous Goods IATA-DGR, De-/Anti-icing SAE AS6286, Loadmaster Narrow & Wide-body IATA-AHM</li>
    </ul>
</div>
""", unsafe_allow_html=True)
