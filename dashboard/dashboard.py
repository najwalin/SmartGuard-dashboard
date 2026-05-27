import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SmartGuard Analytics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --purple-900: #1a0533;
    --purple-800: #2d0a57;
    --purple-700: #3d1278;
    --purple-600: #5b21b6;
    --purple-500: #7c3aed;
    --purple-400: #a855f7;
    --purple-300: #c084fc;
    --purple-200: #e9d5ff;
    --purple-100: #f5f0ff;
    --accent:     #e879f9;
    --danger:     #f43f5e;
    --success:    #10b981;
    --warning:    #f59e0b;
    --text-primary:   #1a0533;
    --text-secondary: #6b21a8;
    --text-muted:     #9333ea;
    --bg-main:    #faf7ff;
    --bg-card:    #ffffff;
    --border:     #ede9fe;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: var(--bg-main) !important;
    color: var(--text-primary) !important;
}

.main .block-container {
    padding: 2rem 2.5rem 3rem !important;
    max-width: 1400px !important;
}

[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    transform: translateX(0) !important;
    background: linear-gradient(180deg, #1a0533 0%, #2d0a57 50%, #3d1278 100%) !important;
    border-right: 1px solid #5b21b6 !important;
    min-width: 260px !important;
    width: 260px !important;
}

[data-testid="stSidebar"][aria-expanded="false"] {
    margin-left: 0 !important;
    transform: translateX(0) !important;
}

[data-testid="stSidebar"] > div:first-child {
    width: 260px !important;
    min-width: 260px !important;
    background: transparent !important;
}

[data-testid="stSidebar"],
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div {
    color: #e9d5ff !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #e9d5ff !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 8px 12px !important;
    border-radius: 8px !important;
    transition: background 0.2s !important;
    display: block !important;
    cursor: pointer !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(124,58,237,0.25) !important;
}

[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    color: #7c3aed !important;
    background: rgba(124,58,237,0.1) !important;
    border-radius: 0 8px 8px 0 !important;
    z-index: 999 !important;
}

[data-testid="collapsedControl"] svg {
    fill: #7c3aed !important;
    color: #7c3aed !important;
}

.st-emotion-cache-1gwvy71,
.st-emotion-cache-6qob1r,
.st-emotion-cache-eczf2c,
.st-emotion-cache-1cypcdb {
    display: block !important;
    visibility: visible !important;
    background: linear-gradient(180deg, #1a0533 0%, #2d0a57 50%, #3d1278 100%) !important;
}
            
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div,
section[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(180deg, #3b0764 0%, #581c87 50%, #6d28d9 100%) !important;
    background-color: #3b0764 !important;
}

.page-header {
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border);
}
.page-header-eyebrow {
    font-size: 11px; font-weight: 600;
    letter-spacing: 1.5px; text-transform: uppercase;
    color: var(--purple-500); margin-bottom: 6px;
}
.page-header-title {
    font-size: 28px; font-weight: 800;
    color: var(--purple-900); letter-spacing: -0.8px;
    line-height: 1.2; margin-bottom: 6px;
}
.page-header-title span {
    background: linear-gradient(135deg, var(--purple-600), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.page-header-desc {
    font-size: 14px; color: #7c3aed;
    font-weight: 400; line-height: 1.6;
}

.metric-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px; margin-bottom: 2rem;
}
.metric-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px; padding: 20px 22px;
    position: relative; overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.metric-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, var(--purple-500), var(--accent));
}
.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(124,58,237,0.12);
}
.metric-card-icon {
    width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; margin-bottom: 14px;
}
.metric-card-icon.purple  { background: rgba(124,58,237,0.1); }
.metric-card-icon.danger  { background: rgba(244,63,94,0.1);  }
.metric-card-icon.success { background: rgba(16,185,129,0.1); }
.metric-card-icon.warning { background: rgba(245,158,11,0.1); }
.metric-card-label {
    font-size: 11px; font-weight: 600;
    letter-spacing: 0.8px; text-transform: uppercase;
    color: #9333ea; margin-bottom: 6px;
}
.metric-card-value {
    font-size: 26px; font-weight: 800;
    color: var(--purple-900); letter-spacing: -1px;
    line-height: 1; margin-bottom: 8px;
    font-family: 'JetBrains Mono', monospace;
}
.metric-card-delta {
    display: inline-flex; align-items: center; gap: 4px;
    font-size: 12px; font-weight: 600;
    padding: 3px 8px; border-radius: 20px;
}
.delta-up      { background: rgba(244,63,94,0.08);   color: var(--danger);   }
.delta-down    { background: rgba(16,185,129,0.08);  color: var(--success);  }
.delta-neutral { background: rgba(124,58,237,0.08);  color: var(--purple-500); }

/* Section card — header only styling (tanpa div wrapper) */
.section-card-header {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px 16px 0 0;
    padding: 20px 24px 14px 24px;
    display: flex; align-items: flex-start;
    justify-content: space-between;
    border-bottom: 1px solid var(--border);
    margin-bottom: 0;
}
.section-card-title {
    font-size: 15px; font-weight: 700;
    color: var(--purple-900); letter-spacing: -0.3px;
}
.section-card-sub {
    font-size: 12px; color: #9333ea;
    margin-top: 3px; font-weight: 400;
}
.section-badge {
    font-size: 11px; font-weight: 600;
    padding: 4px 10px; border-radius: 20px;
    background: rgba(124,58,237,0.08);
    color: var(--purple-600);
    border: 1px solid rgba(124,58,237,0.15);
    white-space: nowrap;
}

/* Section card full — untuk wrap konten + chart */
.section-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px; padding: 24px;
    margin-bottom: 20px;
}
.section-card .section-card-header {
    border-radius: 0; border: none;
    border-bottom: 1px solid var(--border);
    padding: 0 0 14px 0; margin-bottom: 20px;
    background: transparent;
}

.insight-box {
    background: linear-gradient(135deg, rgba(124,58,237,0.06), rgba(232,121,249,0.04));
    border: 1px solid rgba(124,58,237,0.15);
    border-left: 4px solid var(--purple-500);
    border-radius: 0 12px 12px 0;
    padding: 14px 18px; margin-top: 16px;
}
.insight-box-title {
    font-size: 12px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.8px;
    color: var(--purple-600); margin-bottom: 6px;
}
.insight-box-text {
    font-size: 13px; color: var(--text-primary); line-height: 1.7;
}

.sidebar-logo {
    display: flex; align-items: center; gap: 12px;
    padding: 1.5rem 1rem 2rem;
    border-bottom: 1px solid rgba(167,139,250,0.2);
    margin-bottom: 1.5rem;
}
.sidebar-logo-icon {
    width: 42px; height: 42px;
    background: linear-gradient(135deg, #7c3aed, #e879f9);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    box-shadow: 0 4px 15px rgba(124,58,237,0.4);
    flex-shrink: 0;
}
.sidebar-logo-title {
    font-size: 16px; font-weight: 700;
    color: #ffffff !important; letter-spacing: -0.3px; line-height: 1.2;
}
.sidebar-logo-sub {
    font-size: 11px; color: #c084fc !important;
    font-weight: 400; letter-spacing: 0.5px; text-transform: uppercase;
}
.sidebar-nav-label {
    font-size: 10px; font-weight: 600;
    letter-spacing: 1.2px; text-transform: uppercase;
    color: rgba(196,155,255,0.5) !important;
    padding: 0 0.5rem; margin-bottom: 0.5rem; display: block;
}
.sidebar-info {
    margin: 1.5rem 0.75rem 0;
    background: rgba(124,58,237,0.2);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 12px; padding: 14px;
}
.sidebar-info-title {
    font-size: 11px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.8px;
    color: #c084fc !important; margin-bottom: 8px;
}
.sidebar-info-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 4px 0; border-bottom: 1px solid rgba(167,139,250,0.1);
}
.sidebar-info-row:last-child { border-bottom: none; }
.sidebar-info-key { font-size: 12px; color: rgba(196,155,255,0.7) !important; }
.sidebar-info-val {
    font-size: 12px; font-weight: 600;
    color: #e9d5ff !important;
    font-family: 'JetBrains Mono', monospace !important;
}

[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid var(--border) !important;
}
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stPlotlyChart"] { border-radius: 12px; overflow: hidden; }
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--purple-100); }
::-webkit-scrollbar-thumb { background: var(--purple-300); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--purple-400); }
hr { border-color: var(--border) !important; margin: 1.5rem 0 !important; }

