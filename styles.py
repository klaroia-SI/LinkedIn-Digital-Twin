"""Styling constants for the digital twin Gradio app.

Targets the real Gradio 6.14.0 Chatbot DOM (verified against the installed
frontend build): .message-row > .bubble.(bot|user)-row > .flex-wrap >
.message > .bot/.user > .message-content, plus .bubble-wrap (scroll area),
.input-container (composer) and .submit-button.

Brand color is wired through Gradio theme variables (THEME) rather than
!important spam; CSS handles layout (full-window app + centered reading
column) and typography only.
"""

import gradio as gr

# ---------------------------------------------------------------------------
# Brand
# ---------------------------------------------------------------------------
BRAND = "#6C5CE7"
BRAND_HOVER = "#5B4BD6"
BRAND_SOFT = "#EDEBFB"          # subtle brand background (user bubble, light)
BRAND_SOFT_DARK = "#2C2752"     # subtle brand background (dark)

THEME = gr.themes.Base(
    font=[
        "system-ui", "-apple-system", "BlinkMacSystemFont",
        "Segoe UI", "Roboto", "Helvetica", "Arial", "sans-serif",
    ],
).set(
    # Accent / brand
    color_accent=BRAND,
    color_accent_soft=BRAND_SOFT,
    color_accent_soft_dark=BRAND_SOFT_DARK,
    border_color_accent=BRAND,
    border_color_accent_subdued="#D8D3F7",
    border_color_accent_subdued_dark="#3A3466",
    # Primary buttons (Send)
    button_primary_background_fill=BRAND,
    button_primary_background_fill_hover=BRAND_HOVER,
    button_primary_background_fill_dark=BRAND,
    button_primary_background_fill_hover_dark="#7A6BF0",
    button_primary_text_color="#ffffff",
    button_primary_text_color_dark="#ffffff",
    button_primary_border_color=BRAND,
    button_primary_border_color_dark=BRAND,
    # Readable text everywhere (Base defaults are too light)
    body_text_color="#1b1b22",
    body_text_color_dark="#eef0f4",
    body_text_color_subdued="#55555f",
    body_text_color_subdued_dark="#a6a6b2",
)

# ---------------------------------------------------------------------------
# Examples
# ---------------------------------------------------------------------------
EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

# ---------------------------------------------------------------------------
# CSS  (layout + typography; colors come from THEME)
# ---------------------------------------------------------------------------
CSS = """
:root, .gradio-container {
  --twin-brand: #6C5CE7;
  --twin-brand-hover: #5B4BD6;
  --twin-reading: 760px;   /* ~75 chars/line at 15px */
}

/* We manage our own light/dark theming — stop mobile browsers (Chrome/Android
   "force dark", iOS) from independently darkening backgrounds and breaking
   contrast. This makes the browser honour Gradio's theme instead. */
:root, html, body, gradio-app, .gradio-container { color-scheme: light dark; }

/* Hide framework chrome */
footer, .show-api, .api-docs, .built-with { display: none !important; }

/* ---------- Full-window app: remove the card cap (fixes the narrow ribbon) ---------- */
html, body, gradio-app { height: 100%; margin: 0; }
.gradio-container {
  max-width: 100% !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  min-height: 100vh !important;
  --chatbot-text-size: 15px;               /* Gradio's message font-size var */
}
/* Let the ChatInterface flex column own the height (fill_height=True) */
.gradio-container .main,
.gradio-container > .wrap,
.gradio-container .contain { min-width: 0 !important; }

/* ---------- Header: title + status dot, aligned to the reading column ---------- */
.gradio-container h1 {
  max-width: var(--twin-reading) !important;
  margin: 0 auto !important;
  padding: 20px 20px 14px !important;
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  font-size: 22px !important;
  font-weight: 700 !important;
  letter-spacing: -0.01em !important;
  border-bottom: 1px solid var(--border-color-primary) !important;
}
.gradio-container h1::before {           /* brand app icon (three dots) */
  content: "";
  flex: 0 0 auto;
  width: 38px; height: 38px;
  border-radius: 12px;
  background:
    radial-gradient(circle 2.4px at 12px 20px, #fff 99%, transparent 0),
    radial-gradient(circle 2.4px at 19px 20px, #fff 99%, transparent 0),
    radial-gradient(circle 2.4px at 26px 20px, #fff 99%, transparent 0),
    linear-gradient(135deg, #6C5CE7, #8A7BF0);
  box-shadow: 0 6px 16px rgba(108, 92, 231, 0.40);
}
.gradio-container h1::after {            /* "Ready" status */
  content: "● Ready";
  margin-left: auto;
  font-size: 12px !important;
  font-weight: 600 !important;
  color: #22b07d !important;
}

/* Description / any top-level markdown → same reading column */
.gradio-container .prose {
  max-width: var(--twin-reading) !important;
  margin-left: auto !important;
  margin-right: auto !important;
}

/* ---------- Chatbot panel: transparent, grows to fill, scrolls internally ---------- */
.chatbot, .chatbot.block, .panel-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}
.chatbot, .chatbot.block { flex: 1 1 auto !important; min-height: 0 !important; }
.bubble-wrap { overflow-y: auto !important; padding: 10px 12px 4px !important; }
.chatbot > .block-label, .chatbot > label { display: none !important; }
.placeholder-content, .placeholder { color: var(--body-text-color-subdued) !important; }

/* ---------- Reading column: constrain MESSAGES, not the app ---------- */
.message-row {
  max-width: var(--twin-reading) !important;
  width: 100% !important;
  margin-left: auto !important;
  margin-right: auto !important;
}
/* Assistant fills the column; user right-aligned at ~85% */
.bubble.bot-row { max-width: 100% !important; align-self: stretch !important; }
.bubble.user-row { max-width: 85% !important; }

/* Bubble shape (colors come from THEME: user=color_accent_soft, bot=bg secondary) */
.user { border-radius: 16px 16px 4px 16px !important; }
.bot  { border-radius: 4px 16px 16px 16px !important; }

/* ---------- Typography inside messages ---------- */
.bot, .user, .message-content, .flex-wrap { line-height: 1.6 !important; }
.message-content { font-size: 15px !important; }

/* High-contrast, UNIFORM text — fixes gray-on-gray and bold-vs-regular mismatch.
   Uses Gradio's own --body-text-color, which flips automatically for light/dark
   (we set both body_text_color and body_text_color_dark in THEME). This follows
   the active mode instead of relying on a .dark class that mobile may not set,
   so text can never end up dark-on-dark. Bold = weight only, same color. */
.message-content,
.message-content p,
.message-content li,
.message-content span,
.message-content strong,
.message-content b,
.message-content em,
.message-content :is(h1, h2, h3, h4, h5, h6),
.user, .bot, .flex-wrap {
  color: var(--body-text-color) !important;
}
/* Headings sized close to body so bold phrases don't shout */
.message-content :is(h1, h2, h3, h4, h5, h6) {
  font-size: 1.1em !important;
  line-height: 1.4 !important;
  font-weight: 700 !important;
  margin: 0.8em 0 0.35em !important;
}
.message-content p { margin: 0.5em 0 !important; }
.message-content p:first-child { margin-top: 0 !important; }
.message-content p:last-child { margin-bottom: 0 !important; }
/* Tighter list indentation; bullets shouldn't orphan a word */
.message-content ul, .message-content ol { padding-left: 1.35em !important; margin: 0.45em 0 !important; }
.message-content li { margin: 0.2em 0 !important; line-height: 1.6 !important; }
.message-content li > p { margin: 0 !important; }
.message-content a { color: var(--twin-brand) !important; text-decoration: underline; }
.message-content pre, .message-content code { font-size: 0.92em !important; }

/* ---------- Composer: reading-column width, rounded, brand focus ring ---------- */
.input-container {
  max-width: var(--twin-reading) !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 12px 12px 18px !important;
}
.twin-input textarea, .twin-input input[type="text"] {
  border-radius: 14px !important;
  font-size: 15px !important;
  line-height: 1.5 !important;
  padding: 12px 14px !important;
}
.twin-input textarea:focus, .twin-input input[type="text"]:focus {
  border-color: var(--twin-brand) !important;
  box-shadow: 0 0 0 3px rgba(108, 92, 231, 0.22) !important;
  outline: none !important;
}
.submit-button {
  border-radius: 14px !important;
  background: var(--twin-brand) !important;
  border-color: var(--twin-brand) !important;
}
.submit-button:hover { background: var(--twin-brand-hover) !important; border-color: var(--twin-brand-hover) !important; }
.submit-button svg { color: #fff !important; fill: currentColor !important; stroke: currentColor !important; }

/* ---------- Examples → reading column ---------- */
.gradio-container .examples, [data-testid="examples"] {
  max-width: var(--twin-reading) !important;
  margin: 6px auto 0 !important;
}
[data-testid="examples"] button, .examples button {
  border-radius: 999px !important;
  font-size: 13px !important;
}
[data-testid="examples"] button:hover, .examples button:hover {
  border-color: var(--twin-brand) !important;
  color: var(--twin-brand) !important;
}

/* ---------- Scrollbar + selection ---------- */
.bubble-wrap::-webkit-scrollbar { width: 10px; }
.bubble-wrap::-webkit-scrollbar-track { background: transparent; }
.bubble-wrap::-webkit-scrollbar-thumb { background: var(--border-color-primary); border-radius: 999px; }
.bubble-wrap::-webkit-scrollbar-thumb:hover { background: var(--twin-brand); }
::selection { background: rgba(108, 92, 231, 0.28); }

/* ---------- Responsive: edge-to-edge below 768px ---------- */
@media (max-width: 768px) {
  :root, .gradio-container { --twin-reading: 100%; }
  .gradio-container h1 { padding: 16px 16px 12px !important; font-size: 19px !important; }
  .input-container { padding-left: 16px !important; padding-right: 16px !important; }
  .bubble.user-row { max-width: 92% !important; }
}
"""

# ---------------------------------------------------------------------------
# JS  (unchanged behavior: title + keep the composer focused)
# ---------------------------------------------------------------------------
JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