.qbadge {
    display: inline-block;
    background: linear-gradient(135deg, #7c3aed, #e879f9);
    color: white !important; font-size: 11px; font-weight: 700;
    padding: 3px 10px; border-radius: 20px;
    letter-spacing: 0.5px; margin-right: 8px;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PLOTLY THEME
# ─────────────────────────────────────────────
PURPLE_PALETTE = [
    "#7c3aed", "#a855f7", "#c084fc", "#e879f9",
    "#5b21b6", "#9333ea", "#d946ef", "#ec4899"
]

CHART_LAYOUT = dict(
    font_family="Plus Jakarta Sans",
    font_color="#1a0533",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=40, b=10),
    title_font_size=14,
    title_font_color="#1a0533",
)

AXIS_STYLE  = dict(gridcolor="#f5f0ff", linecolor="#ede9fe", tickfont_size=11, tickfont_color="#9333ea")
AXIS_STYLE2 = dict(gridcolor="rgba(0,0,0,0)", tickfont_color="#f43f5e")


# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('data/main_data.csv.gz', sep=';')
    df['Balance_After_Transaction'] = (
        df['Balance_After_Transaction'].astype(str)
        .str.replace('.', '', regex=False).astype(float) / 1e12
    )
    df['Amount_to_Age_Ratio'] = (
        df['Amount_to_Age_Ratio'].astype(str)
        .str.replace('.', '', regex=False).astype(float) / 1e15
    )
    df['Transaction_Amount_zscore'] = pd.to_numeric(df['Transaction_Amount_zscore'], errors='coerce')
    # Buat Time_Category (sudah di-drop saat FE, dibuat ulang dari Transaction_Hour)
    def time_cat(h):
        if h < 6:   return 'Night'
        elif h < 12: return 'Morning'
        elif h < 18: return 'Afternoon'
        else:        return 'Evening'
    df['Time_Category'] = df['Transaction_Hour'].apply(time_cat)
    return df

df = load_data()


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">🛡️</div>
        <div>
            <div class="sidebar-logo-title">SmartGuard</div>
            <div class="sidebar-logo-sub">Analytics Dashboard</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        label="Navigasi",
        options=[
            "Overview Dataset",
            "Analisis Temporal",
            "Analisis Nominal",
            "Analisis Geografis",
            "Merchant & Device",
            "Analisis Finansial",
            "Evaluasi Fitur"
        ],
        label_visibility="collapsed"
    )

    total_data   = len(df)
    fraud_count  = int(df['Is_Fraud'].sum())
    normal_count = total_data - fraud_count
    fraud_pct    = fraud_count / total_data * 100
    ratio        = int(normal_count / fraud_count) if fraud_count > 0 else 0

    st.markdown(f"""
    <div class="sidebar-info">
        <div class="sidebar-info-title">Info Dataset</div>
        <div class="sidebar-info-row">
            <span class="sidebar-info-key">Total Data</span>
            <span class="sidebar-info-val">{total_data:,}</span>
        </div>
        <div class="sidebar-info-row">
            <span class="sidebar-info-key">Fraud</span>
            <span class="sidebar-info-val">{fraud_count:,} ({fraud_pct:.2f}%)</span>
        </div>
        <div class="sidebar-info-row">
            <span class="sidebar-info-key">Normal</span>
            <span class="sidebar-info-val">{normal_count:,}</span>
        </div>
        <div class="sidebar-info-row">
            <span class="sidebar-info-key">Rasio</span>
            <span class="sidebar-info-val">1 : {ratio}</span>
        </div>
        <div class="sidebar-info-row">
            <span class="sidebar-info-key">Fitur</span>
            <span class="sidebar-info-val">{len(df.columns)}</span>
        </div>
        <div class="sidebar-info-row">
            <span class="sidebar-info-key">Tim</span>
            <span class="sidebar-info-val">CC26-PSU072</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────
def metric_card(icon, icon_class, label, value, delta_text, delta_class):
    return f"""
    <div class="metric-card">
        <div class="metric-card-icon {icon_class}">{icon}</div>
        <div class="metric-card-label">{label}</div>
        <div class="metric-card-value">{value}</div>
        <span class="metric-card-delta {delta_class}">{delta_text}</span>
    </div>
    """

def section_card_header(title, subtitle, badge=None):
    badge_html = f'<span class="section-badge">{badge}</span>' if badge else ""
    return f"""
    <div class="section-card-header">
        <div>
            <div class="section-card-title">{title}</div>
            <div class="section-card-sub">{subtitle}</div>
        </div>
        {badge_html}
    </div>
    """

def insight_box(text):
    return f"""
    <div class="insight-box">
        <div class="insight-box-title">💡 Insight</div>
        <div class="insight-box-text">{text}</div>
    </div>
    """

def q_header(q_num, title, subtitle):
    return f"""
    <div class="page-header">
        <div class="page-header-eyebrow">SmartGuard · CC26-PSU072</div>
        <div class="page-header-title"><span class="qbadge">Q{q_num}</span> <span>{title}</span></div>
        <div class="page-header-desc">{subtitle}</div>
    </div>
    """

def sc_header(title, subtitle, badge=None):
    """Render section card header standalone tanpa div wrapper — aman untuk Streamlit."""
    st.markdown(section_card_header(title, subtitle, badge), unsafe_allow_html=True)

def sc_end():
    """Tidak perlu close div — header sudah berdiri sendiri via CSS."""
    pass


# ═══════════════════════════════════════════════════════════════
# PAGE: OVERVIEW DATASET
# ═══════════════════════════════════════════════════════════════
if "Overview" in page:

    st.markdown("""
    <div class="page-header">
        <div class="page-header-eyebrow">SmartGuard · CC26-PSU072</div>
        <div class="page-header-title">Dataset <span>Overview</span></div>
        <div class="page-header-desc">
            Gambaran umum dataset Bank Transaction Fraud Detection — distribusi kelas,
            statistik dasar, dan ringkasan fitur.
        </div>
    </div>
    """, unsafe_allow_html=True)

    total        = len(df)
    fraud_count  = int(df['Is_Fraud'].sum())
    normal_count = total - fraud_count
    fraud_rate   = fraud_count / total * 100

    st.markdown(f"""
    <div class="metric-grid">
        {metric_card("📊", "purple",  "Total Transaksi",  f"{total:,}",         "Dataset lengkap",                "delta-neutral")}
        {metric_card("✅", "success", "Transaksi Normal", f"{normal_count:,}",   f"{100-fraud_rate:.2f}% dari total", "delta-down")}
        {metric_card("🚨", "danger",  "Transaksi Fraud",  f"{fraud_count:,}",    f"{fraud_rate:.2f}% dari total",     "delta-up")}
        {metric_card("⚖️", "warning", "Rasio Imbalance",  f"1 : {int(normal_count/fraud_count)}", "Fraud vs Normal", "delta-neutral")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.6])

    with col1:
        sc_header("Distribusi Kelas", "Fraud vs Non-Fraud", "Is_Fraud")
        fig_pie = go.Figure(go.Pie(
            labels=["Normal", "Fraud"], values=[normal_count, fraud_count],
            hole=0.65, marker_colors=["#7c3aed", "#f43f5e"],
            textinfo="percent", textfont_size=13,
            hovertemplate="<b>%{label}</b><br>%{value:,} transaksi<br>%{percent}<extra></extra>",
        ))
        fig_pie.add_annotation(
            text=f"<b>{fraud_rate:.1f}%</b><br><span style='font-size:11px'>Fraud Rate</span>",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#1a0533", family="Plus Jakarta Sans"), align="center"
        )
        fig_pie.update_layout(**CHART_LAYOUT, height=280, showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5))
        st.plotly_chart(fig_pie, width='stretch')

    with col2:
        sc_header("Distribusi Nominal Transaksi", "Transaction Amount — Normal vs Fraud")
        fig_hist = go.Figure()
        fig_hist.add_trace(go.Histogram(x=df[df['Is_Fraud']==0]['Transaction_Amount'],
            name="Normal", nbinsx=50, marker_color="#7c3aed", opacity=0.6))
        fig_hist.add_trace(go.Histogram(x=df[df['Is_Fraud']==1]['Transaction_Amount'],
            name="Fraud", nbinsx=50, marker_color="#f43f5e", opacity=0.7))
        fig_hist.update_layout(**CHART_LAYOUT, height=280, barmode="overlay",
            xaxis_title="Nominal Transaksi", yaxis_title="Frekuensi",
            xaxis=AXIS_STYLE, yaxis=AXIS_STYLE)
        st.plotly_chart(fig_hist, width='stretch')

    # Distribusi 3 fitur numerik utama
    sc_header("Distribusi Fitur Numerik Utama", "Transaction Amount, Account Balance, dan Age")
    col_n1, col_n2, col_n3 = st.columns(3)
    for col_obj, col_name, label in [
        (col_n1, 'Transaction_Amount', 'Nominal Transaksi (INR)'),
        (col_n2, 'Account_Balance',    'Saldo Akun (INR)'),
        (col_n3, 'Age',                'Usia Nasabah (Tahun)'),
    ]:
        with col_obj:
            fig_n = go.Figure()
            fig_n.add_trace(go.Histogram(
                x=df[col_name], nbinsx=40,
                marker_color='#7c3aed', opacity=0.75,
                name=label))
            skew_val = float(df[col_name].skew())
            fig_n.update_layout(**CHART_LAYOUT, height=260,
                title=f"{label}<br><sup>Skewness: {skew_val:.3f} (≈0 → Uniform/Sintetis)</sup>",
                xaxis=AXIS_STYLE, yaxis=dict(**AXIS_STYLE, title="Frekuensi"),
                showlegend=False)
            st.plotly_chart(fig_n, width='stretch')

    with st.expander("🔍 Preview Data (main_data)"):
        st.dataframe(df.head(100), width='stretch')
        st.caption(f"Total {len(df):,} baris × {len(df.columns)} kolom")

    st.markdown(insight_box(
        f"Dataset terdiri dari <b>{total:,} transaksi</b> dengan fraud rate <b>{fraud_rate:.2f}%</b> "
        f"({fraud_count:,} fraud dari {total:,} total). Rasio imbalance 1:{int(normal_count/fraud_count)} "
        f"menunjukkan perlunya teknik resampling (SMOTE)."
        f"<br><br>⚠️ <b>Indikasi Data Sintetis:</b> Distribusi <b>Uniform (skewness ≈ 0)</b> pada seluruh "
        f"fitur numerik (Transaction_Amount, Account_Balance, Age) mengonfirmasi dataset ini bersifat sintetis. "
        f"Hal ini menyebabkan fraud rate yang homogen (~5%) di semua kategori, sehingga korelasi linear "
        f"fitur tunggal sangat lemah dan model perlu menangkap <b>kombinasi fitur non-linear</b>."
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: ANALISIS TEMPORAL  (Menjawab pertanyaan 1 dan 3)
# ═══════════════════════════════════════════════════════════════
elif "Temporal" in page:

    st.markdown(q_header(1, "Analisis Temporal",
        "Faktor waktu dan perangkat yang paling dominan memicu fraud — jam, hari, malam, akhir pekan."),
        unsafe_allow_html=True)

    night_fraud_rate = df[df['Is_Night_Transaction']==1]['Is_Fraud'].mean()*100
    day_fraud_rate   = df[df['Is_Night_Transaction']==0]['Is_Fraud'].mean()*100
    weekend_fr       = df[df['Transaction_Weekend']==1]['Is_Fraud'].mean()*100
    combo_fr         = df[df['Is_High_Risk_Combination']==1]['Is_Fraud'].mean()*100

    st.markdown(f"""
    <div class="metric-grid">
        {metric_card("🌙", "danger",  "Fraud Rate Malam",   f"{night_fraud_rate:.2f}%", "Jam 00:00–05:59", "delta-up")}
        {metric_card("☀️", "success", "Fraud Rate Siang",   f"{day_fraud_rate:.2f}%",   "Jam 06:00–23:59", "delta-down")}
        {metric_card("📅", "warning", "Fraud Rate Weekend", f"{weekend_fr:.2f}%",       "Sabtu & Minggu",  "delta-up")}
        {metric_card("⚡", "danger",  "Fraud Rate Kombo",   f"{combo_fr:.2f}%",         "Malam + Mobile",  "delta-up")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        hour_stats = df.groupby('Transaction_Hour').agg(
            Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
        ).reset_index()
        hour_stats['Fraud_Rate'] = hour_stats['Fraud'] / hour_stats['Total'] * 100

        fig_hour = go.Figure()
        fig_hour.add_trace(go.Bar(x=hour_stats['Transaction_Hour'], y=hour_stats['Total'],
            name='Total', marker_color='#c084fc', opacity=0.5))
        fig_hour.add_trace(go.Scatter(x=hour_stats['Transaction_Hour'], y=hour_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#f43f5e', width=2.5), marker=dict(size=6), yaxis='y2'))
        fig_hour.update_layout(**CHART_LAYOUT, height=320,
            title="Fraud Rate per Jam Transaksi", xaxis_title="Jam",
            xaxis=AXIS_STYLE, yaxis=dict(**AXIS_STYLE, title="Volume"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'))
        st.plotly_chart(fig_hour, width='stretch')

    with col2:
        day_stats = df.groupby('Transaction_DayOfWeek').agg(
            Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
        ).reset_index()
        day_stats['Fraud_Rate'] = day_stats['Fraud'] / day_stats['Total'] * 100
        day_labels = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
        day_stats['Hari'] = day_stats['Transaction_DayOfWeek'].apply(
            lambda x: day_labels[x] if x < len(day_labels) else str(x))

        fig_day = go.Figure()
        fig_day.add_trace(go.Bar(x=day_stats['Hari'], y=day_stats['Total'],
            name='Total', marker_color='#a855f7', opacity=0.5))
        fig_day.add_trace(go.Scatter(x=day_stats['Hari'], y=day_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#f43f5e', width=2.5), marker=dict(size=7), yaxis='y2'))
        fig_day.update_layout(**CHART_LAYOUT, height=320,
            title="Fraud Rate per Hari Transaksi", xaxis_title="Hari",
            xaxis=AXIS_STYLE, yaxis=dict(**AXIS_STYLE, title="Volume"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'))
        st.plotly_chart(fig_day, width='stretch')

    # Heatmap
    sc_header("Heatmap Fraud — Jam vs Hari", "Intensitas fraud per kombinasi waktu")
    fraud_only    = df[df['Is_Fraud'] == 1]
    heatmap_data  = fraud_only.groupby(['Transaction_DayOfWeek', 'Transaction_Hour']).size().reset_index(name='count')
    heatmap_pivot = heatmap_data.pivot(index='Transaction_DayOfWeek', columns='Transaction_Hour', values='count').fillna(0)
    day_labels    = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
    fig_heat = px.imshow(heatmap_pivot,
        color_continuous_scale=['#f5f0ff','#7c3aed','#1a0533'],
        labels=dict(x="Jam", y="Hari", color="Jumlah Fraud"),
        y=[day_labels[i] for i in heatmap_pivot.index if i < len(day_labels)])
    fig_heat.update_layout(**CHART_LAYOUT, height=300)
    st.plotly_chart(fig_heat, width='stretch')

    # Time_Category + Skor Dominansi
    col_tc1, col_tc2 = st.columns(2)

    with col_tc1:
        time_order = ['Morning','Afternoon','Evening','Night']
        time_stats = df.groupby('Time_Category').agg(
            Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
        ).reset_index()
        time_stats['Fraud_Rate'] = time_stats['Fraud'] / time_stats['Total'] * 100
        time_stats['Time_Category'] = pd.Categorical(
            time_stats['Time_Category'], categories=time_order, ordered=True)
        time_stats = time_stats.sort_values('Time_Category')
        colors_tc = ['#a855f7' if cat != 'Night' else '#f43f5e' 
             for cat in time_stats['Time_Category'].astype(str)]

        fig_tc = go.Figure(go.Bar(
            x=time_stats['Time_Category'].astype(str),
            y=time_stats['Fraud_Rate'],
            marker_color=colors_tc,
            text=[f"{v:.2f}%" for v in time_stats['Fraud_Rate']],
            textposition='outside'))
        fig_tc.add_hline(y=df['Is_Fraud'].mean()*100, line_dash='dash',
            line_color='#e879f9', annotation_text=f"Rata-rata {df['Is_Fraud'].mean()*100:.2f}%")
        fig_tc.update_layout(**CHART_LAYOUT, height=320,
            title="Fraud Rate per Kategori Waktu",
            xaxis_title="Kategori Waktu", xaxis=AXIS_STYLE,
            yaxis=dict(**AXIS_STYLE, title="Fraud Rate (%)"))
        st.plotly_chart(fig_tc, width='stretch')

    with col_tc2:
        # Skor Dominansi
        total_n = len(df)
        dominansi_data = []
        factors_dom = {
            'Channel (Business)': (
                df[df['Account_Type']=='Business']['Is_Fraud'].mean()*100,
                (df['Account_Type']=='Business').mean()*100),
            'Waktu (Night)': (
                df[df['Time_Category']=='Night']['Is_Fraud'].mean()*100,
                (df['Time_Category']=='Night').mean()*100),
            'Device (Desktop)': (
                df[df['Device_Type']=='Desktop']['Is_Fraud'].mean()*100,
                (df['Device_Type']=='Desktop').mean()*100),
        }
        for label, (fr, prop) in factors_dom.items():
            dominansi_data.append({
                'Faktor': label,
                'Fraud Rate (%)': round(fr, 2),
                'Proporsi Data (%)': round(prop, 2),
                'Skor Dominansi': round(fr * prop, 2)
            })
        dom_df = pd.DataFrame(dominansi_data).sort_values('Skor Dominansi', ascending=True)
        max_skor = dom_df['Skor Dominansi'].max()
        colors_dom = ['#f43f5e' if v == max_skor else '#a855f7' for v in dom_df['Skor Dominansi']]

        fig_dom = go.Figure(go.Bar(
            x=dom_df['Skor Dominansi'], y=dom_df['Faktor'],
            orientation='h',
            marker_color=colors_dom,
            text=[f"{v:.2f}" for v in dom_df['Skor Dominansi']],
            textposition='outside'))
        fig_dom.update_layout(**CHART_LAYOUT, height=320,
            title="Skor Dominansi Faktor Pemicu Fraud<br><sup>Skor = Fraud Rate × Proporsi Data</sup>",
            xaxis=dict(**AXIS_STYLE, title="Skor Dominansi"),
            yaxis=AXIS_STYLE)
        st.plotly_chart(fig_dom, width='stretch')

    st.markdown("---")
    st.markdown(q_header(3, "Kombinasi Fitur Temporal + Device",
        "Kombinasi waktu, perangkat, dan lokasi yang paling sering muncul pada transaksi fraud."),
        unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        flags = {
            'Is_Night_Transaction'   : 'Transaksi Malam',
            'Is_High_Risk_Combination': 'Malam + Mobile',
            'Is_Weekend_Small_Amount' : 'Weekend + Nominal Kecil',
            'Transaction_Weekend'    : 'Akhir Pekan',
        }
        flag_data = []
        for col_name, label in flags.items():
            fr_yes = df[df[col_name]==1]['Is_Fraud'].mean()*100
            fr_no  = df[df[col_name]==0]['Is_Fraud'].mean()*100
            flag_data.append({'Kondisi': label, 'Terpenuhi': round(fr_yes,3), 'Tidak': round(fr_no,3)})
        flag_df = pd.DataFrame(flag_data)

        flag_df['Selisih'] = flag_df['Terpenuhi'] - flag_df['Tidak']

        fig_flags = go.Figure(go.Bar(
            x=flag_df['Selisih'],
            y=flag_df['Kondisi'],
            orientation='h',
            marker_color=['#f43f5e' if v > 0 else '#7c3aed' for v in flag_df['Selisih']],
            text=[f"+{v:.2f}%" if v > 0 else f"{v:.2f}%" for v in flag_df['Selisih']],
            textposition='outside'
        ))
        fig_flags.update_layout(**CHART_LAYOUT, height=340,
            title="Seberapa Besar Kondisi Ini Meningkatkan Fraud?<br><sup>🔴 Meningkatkan fraud | 🟣 Menurunkan fraud</sup>",
            xaxis=dict(**AXIS_STYLE, title="Selisih Fraud Rate (%)"),
            yaxis=AXIS_STYLE
        )
        st.plotly_chart(fig_flags, width='stretch')

    with col4:
        dev_stats = df.groupby('Device_Type').agg(
            Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
        ).reset_index()
        dev_stats['Fraud_Rate'] = dev_stats['Fraud'] / dev_stats['Total'] * 100
        dev_stats = dev_stats.sort_values('Fraud_Rate', ascending=False)

        max_dev = dev_stats['Fraud_Rate'].max()
        colors_dev = ['#f43f5e' if v == max_dev else '#a855f7' for v in dev_stats['Fraud_Rate']]

        fig_dev = go.Figure(go.Bar(
            x=dev_stats['Device_Type'],
            y=dev_stats['Fraud_Rate'],
            marker_color=colors_dev,
            text=[f"{v:.2f}%" for v in dev_stats['Fraud_Rate']],
            textposition='outside'
        ))
        fig_dev.update_layout(**CHART_LAYOUT, height=340,
            title="Fraud Rate per Tipe Device",
            xaxis=dict(**AXIS_STYLE, title="Device"),
            yaxis=dict(**AXIS_STYLE, title="Fraud Rate (%)"),
        )
        st.plotly_chart(fig_dev, width='stretch')

    st.markdown(insight_box(
        f"<b>Q1:</b> Berdasarkan kategori waktu, <b>Night (00:00–05:59)</b> memiliki fraud rate tertinggi "
        f"({night_fraud_rate:.2f}%), diikuti Morning, Evening, dan Afternoon. "
        f"<b>Skor Dominansi</b> (fraud_rate × proporsi data) menempatkan <b>Channel Business</b> "
        f"sebagai faktor paling dominan (171.80), karena meski fraud rate-nya tidak tertinggi, "
        f"proporsi datanya sangat besar (33.24%). Waktu Night (128.15) dan Device Desktop (127.20) "
        f"menyusul di posisi kedua dan ketiga."
        f"<br><br><b>Kesimpulan:</b> Tidak ada satu faktor tunggal yang dominan ekstrem — "
        f"fraud tersebar merata. Model AI perlu menangkap <b>kombinasi fitur</b>, bukan satu fitur saja."
        f"<br><br><b>Q3:</b> Device <b>{dev_stats.iloc[0]['Device_Type']}</b> fraud rate tertinggi "
        f"({dev_stats.iloc[0]['Fraud_Rate']:.2f}%). Kombinasi malam + mobile (Night + Mobile) "
        f"menjadi pola paling berisiko dengan fraud rate {combo_fr:.2f}%."
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: ANALISIS NOMINAL  (Menjawab pertanyaan 2)
# ═══════════════════════════════════════════════════════════════
elif "Nominal" in page:

    st.markdown(q_header(2, "Analisis Nominal Transaksi",
        "Interval nominal transaksi di mana fraud mulai melonjak dan skema verifikasi berjenjang yang tepat."),
        unsafe_allow_html=True)

    avg_fraud  = df[df['Is_Fraud']==1]['Transaction_Amount'].mean()
    avg_normal = df[df['Is_Fraud']==0]['Transaction_Amount'].mean()
    small_fr   = df[df['Is_Small_Amount_High_Risk']==1]['Is_Fraud'].mean()*100
    med_fraud  = df[df['Is_Fraud']==1]['Transaction_Amount'].median()

    st.markdown(f"""
    <div class="metric-grid">
        {metric_card("💵", "purple",  "Rata-rata Normal",     f"INR {avg_normal:,.0f}", "Per transaksi normal", "delta-neutral")}
        {metric_card("🔴", "danger",  "Rata-rata Fraud",      f"INR {avg_fraud:,.0f}",  "Per transaksi fraud",  "delta-up")}
        {metric_card("🎯", "warning", "Median Fraud",         f"INR {med_fraud:,.0f}",  "Nilai tengah fraud",   "delta-neutral")}
        {metric_card("⚠️", "danger",  "Fraud Rate Small Amt", f"{small_fr:.2f}%",      "Nominal < Rp 10.000",  "delta-up")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig_box = px.box(df, x='Is_Fraud', y='Transaction_Amount', color='Is_Fraud',
            color_discrete_map={0: "#7c3aed", 1: "#f43f5e"},
            labels={'Is_Fraud': 'Tipe (0=Normal, 1=Fraud)', 'Transaction_Amount': 'Nominal (Rp)'},
            title="Distribusi Nominal — Normal vs Fraud")
        fig_box.update_layout(**CHART_LAYOUT, height=350, xaxis=AXIS_STYLE, yaxis=AXIS_STYLE)
        st.plotly_chart(fig_box, width='stretch')

    with col2:
        sc_header("Statistik Deskriptif", "Transaction Amount per kelas")
        normal_stats = df[df['Is_Fraud']==0]['Transaction_Amount'].describe().round(2)
        fraud_stats  = df[df['Is_Fraud']==1]['Transaction_Amount'].describe().round(2)
        st.dataframe(pd.DataFrame({'Normal': normal_stats, 'Fraud': fraud_stats}), width='stretch')

    df_copy = df.copy()
    bins  = [0, 10_000, 25_000, 50_000, 75_000, 99_001]
    labs  = ['< 10K', '10K–25K', '25K–50K', '50K–75K', '> 75K']
    df_copy['Amount_Bin'] = pd.cut(df_copy['Transaction_Amount'], bins=bins, labels=labs)
    bin_stats = df_copy.groupby('Amount_Bin', observed=True).agg(
        Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
    ).reset_index()
    bin_stats['Fraud_Rate'] = (bin_stats['Fraud'] / bin_stats['Total'] * 100).round(3)
    bin_stats['Normal']     = bin_stats['Total'] - bin_stats['Fraud']
    bin_stats['Verifikasi'] = [
        '🔴 2FA Wajib (Card Testing)', '🟡 OTP + Notifikasi',
        '🟢 Notifikasi Standar', '🟡 OTP + Notifikasi', '🔴 2FA + Approval Manual'
    ]

    col3, col4 = st.columns([1.4, 1])

    with col3:
        max_fr = bin_stats['Fraud_Rate'].max()
        colors_fr = ['#f43f5e' if v == max_fr else '#a855f7' for v in bin_stats['Fraud_Rate']]

        fig_bin = go.Figure()
        fig_bin.add_trace(go.Bar(
            x=bin_stats['Amount_Bin'].astype(str), y=bin_stats['Normal'],
            name='Normal', marker_color='#7c3aed', opacity=0.7))
        fig_bin.add_trace(go.Bar(
            x=bin_stats['Amount_Bin'].astype(str), y=bin_stats['Fraud'],
            name='Fraud', marker_color='#f43f5e', opacity=0.9))
        fig_bin.add_trace(go.Scatter(
            x=bin_stats['Amount_Bin'].astype(str), y=bin_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#e879f9', width=2.5, dash='dot'),
            marker=dict(size=8, color='#e879f9'), yaxis='y2'))
        fig_bin.update_layout(**CHART_LAYOUT, height=360, barmode='group',
            title="Volume & Fraud Rate per Interval Nominal",
            xaxis_title="Interval Nominal (INR)", xaxis=AXIS_STYLE,
            yaxis=dict(**AXIS_STYLE, title="Jumlah Transaksi"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'))
        st.plotly_chart(fig_bin, width='stretch')

    with col4:
        sc_header("Skema Verifikasi Berjenjang", "Rekomendasi berdasarkan interval nominal")
        verif_df = bin_stats[['Amount_Bin','Fraud_Rate','Verifikasi']].rename(
            columns={'Amount_Bin':'Interval','Fraud_Rate':'Fraud Rate (%)','Verifikasi':'Rekomendasi'})
        st.dataframe(verif_df, width='stretch', hide_index=True)

    st.markdown(insight_box(
        f"<b>Q2:</b> Transaksi <b>nominal sangat kecil (<10.000)</b> memiliki fraud rate tertinggi "
        f"({small_fr:.2f}%) karena sering digunakan untuk <b>card testing</b>. "
        f"Rerata nominal fraud (INR {avg_fraud:,.0f}) hampir sama dengan normal (INR {avg_normal:,.0f})."
        f"<br><br><b>Skema Verifikasi:</b> &lt; 10K → 2FA wajib | 10K–75K → OTP | &gt; 75K → 2FA + approval manual."
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: ANALISIS GEOGRAFIS  (Menjawab pertanyaan 4)
# ═══════════════════════════════════════════════════════════════
elif "Geografis" in page:

    st.markdown(q_header(4, "Analisis Geografis & Segmentasi",
        "Distribusi fraud per channel transaksi, tipe akun, dan segmentasi nasabah."),
        unsafe_allow_html=True)

    type_stats = df.groupby('Transaction_Type').agg(
        Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
    ).reset_index()
    type_stats['Fraud_Rate'] = (type_stats['Fraud'] / type_stats['Total'] * 100).round(3)
    type_stats['Normal']     = type_stats['Total'] - type_stats['Fraud']
    type_stats = type_stats.sort_values('Fraud_Rate', ascending=False)

    acc_stats = df.groupby('Account_Type').agg(
        Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
    ).reset_index()
    acc_stats['Fraud_Rate'] = (acc_stats['Fraud'] / acc_stats['Total'] * 100).round(3)
    acc_stats = acc_stats.sort_values('Fraud_Rate', ascending=False)

    gender_stats = df.groupby('Gender').agg(
        Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
    ).reset_index()
    gender_stats['Fraud_Rate'] = (gender_stats['Fraud'] / gender_stats['Total'] * 100).round(3)

    top_type = type_stats.iloc[0]

    st.markdown(f"""
    <div class="metric-grid">
        {metric_card("🏆", "danger",  "Channel Fraud Tertinggi", top_type['Transaction_Type'], f"Fraud Rate {top_type['Fraud_Rate']:.2f}%", "delta-up")}
        {metric_card("💳", "warning", "Akun Business",  f"{acc_stats[acc_stats['Account_Type']=='Business']['Fraud_Rate'].values[0]:.2f}%", "Fraud rate tertinggi", "delta-up")}
        {metric_card("👤", "purple",  "Fraud Rate Male",   f"{gender_stats[gender_stats['Gender']=='Male']['Fraud_Rate'].values[0]:.2f}%",   "Laki-laki", "delta-neutral")}
        {metric_card("👤", "success", "Fraud Rate Female", f"{gender_stats[gender_stats['Gender']=='Female']['Fraud_Rate'].values[0]:.2f}%", "Perempuan", "delta-neutral")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.4, 1])

    with col1:
        fig_type = go.Figure()
        fig_type.add_trace(go.Bar(x=type_stats['Transaction_Type'], y=type_stats['Normal'],
            name='Normal', marker_color='#7c3aed', opacity=0.75))
        fig_type.add_trace(go.Bar(x=type_stats['Transaction_Type'], y=type_stats['Fraud'],
            name='Fraud', marker_color='#f43f5e', opacity=0.9))
        fig_type.add_trace(go.Scatter(x=type_stats['Transaction_Type'], y=type_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#e879f9', width=2.5), marker=dict(size=8), yaxis='y2'))
        fig_type.update_layout(**CHART_LAYOUT, height=360, barmode='group',
            title="Fraud per Tipe Transaksi (Channel)", xaxis_title="Tipe Transaksi",
            xaxis=AXIS_STYLE, yaxis=dict(**AXIS_STYLE, title="Jumlah Transaksi"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'))
        st.plotly_chart(fig_type, width='stretch')

    with col2:
        sc_header("Statistik per Channel", "Fraud Rate & Volume")
        disp = type_stats[['Transaction_Type','Total','Fraud','Fraud_Rate']].rename(
            columns={'Transaction_Type':'Channel','Fraud_Rate':'Rate (%)'})
        st.dataframe(disp, width='stretch', hide_index=True)

    col3, col4 = st.columns(2)

    with col3:
        max_acc = acc_stats['Fraud_Rate'].max()
        colors_acc = ['#f43f5e' if v == max_acc else '#a855f7' for v in acc_stats['Fraud_Rate']]

        fig_acc = go.Figure(go.Bar(
            x=acc_stats['Account_Type'],
            y=acc_stats['Fraud_Rate'],
            marker_color=colors_acc,
            text=[f"{v:.2f}%" for v in acc_stats['Fraud_Rate']],
            textposition='outside'
        ))
        fig_acc.update_layout(**CHART_LAYOUT, height=300,
            title="Fraud Rate per Tipe Akun",
            xaxis=dict(**AXIS_STYLE, title="Tipe Akun"),
            yaxis=dict(**AXIS_STYLE, title="Fraud Rate (%)"),
        )
        st.plotly_chart(fig_acc, width='stretch')

    with col4:
        fig_gender = go.Figure()
        fig_gender.add_trace(go.Bar(x=gender_stats['Gender'], y=gender_stats['Total'],
            name='Total', marker_color='#a855f7', opacity=0.6))
        fig_gender.add_trace(go.Bar(x=gender_stats['Gender'], y=gender_stats['Fraud'],
            name='Fraud', marker_color='#f43f5e', opacity=0.9))
        fig_gender.add_trace(go.Scatter(x=gender_stats['Gender'], y=gender_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#e879f9', width=2), marker=dict(size=10), yaxis='y2'))
        fig_gender.update_layout(**CHART_LAYOUT, height=300, barmode='group',
            title="Fraud per Gender", xaxis=AXIS_STYLE,
            yaxis=dict(**AXIS_STYLE, title="Jumlah"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.3, x=0.5, xanchor='center'))
        st.plotly_chart(fig_gender, width='stretch')

    sc_header("Heatmap Segmentasi", "Fraud Rate: Tipe Akun × Tipe Transaksi")
    cross = df.groupby(['Account_Type','Transaction_Type'])['Is_Fraud'].mean().reset_index()
    cross['Is_Fraud'] = (cross['Is_Fraud'] * 100).round(3)
    pivot_cross = cross.pivot(index='Account_Type', columns='Transaction_Type', values='Is_Fraud')
    fig_cross = px.imshow(pivot_cross, text_auto='.2f',
        color_continuous_scale=['#f5f0ff','#a855f7','#f43f5e'],
        title="Fraud Rate (%) — Tipe Akun vs Tipe Transaksi<br><sup>Rentang nilai sempit (4.7%–5.4%)",
        labels=dict(color="Fraud Rate (%)"))
    fig_cross.update_layout(**CHART_LAYOUT, height=300)
    st.plotly_chart(fig_cross, width='stretch')

    max_val = pivot_cross.max().max()
    max_col = pivot_cross.max().idxmax()
    max_row = pivot_cross[max_col].idxmax()
    st.info(f"💡 Kombinasi tertinggi: **{max_row} × {max_col}** dengan fraud rate **{max_val:.2f}%**")

    # Heatmap Account_Type × Time_Category (dari notebook Q4)
    sc_header("Heatmap Waktu × Tipe Akun", "Fraud Rate: Kategori Waktu × Tipe Akun — identifikasi celah berisiko")
    cross_time = df.groupby(['Account_Type','Time_Category'])['Is_Fraud'].mean().reset_index()
    cross_time['Is_Fraud'] = (cross_time['Is_Fraud'] * 100).round(3)
    time_order = ['Morning','Afternoon','Evening','Night']
    pivot_time = cross_time.pivot(index='Account_Type', columns='Time_Category', values='Is_Fraud')
    pivot_time = pivot_time[[c for c in time_order if c in pivot_time.columns]]
    fig_time_acc = px.imshow(pivot_time, text_auto='.2f',
        color_continuous_scale=['#f5f0ff','#a855f7','#f43f5e'],
        title="Fraud Rate (%) — Tipe Akun vs Kategori Waktu",
        labels=dict(color="Fraud Rate (%)"))
    fig_time_acc.update_layout(**CHART_LAYOUT, height=280)
    st.plotly_chart(fig_time_acc, width='stretch')

    max_val = pivot_time.max().max()
    max_col = pivot_time.max().idxmax()
    max_row = pivot_time[max_col].idxmax()
    st.info(f"💡 Kombinasi tertinggi: **{max_row} × {max_col}** dengan fraud rate **{max_val:.2f}%**")

    st.markdown(insight_box(
        f"<b>Q4:</b> Channel <b>{top_type['Transaction_Type']}</b> memiliki fraud rate tertinggi "
        f"({top_type['Fraud_Rate']:.2f}%). Akun <b>Business</b> memiliki fraud rate tertinggi "
        f"({acc_stats.iloc[0]['Fraud_Rate']:.2f}%) karena volume dan nominal transaksi lebih besar. "
        f"Gender hampir tidak berpengaruh (~5% untuk keduanya). "
        f"<br><br>Heatmap <b>Tipe Akun × Kategori Waktu</b> menunjukkan pengaruh waktu berbeda per segmen — "
        f"akun Business lebih rentan pada <b>malam hari (Night)</b>, sedangkan Savings relatif stabil. "
        f"Kombinasi segmen + waktu jauh lebih informatif dibanding masing-masing fitur secara terpisah. "
        f"Kolom State & City sudah di-drop saat feature engineering karena fraud rate antar wilayah "
        f"homogen (~5%), tidak cukup diskriminatif sebagai fitur model."
        f"<br><br><b>Rekomendasi:</b> Tingkatkan monitoring channel Transfer dan akun Business, "
        f"terutama pada malam hari."
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: MERCHANT & DEVICE  (Menjawab pertanyaan ke 5)
# ═══════════════════════════════════════════════════════════════
elif "Merchant" in page:

    st.markdown(q_header(5, "Merchant & Device",
        "Kategori merchant dengan fraud rate tertinggi dan kebijakan keamanan yang paling tepat."),
        unsafe_allow_html=True)

    merch_stats = df.groupby('Merchant_Category').agg(
        Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
    ).reset_index()
    merch_stats['Fraud_Rate'] = (merch_stats['Fraud'] / merch_stats['Total'] * 100).round(3)
    merch_stats['Normal']     = merch_stats['Total'] - merch_stats['Fraud']
    merch_stats = merch_stats.sort_values('Fraud_Rate', ascending=False)

    device_stats = df.groupby('Device_Type').agg(
        Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
    ).reset_index()
    device_stats['Fraud_Rate'] = (device_stats['Fraud'] / device_stats['Total'] * 100).round(3)
    device_stats['Normal']     = device_stats['Total'] - device_stats['Fraud']
    device_stats = device_stats.sort_values('Fraud_Rate', ascending=False)

    top_merch  = merch_stats.iloc[0]
    top_device = device_stats.iloc[0]

    st.markdown(f"""
    <div class="metric-grid">
        {metric_card("🏪", "danger",  "Merchant Fraud Tertinggi", top_merch['Merchant_Category'],  f"Rate {top_merch['Fraud_Rate']:.2f}%",  "delta-up")}
        {metric_card("📱", "warning", "Device Fraud Tertinggi",   top_device['Device_Type'],       f"Rate {top_device['Fraud_Rate']:.2f}%", "delta-up")}
        {metric_card("🎯", "danger",  "High Risk Merchant",       f"{df['Is_High_Risk_Merchant'].mean()*100:.1f}%", "Clothing + Groceries", "delta-neutral")}
        {metric_card("💻", "warning", "High Risk Device",         f"{df['Is_High_Risk_Device'].mean()*100:.1f}%",  "Desktop",              "delta-neutral")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig_merch = go.Figure()
        fig_merch.add_trace(go.Bar(x=merch_stats['Merchant_Category'], y=merch_stats['Normal'],
            name='Normal', marker_color='#7c3aed', opacity=0.7))
        fig_merch.add_trace(go.Bar(x=merch_stats['Merchant_Category'], y=merch_stats['Fraud'],
            name='Fraud', marker_color='#f43f5e', opacity=0.9))
        fig_merch.add_trace(go.Scatter(x=merch_stats['Merchant_Category'], y=merch_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#e879f9', width=2.5), marker=dict(size=8), yaxis='y2'))
        fig_merch.update_layout(**CHART_LAYOUT, height=360, barmode='group',
            title="Fraud per Kategori Merchant", xaxis_title="Merchant Category",
            xaxis=AXIS_STYLE, yaxis=dict(**AXIS_STYLE, title="Jumlah Transaksi"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'))
        st.plotly_chart(fig_merch, width='stretch')

    with col2:
        fig_dev2 = go.Figure()
        fig_dev2.add_trace(go.Bar(x=device_stats['Device_Type'], y=device_stats['Normal'],
            name='Normal', marker_color='#a855f7', opacity=0.7))
        fig_dev2.add_trace(go.Bar(x=device_stats['Device_Type'], y=device_stats['Fraud'],
            name='Fraud', marker_color='#f43f5e', opacity=0.9))
        fig_dev2.add_trace(go.Scatter(x=device_stats['Device_Type'], y=device_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#e879f9', width=2.5), marker=dict(size=8), yaxis='y2'))
        fig_dev2.update_layout(**CHART_LAYOUT, height=360, barmode='group',
            title="Fraud per Tipe Device", xaxis_title="Device Type",
            xaxis=AXIS_STYLE, yaxis=dict(**AXIS_STYLE, title="Jumlah Transaksi"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'))
        st.plotly_chart(fig_dev2, width='stretch')

    col3, col4 = st.columns(2)

    with col3:
        fig_tree = px.treemap(merch_stats, path=['Merchant_Category'], values='Total',
            color='Fraud_Rate', color_continuous_scale=['#e9d5ff','#7c3aed','#f43f5e'],
            title="Volume Transaksi per Merchant (warna = Fraud Rate)",
            custom_data=['Fraud_Rate'])
        fig_tree.update_traces(texttemplate='%{label}<br>%{customdata[0]:.2f}%')
        fig_tree.update_layout(**CHART_LAYOUT, height=320)
        st.plotly_chart(fig_tree, width='stretch')

    with col4:
        cross_md = df.groupby(['Merchant_Category','Device_Type'])['Is_Fraud'].mean().reset_index()
        cross_md['Is_Fraud'] = (cross_md['Is_Fraud']*100).round(3)
        pivot_md = cross_md.pivot(index='Merchant_Category', columns='Device_Type', values='Is_Fraud')
        fig_md = px.imshow(pivot_md, text_auto='.2f',
            color_continuous_scale=['#f5f0ff','#a855f7','#f43f5e'],
            title="Fraud Rate (%) — Merchant × Device",
            labels=dict(color="Fraud Rate (%)"))
        fig_md.update_layout(**CHART_LAYOUT, height=320)
        st.plotly_chart(fig_md, width='stretch')

    sc_header("Kebijakan Keamanan per Merchant", "Rekomendasi berdasarkan fraud rate & risiko kategori")
    kebijakan_map = {
        'Clothing'     : ('Tinggi', '2FA wajib + limit nominal harian'),
        'Groceries'    : ('Tinggi', '2FA wajib + alert transaksi berulang'),
        'Electronics'  : ('Sedang', 'OTP + limit transaksi > Rp 500K'),
        'Entertainment': ('Sedang', 'OTP + monitoring frekuensi'),
        'Restaurant'   : ('Rendah', 'Push notifikasi standar'),
        'Health'       : ('Rendah', 'Push notifikasi standar'),
    }
    kebijakan_data = []
    for _, row in merch_stats.iterrows():
        m = row['Merchant_Category']
        risk, policy = kebijakan_map.get(m, ('🟢 Rendah', 'Push notifikasi standar'))
        kebijakan_data.append({'Merchant': m, 'Fraud Rate (%)': row['Fraud_Rate'],
                                'Risiko': risk, 'Kebijakan': policy})
    st.dataframe(pd.DataFrame(kebijakan_data), width='stretch', hide_index=True)

    hr_merch_fr = df[df['Is_High_Risk_Merchant']==1]['Is_Fraud'].mean()*100
    hr_dev_fr   = df[df['Is_High_Risk_Device']==1]['Is_Fraud'].mean()*100

    st.markdown(insight_box(
        f"<b>Q5:</b> Merchant <b>{top_merch['Merchant_Category']}</b> memiliki fraud rate tertinggi "
        f"({top_merch['Fraud_Rate']:.2f}%), flag <code>Is_High_Risk_Merchant</code> fraud rate {hr_merch_fr:.2f}%. "
        f"Device <b>{top_device['Device_Type']}</b> fraud rate tertinggi ({top_device['Fraud_Rate']:.2f}%), "
        f"flag <code>Is_High_Risk_Device</code> ({hr_dev_fr:.2f}%)."
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: ANALISIS FINANSIAL  (Menjawab pertanyaan ke 6)
# ═══════════════════════════════════════════════════════════════
elif "Finansial" in page:

    st.markdown(q_header(6, "Analisis Finansial",
        "Hubungan saldo akun dan nilai transaksi terhadap fraud — rasio Amount/Balance sebagai aturan deteksi."),
        unsafe_allow_html=True)

    avg_normal       = df[df['Is_Fraud']==0]['Transaction_Amount'].mean()
    avg_fraud        = df[df['Is_Fraud']==1]['Transaction_Amount'].mean()
    total_loss       = df[df['Is_Fraud']==1]['Transaction_Amount'].sum()
    critical_fr      = df[df['Is_Balance_Critical']==1]['Is_Fraud'].mean()*100
    avg_ratio_fraud  = df[df['Is_Fraud']==1]['Amount_to_Balance_Ratio'].mean()
    avg_ratio_normal = df[df['Is_Fraud']==0]['Amount_to_Balance_Ratio'].mean()
    med_normal       = df[df['Is_Fraud']==0]['Transaction_Amount'].median()

    st.markdown(f"""
    <div class="metric-grid">
        {metric_card("💵", "purple",  "Rata-rata Normal",        f"INR {avg_normal:,.0f}",     "Per transaksi",           "delta-neutral")}
        {metric_card("🔴", "danger",  "Rata-rata Fraud",         f"INR {avg_fraud:,.0f}",      "Per transaksi fraud",      "delta-up")}
        {metric_card("📉", "warning", "Total Estimasi Kerugian", f"INR {total_loss/1e9:.1f}M", "Seluruh transaksi fraud",  "delta-up")}
        {metric_card("📊", "success", "Median Normal",           f"INR {med_normal:,.0f}",     "Nilai tengah",             "delta-down")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        sample = df.sample(min(3000, len(df)), random_state=42)
        fig_scatter = px.scatter(sample, x='Account_Balance', y='Transaction_Amount',
            color='Is_Fraud', color_discrete_map={0:'#7c3aed', 1:'#f43f5e'},
            opacity=0.4, title="Saldo Akun vs Nominal Transaksi",
            labels={'Account_Balance':'Saldo Akun (INR)', 'Transaction_Amount':'Nominal Transaksi (INR)', 'Is_Fraud':'Fraud'})
        fig_scatter.update_layout(**CHART_LAYOUT, height=360, xaxis=AXIS_STYLE, yaxis=AXIS_STYLE)
        st.plotly_chart(fig_scatter, width='stretch')

    with col2:
        bins_r = [0, 0.1, 0.25, 0.5, 0.75, 1.01]
        labs_r = ['0–10%', '10–25%', '25–50%', '50–75%', '75–100%']
        df_r   = df.copy()
        df_r['ratio_bin'] = pd.cut(df_r['Amount_to_Balance_Ratio'], bins=bins_r, labels=labs_r)
        ratio_stats = df_r.groupby('ratio_bin', observed=True).agg(
            Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
        ).reset_index()
        ratio_stats['Fraud_Rate'] = (ratio_stats['Fraud'] / ratio_stats['Total'] * 100).round(3)

        fig_ratio = go.Figure()
        fig_ratio.add_trace(go.Bar(x=ratio_stats['ratio_bin'].astype(str), y=ratio_stats['Total'],
            name='Total', marker_color='#a855f7', opacity=0.6))
        fig_ratio.add_trace(go.Scatter(x=ratio_stats['ratio_bin'].astype(str), y=ratio_stats['Fraud_Rate'],
            name='Fraud Rate (%)', mode='lines+markers',
            line=dict(color='#f43f5e', width=2.5), marker=dict(size=8), yaxis='y2'))
        fig_ratio.update_layout(**CHART_LAYOUT, height=360,
            title="Fraud Rate per Rasio Amount/Balance",
            xaxis_title="Rasio Transaksi terhadap Saldo (%)", xaxis=AXIS_STYLE,
            yaxis=dict(**AXIS_STYLE, title="Jumlah Transaksi"),
            yaxis2=dict(**AXIS_STYLE2, title="Fraud Rate (%)", overlaying='y', side='right'),
            legend=dict(orientation='h', y=-0.25, x=0.5, xanchor='center'))
        st.plotly_chart(fig_ratio, width='stretch')
    ins1, ins2 = st.columns(2)

    with ins1:
        st.markdown("""
        <div style="background:#f5f0ff; border-left:3px solid #a855f7; padding:12px; border-radius:6px">
            💡 <b>Saldo vs Nominal:</b> Fraud tersebar merata di semua level saldo dan nominal, 
            pelaku tidak terpaku pada nasabah kaya atau transaksi besar saja.
        </div>
        """, unsafe_allow_html=True)
    with ins2:
        st.markdown("""
        <div style="background:#f5f0ff; border-left:3px solid #f43f5e; padding:12px; border-radius:6px">
            💡 <b>Rasio Transaksi:</b> Fraud rate tertinggi pada transaksi <b>0–10% dari saldo</b>, 
            pelaku cenderung bertransaksi kecil relatif terhadap saldo untuk menghindari deteksi.
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        fig_hist_amount = go.Figure()
        fig_hist_amount.add_trace(go.Histogram(x=df[df['Is_Fraud']==0]['Transaction_Amount'],
            name="Normal", nbinsx=60, marker_color="#7c3aed", opacity=0.65))
        fig_hist_amount.add_trace(go.Histogram(x=df[df['Is_Fraud']==1]['Transaction_Amount'],
            name="Fraud", nbinsx=60, marker_color="#f43f5e", opacity=0.75))
        fig_hist_amount.update_layout(**CHART_LAYOUT, barmode="overlay", height=320,
            title="Distribusi Nominal Transaksi",
            xaxis_title="Nominal (INR)", yaxis_title="Frekuensi",
            xaxis=AXIS_STYLE, yaxis=AXIS_STYLE)
        st.plotly_chart(fig_hist_amount, width='stretch')

        fraud_median = df[df['Is_Fraud']==1]['Transaction_Amount'].median()
        normal_median = df[df['Is_Fraud']==0]['Transaction_Amount'].median()
        fraud_mean = df[df['Is_Fraud']==1]['Transaction_Amount'].mean()
        normal_mean = df[df['Is_Fraud']==0]['Transaction_Amount'].mean()
        selisih_pct = abs(fraud_mean - normal_mean) / normal_mean * 100

        st.markdown(f"""
        <div style="background:#f5f0ff; border-left:3px solid #a855f7; padding:12px; border-radius:6px">
            💡 Median nominal fraud <b>INR {fraud_median:,.0f}</b> vs normal <b>INR {normal_median:,.0f}</b> — 
            distribusi fraud {'lebih condong ke nominal tinggi' if fraud_median > normal_median else 'tersebar merata di semua nominal'}, 
            dengan rata-rata fraud <b>{selisih_pct:.1f}%</b> {'lebih tinggi' if fraud_mean > normal_mean else 'lebih rendah'} dari transaksi normal.
        </div>
        """, unsafe_allow_html=True)

    with col4:
        bc_stats = df.groupby('Is_Balance_Critical').agg(
            Total=('Is_Fraud','count'), Fraud=('Is_Fraud','sum')
        ).reset_index()
        bc_stats['Fraud_Rate'] = bc_stats['Fraud'] / bc_stats['Total'] * 100
        bc_stats['Label'] = bc_stats['Is_Balance_Critical'].map({0:'Saldo Normal', 1:'Saldo Kritis (<10%)'})
        fr_kritis = bc_stats[bc_stats['Is_Balance_Critical']==1]['Fraud_Rate'].values[0]
        fr_normal = bc_stats[bc_stats['Is_Balance_Critical']==0]['Fraud_Rate'].values[0]

        max_bc = bc_stats['Fraud_Rate'].max()
        colors_bc = ['#f43f5e' if v == max_bc else '#a855f7' for v in bc_stats['Fraud_Rate']]

        fig_bc = go.Figure(go.Bar(
            x=bc_stats['Label'],
            y=bc_stats['Fraud_Rate'],
            marker_color=colors_bc,
            text=[f"{v:.2f}%" for v in bc_stats['Fraud_Rate']],
            textposition='outside'
        ))
        fig_bc.update_layout(**CHART_LAYOUT, height=320,
            title="Fraud Rate: Saldo Kritis vs Normal",
            xaxis=dict(**AXIS_STYLE, title=""),
            yaxis=dict(**AXIS_STYLE, title="Fraud Rate (%)"),
        )
        st.plotly_chart(fig_bc, width='stretch')
        st.markdown(f"""
        <div style="background:#f5f0ff; border-left:3px solid #a855f7; padding:12px; border-radius:6px">
            💡 Perbedaan fraud rate hanya <b>{abs(fr_kritis-fr_normal):.2f}%</b> — 
            saldo rendah bukan indikator kuat terjadinya fraud.
        </div>
        """, unsafe_allow_html=True)
        
    sc_header("Rekomendasi Aturan Deteksi Berbasis Rasio", "Threshold deteksi fraud dari fitur finansial")
    rules_df = pd.DataFrame({
        'Aturan'     : ['Amount/Balance > 75%', 'Saldo kritis (<10% saldo awal)',
                        'Nominal < 10.000', 'Amount/Balance 0–10% + small amount'],
        'Basis Fitur': ['Amount_to_Balance_Ratio', 'Is_Balance_Critical',
                        'Is_Small_Amount_High_Risk', 'Kombinasi rasio + flag'],
        'Aksi'       : ['Wajib OTP', 'Blokir + notifikasi', '2FA + delay', 'Flag card testing'],
        'Prioritas'  : ['Tinggi', 'Tinggi', 'Tinggi', 'Tinggi'],
    })
    st.dataframe(rules_df, width='stretch', hide_index=True)

    st.markdown(insight_box(
        f"<b>Q6:</b> Rata-rata rasio Amount/Balance untuk fraud ({avg_ratio_fraud:.3f}) lebih tinggi "
        f"dari normal ({avg_ratio_normal:.3f}). Total estimasi kerugian: <b>INR {total_loss/1e9:.1f} Miliar</b>. "
        f"Transaksi dengan Amount/Balance > 75% atau nominal < 10.000 harus segera di-flag."
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: EVALUASI FITUR  (Menjawab pertanyaan ke 7)
# ═══════════════════════════════════════════════════════════════
elif "Evaluasi" in page and "Model" not in page:

    st.markdown(q_header(7, "Evaluasi Fitur",
        "Fitur dengan korelasi tertinggi terhadap fraud dan validasi hasil feature engineering."),
        unsafe_allow_html=True)

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    corr_fraud   = df[numeric_cols].corr()['Is_Fraud'].drop('Is_Fraud').abs().sort_values(ascending=False).dropna()

    top_feat = corr_fraud.index[0]
    top_corr = corr_fraud.iloc[0]

    st.markdown(f"""
    <div class="metric-grid">
        {metric_card("🥇", "danger",  "Fitur Korelasi Tertinggi", top_feat,             f"Korelasi {top_corr:.5f}",           "delta-up")}
        {metric_card("🔬", "purple",  "Total Fitur Numerik",      f"{len(corr_fraud)}", "Dianalisis korelasinya",             "delta-neutral")}
        {metric_card("⚙️", "warning", "Top-5 Avg Korelasi",       f"{corr_fraud.head(5).mean():.5f}", "Rata-rata 5 teratas", "delta-neutral")}
        {metric_card("📈", "success", "Fitur ke-2",               corr_fraud.index[1],  f"Korelasi {corr_fraud.iloc[1]:.5f}", "delta-neutral")}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.4, 1])

    with col1:
        colors_corr = ['#f43f5e' if i == 0 else '#c084fc' for i in range(len(corr_fraud))]

    fig_corr_bar = go.Figure(go.Bar(
        x=corr_fraud.values, y=corr_fraud.index, orientation='h',
        marker_color=colors_corr
    ))
    fig_corr_bar.update_layout(**CHART_LAYOUT, height=480,
        title="Korelasi Absolut Fitur terhadap Is_Fraud",
        xaxis_title="Korelasi Absolut", xaxis=AXIS_STYLE,
        yaxis=dict(**AXIS_STYLE, autorange='reversed'))
    st.plotly_chart(fig_corr_bar, width='stretch')

    # Insight Korelasi Absolut
    top1_feat  = corr_fraud.index[0]
    top1_val   = corr_fraud.values[0]
    top3_feats = ", ".join(corr_fraud.index[:3].tolist())
    st.markdown(f"""
    <div style="background:#f5f0ff; border-left:3px solid #a855f7; padding:12px; border-radius:6px; margin-bottom:20px">
        💡 Fitur paling berkorelasi dengan fraud adalah <b>{top1_feat}</b> 
        (korelasi absolut: <b>{top1_val:.5f}</b>). Tiga fitur teratas — <b>{top3_feats}</b> — 
        menunjukkan pola kombinasi waktu dan nominal transaksi sebagai sinyal fraud terkuat.
        Namun nilai korelasi yang rendah (&lt;0.01) mengindikasikan fraud bersifat 
        <b>multivariat</b> — tidak bisa dideteksi hanya dari satu fitur.
    </div>
    """, unsafe_allow_html=True)

    with col2:
        top10   = corr_fraud.head(10).index.tolist() + ['Is_Fraud']
    corr_matrix = df[top10].corr()
    fig_heatmap = px.imshow(corr_matrix, text_auto='.2f',
        color_continuous_scale=['#f5f0ff','#a855f7','#1a0533'],
        title="Korelasi Top 10 Fitur + Target", zmin=-1, zmax=1)
    fig_heatmap.update_layout(**CHART_LAYOUT, height=500)
    st.plotly_chart(fig_heatmap, width='stretch')

    # Insight Heatmap
    top_pair_val = corr_matrix['Is_Fraud'].drop('Is_Fraud').abs().idxmax()
    top_pair_corr = corr_matrix['Is_Fraud'][top_pair_val]

    # Cek multikolinearitas antar fitur (exclude Is_Fraud)
    sub = corr_matrix.drop('Is_Fraud', axis=0).drop('Is_Fraud', axis=1)
    mask = sub.abs() > 0.5
    n_high = int(mask.sum().sum() - len(sub))  # exclude diagonal
    n_high = max(n_high // 2, 0)               # simetris

    st.markdown(f"""
    <div style="background:#f5f0ff; border-left:3px solid #a855f7; padding:12px; border-radius:6px; margin-bottom:20px">
        💡 Dari heatmap, <b>{top_pair_val}</b> memiliki korelasi tertinggi terhadap 
        <b>Is_Fraud</b> sebesar <b>{top_pair_corr:+.3f}</b>. 
        {"Terdeteksi <b>" + str(n_high) + " pasang fitur</b> dengan korelasi antar-fitur > 0.5 — perlu diwaspadai <b>multikolinearitas</b> saat melatih model linear." if n_high > 0 else "Tidak terdeteksi multikolinearitas signifikan antar fitur — set fitur ini relatif <b>independen satu sama lain</b>."}
    </div>
    """, unsafe_allow_html=True)

    sc_header("Validasi Engineered Features", "Seberapa besar kondisi ini meningkatkan risiko fraud?")

    eng_features = [
        ('Is_Small_Amount_High_Risk', 'Small Amount (<10K)'),
        ('Is_Night_Transaction',      'Transaksi Malam'),
        ('Is_High_Risk_Combination',  'Malam + Mobile'),
        ('Is_Weekend_Small_Amount',   'Weekend + Small'),
        ('Is_High_Risk_Merchant',     'High Risk Merchant'),
        ('Is_High_Risk_Device',       'High Risk Device'),
        ('Is_Balance_Critical',       'Saldo Kritis'),
    ]

    eng_df = []
    for col_name, label in eng_features:
        fr_yes = df[df[col_name]==1]['Is_Fraud'].mean()*100
        fr_no  = df[df[col_name]==0]['Is_Fraud'].mean()*100
        eng_df.append({'Fitur': label, 'Ya (%)': round(fr_yes,3),
                    'Tidak (%)': round(fr_no,3), 'Selisih (%)': round(fr_yes-fr_no,3)})

    eng_df = pd.DataFrame(eng_df).sort_values('Selisih (%)', ascending=False)

    max_val = eng_df['Selisih (%)'].max()
    colors  = ['#f43f5e' if v == max_val else '#a855f7' for v in eng_df['Selisih (%)']]

    fig = go.Figure(go.Bar(
        x=eng_df['Fitur'], y=eng_df['Selisih (%)'],
        marker_color=colors,
        text=[f"+{v:.3f}%" for v in eng_df['Selisih (%)']],
        textposition='outside'
    ))
    fig.update_layout(**CHART_LAYOUT, height=380,
        title="Kenaikan Fraud Rate Saat Kondisi Terpenuhi",
        xaxis=dict(**AXIS_STYLE, tickangle=-20),
        yaxis=dict(**AXIS_STYLE, title="Selisih Fraud Rate (%)"))
    st.plotly_chart(fig, width='stretch')

    top, low = eng_df.iloc[0], eng_df.iloc[-1]
    st.markdown(f"""
    <div style="background:#f5f0ff; border-left:3px solid #a855f7; padding:12px; border-radius:6px">
        <b>{top['Fitur']}</b> paling meningkatkan risiko fraud (+{top['Selisih (%)']:.3f}%).
        Sebaliknya, <b>{low['Fitur']}</b> hampir tidak memberi perbedaan (+{low['Selisih (%)']:.3f}%) 
        — bukan sinyal fraud yang kuat.
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(eng_df, width='stretch', hide_index=True)

    st.markdown(insight_box(
        f"<b>Q7:</b> Fitur dengan korelasi tertinggi adalah <b>{corr_fraud.index[0]}</b> ({corr_fraud.iloc[0]:.5f}), "
        f"diikuti <b>{corr_fraud.index[1]}</b> ({corr_fraud.iloc[1]:.5f}). "
        f"Fitur engineered memiliki korelasi lebih tinggi dibanding fitur asli — "
        f"membuktikan feature engineering berhasil meningkatkan representasi pola fraud."
    ), unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<hr>
<div style="text-align: center; padding: 1rem 0; color: #9333ea; font-size: 12px;">
    SmartGuard Analytics Dashboard · CC26-PSU072
</div>
""", unsafe_allow_html=True)
