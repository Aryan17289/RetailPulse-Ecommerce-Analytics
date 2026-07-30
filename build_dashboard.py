import json

monthly = [
    {"month":"2016-10","orders":265,"revenue":46566.71},
    {"month":"2016-12","orders":1,"revenue":19.62},
    {"month":"2017-01","orders":750,"revenue":127545.67},
    {"month":"2017-02","orders":1653,"revenue":271298.65},
    {"month":"2017-03","orders":2546,"revenue":414369.39},
    {"month":"2017-04","orders":2303,"revenue":390952.18},
    {"month":"2017-05","orders":3546,"revenue":567066.73},
    {"month":"2017-06","orders":3135,"revenue":490225.60},
    {"month":"2017-07","orders":3872,"revenue":566403.93},
    {"month":"2017-08","orders":4193,"revenue":646000.61},
    {"month":"2017-09","orders":4150,"revenue":701169.99},
    {"month":"2017-10","orders":4478,"revenue":751140.27},
    {"month":"2017-11","orders":7289,"revenue":1153528.05},
    {"month":"2017-12","orders":5513,"revenue":843199.17},
    {"month":"2018-01","orders":7069,"revenue":1078606.86},
    {"month":"2018-02","orders":6555,"revenue":966510.88},
    {"month":"2018-03","orders":7003,"revenue":1120678.00},
    {"month":"2018-04","orders":6798,"revenue":1132933.95},
    {"month":"2018-05","orders":6749,"revenue":1128836.69},
    {"month":"2018-06","orders":6099,"revenue":1012090.68},
    {"month":"2018-07","orders":6159,"revenue":1027903.86},
    {"month":"2018-08","orders":6351,"revenue":985414.28},
]
categories = [
    {"category":"Bed & Bath Table","orders":9272,"revenue":1692714.28},
    {"category":"Health & Beauty","orders":8646,"revenue":1620684.04},
    {"category":"Computers & Accessories","orders":6530,"revenue":1549372.59},
    {"category":"Furniture & Decor","orders":6307,"revenue":1394466.93},
    {"category":"Watches & Gifts","orders":5495,"revenue":1387362.45},
    {"category":"Sports & Leisure","orders":7530,"revenue":1349446.93},
    {"category":"Housewares","orders":5743,"revenue":1069787.97},
    {"category":"Auto","orders":3810,"revenue":833745.67},
    {"category":"Garden Tools","orders":3448,"revenue":810614.93},
    {"category":"Cool Stuff","orders":3559,"revenue":744649.32},
]
states = [
    {"state":"SP","orders":40500,"revenue":5770266.19},
    {"state":"RJ","orders":12350,"revenue":2055690.45},
    {"state":"MG","orders":11354,"revenue":1819277.61},
    {"state":"RS","orders":5345,"revenue":861802.40},
    {"state":"PR","orders":4923,"revenue":781919.55},
    {"state":"SC","orders":3546,"revenue":595208.40},
    {"state":"BA","orders":3256,"revenue":591270.60},
    {"state":"DF","orders":2080,"revenue":346146.17},
    {"state":"GO","orders":1957,"revenue":334294.22},
    {"state":"ES","orders":1995,"revenue":317682.65},
]
aov = [
    {"month":"2016-10","aov":175.72},{"month":"2017-01","aov":170.06},
    {"month":"2017-02","aov":164.13},{"month":"2017-03","aov":162.75},
    {"month":"2017-04","aov":169.76},{"month":"2017-05","aov":159.92},
    {"month":"2017-06","aov":156.37},{"month":"2017-07","aov":146.28},
    {"month":"2017-08","aov":154.07},{"month":"2017-09","aov":168.96},
    {"month":"2017-10","aov":167.74},{"month":"2017-11","aov":158.26},
    {"month":"2017-12","aov":152.95},{"month":"2018-01","aov":152.58},
    {"month":"2018-02","aov":147.45},{"month":"2018-03","aov":160.03},
    {"month":"2018-04","aov":166.66},{"month":"2018-05","aov":167.26},
    {"month":"2018-06","aov":165.94},{"month":"2018-07","aov":166.89},
    {"month":"2018-08","aov":155.16},
]
rfm = [
    {"segment":"New Customer","customers":38227,"avg_recency":92,"avg_frequency":1.0,"avg_monetary":168.10,"total_revenue":6426016.31},
    {"segment":"Potential","customers":33953,"avg_recency":265,"avg_frequency":1.0,"avg_monetary":144.34,"total_revenue":4900877.63},
    {"segment":"Lost","customers":19284,"avg_recency":463,"avg_frequency":1.0,"avg_monetary":124.71,"total_revenue":2404973.50},
    {"segment":"Cannot Lose","customers":1665,"avg_recency":396,"avg_frequency":1.1,"avg_monetary":945.97,"total_revenue":1575045.50},
    {"segment":"Loyal","customers":126,"avg_recency":127,"avg_frequency":3.1,"avg_monetary":457.32,"total_revenue":57622.78},
    {"segment":"At Risk","customers":69,"avg_recency":392,"avg_frequency":3.1,"avg_monetary":425.08,"total_revenue":29330.81},
    {"segment":"Champion","customers":33,"avg_recency":85,"avg_frequency":4.9,"avg_monetary":866.52,"total_revenue":28595.24},
]

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>E-Commerce Analytics — Olist Brazil</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden;font-family:'Inter',sans-serif;background:#EEF2FF;color:#1e2235}

/* ── LAYOUT ── */
.app{display:flex;height:100vh;width:100vw;overflow:hidden}

/* ── SIDEBAR ── */
.sidebar{
  width:200px;flex-shrink:0;background:#1e2235;
  display:flex;flex-direction:column;overflow:hidden;
  box-shadow:2px 0 12px rgba(0,0,0,0.2)
}
.logo{padding:16px 14px 12px;border-bottom:1px solid rgba(255,255,255,0.07)}
.logo-icon{font-size:18px;margin-bottom:4px}
.logo h1{font-size:12px;font-weight:700;color:#fff;line-height:1.3}
.logo p{font-size:9px;color:rgba(255,255,255,0.35);margin-top:2px}
.nav-section{padding:12px 10px 4px;font-size:8px;font-weight:700;
  color:rgba(255,255,255,0.25);letter-spacing:.1em;text-transform:uppercase}
.nav-item{
  display:flex;align-items:center;gap:8px;padding:8px 14px;
  cursor:pointer;color:rgba(255,255,255,0.5);font-size:11px;font-weight:500;
  border-left:2px solid transparent;transition:all .15s;user-select:none
}
.nav-item:hover{background:rgba(255,255,255,0.05);color:#fff}
.nav-item.active{background:rgba(41,98,255,0.18);color:#fff;border-left-color:#2962FF}
.nav-icon{font-size:13px;width:18px;text-align:center;flex-shrink:0}
.nav-badge{margin-left:auto;background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.4);
  font-size:8px;padding:1px 5px;border-radius:8px}
.sidebar-foot{margin-top:auto;padding:10px 14px;border-top:1px solid rgba(255,255,255,0.07);
  font-size:8px;color:rgba(255,255,255,0.2);line-height:1.6}

/* ── MAIN AREA ── */
.main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}

/* ── TOPBAR ── */
.topbar{
  background:#fff;border-bottom:1px solid #dde3f0;
  padding:0 20px;height:46px;flex-shrink:0;
  display:flex;align-items:center;justify-content:space-between;
  box-shadow:0 1px 6px rgba(0,0,0,0.05)
}
.topbar-title{font-size:14px;font-weight:700;color:#1e2235}
.topbar-sub{font-size:10px;color:#9ba3c0;margin-top:1px}
.live-badge{background:#e6f9f2;color:#00b67a;font-size:9px;font-weight:700;
  padding:3px 10px;border-radius:20px;display:flex;align-items:center;gap:4px}
.live-dot{width:5px;height:5px;border-radius:50%;background:#00b67a;animation:pulse 1.5s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}

/* ── FILTER BAR ── */
.filterbar{
  background:#fff;border-bottom:1px solid #dde3f0;
  padding:7px 20px;flex-shrink:0;
  display:flex;align-items:center;gap:14px;flex-wrap:wrap
}
.filter-label{font-size:9px;font-weight:700;color:#9ba3c0;
  text-transform:uppercase;letter-spacing:.07em;white-space:nowrap}
.filter-group{display:flex;gap:4px}
.fbtn{
  padding:4px 12px;border-radius:20px;font-size:10px;font-weight:600;
  cursor:pointer;border:1.5px solid #dde3f0;background:#fff;
  color:#5a6180;transition:all .15s;font-family:'Inter',sans-serif
}
.fbtn:hover{border-color:#2962FF;color:#2962FF}
.fbtn.active{background:#2962FF;color:#fff;border-color:#2962FF}
.filter-sep{width:1px;height:18px;background:#dde3f0}
.filter-info{font-size:10px;color:#2962FF;font-weight:600}

/* ── SCROLL AREA ── */
.scroll{flex:1;overflow-y:auto;overflow-x:hidden;padding:14px 20px 14px}
.scroll::-webkit-scrollbar{width:4px}
.scroll::-webkit-scrollbar-track{background:transparent}
.scroll::-webkit-scrollbar-thumb{background:#dde3f0;border-radius:4px}

/* ── PAGES ── */
.page{display:none}
.page.active{display:block}

/* ── KPI GRID ── */
.kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:12px}
.kpi{
  background:#fff;border-radius:10px;padding:12px 14px;
  border:1px solid #dde3f0;position:relative;overflow:hidden;
  transition:transform .2s,box-shadow .2s
}
.kpi:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.07)}
.kpi::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.kpi.blue::before{background:#2962FF}
.kpi.green::before{background:#00b67a}
.kpi.purple::before{background:#7b2fbe}
.kpi.orange::before{background:#ff8c00}
.kpi-ico{position:absolute;right:12px;top:12px;font-size:20px;opacity:.1}
.kpi-lbl{font-size:9px;font-weight:700;color:#9ba3c0;
  text-transform:uppercase;letter-spacing:.07em;margin-bottom:5px}
.kpi-val{font-size:20px;font-weight:800;line-height:1;margin-bottom:3px}
.kpi.blue .kpi-val{color:#2962FF}
.kpi.green .kpi-val{color:#00b67a}
.kpi.purple .kpi-val{color:#7b2fbe}
.kpi.orange .kpi-val{color:#ff8c00}
.kpi-delta{font-size:9px;font-weight:600}
.up{color:#00b67a}.dn{color:#ff4d4d}

/* ── INSIGHT BOX ── */
.insight{
  background:linear-gradient(135deg,#eef3ff,#f3eeff);
  border:1px solid #c7d7ff;border-radius:10px;
  padding:10px 14px;margin-bottom:12px;
  display:flex;align-items:flex-start;gap:10px
}
.insight-ico{font-size:16px;flex-shrink:0;margin-top:1px}
.insight-title{font-size:11px;font-weight:700;color:#2962FF;margin-bottom:2px}
.insight-text{font-size:10px;color:#5a6180;line-height:1.5}

/* ── CHART GRID ── */
.chart-grid{display:grid;gap:10px;margin-bottom:12px}
.g2{grid-template-columns:1.6fr 1fr}
.g2e{grid-template-columns:1fr 1fr}
.g1{grid-template-columns:1fr}
.chart-card{
  background:#fff;border-radius:10px;padding:14px 16px;
  border:1px solid #dde3f0;transition:box-shadow .2s
}
.chart-card:hover{box-shadow:0 4px 16px rgba(0,0,0,0.06)}
.chart-head{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:10px}
.chart-title{font-size:11px;font-weight:700;color:#1e2235}
.chart-sub{font-size:9px;color:#9ba3c0;margin-top:2px}
.chart-tag{font-size:9px;font-weight:600;padding:2px 7px;
  border-radius:20px;background:#eef3ff;color:#2962FF;white-space:nowrap;flex-shrink:0}

/* ── SEGMENT GRID ── */
.seg-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;height:calc(100% - 36px)}
.seg-card{border-radius:8px;padding:8px 10px;border:1px solid #dde3f0;
  cursor:pointer;transition:all .15s}
.seg-card:hover{transform:scale(1.02);box-shadow:0 4px 12px rgba(0,0,0,0.08)}
.seg-card.new{background:#eef3ff;border-color:#90caf9}
.seg-card.potential{background:#f3eeff;border-color:#ce93d8}
.seg-card.lost{background:#f5f5f5;border-color:#e0e0e0}
.seg-card.cannotlose{background:#fff0f0;border-color:#ef9a9a}
.seg-card.champion{background:#fff8e1;border-color:#ffe082}
.seg-card.atrisk{background:#fff4e0;border-color:#ffcc80}
.seg-name{font-size:8px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:3px}
.seg-card.new .seg-name{color:#2962FF}
.seg-card.potential .seg-name{color:#7b2fbe}
.seg-card.lost .seg-name{color:#757575}
.seg-card.cannotlose .seg-name{color:#ff4d4d}
.seg-card.champion .seg-name{color:#ff8c00}
.seg-card.atrisk .seg-name{color:#e65100}
.seg-count{font-size:17px;font-weight:800;color:#1e2235}
.seg-detail{font-size:8px;color:#9ba3c0;margin-top:1px}

/* ── SCROLLBAR STYLE ── */
</style>
</head>
<body>
<div class="app">

<!-- SIDEBAR -->
<nav class="sidebar">
  <div class="logo">
    <div class="logo-icon">🛒</div>
    <h1>Olist Analytics</h1>
    <p>E-Commerce · Brazil · 2016–2018</p>
  </div>
  <div class="nav-section">Dashboard</div>
  <div class="nav-item active" onclick="showPage('overview',this)">
    <span class="nav-icon">📊</span><span>Executive Overview</span>
  </div>
  <div class="nav-item" onclick="showPage('segments',this)">
    <span class="nav-icon">👥</span><span>Customer Segments</span><span class="nav-badge">RFM</span>
  </div>
  <div class="nav-item" onclick="showPage('products',this)">
    <span class="nav-icon">📦</span><span>Product Performance</span>
  </div>
  <div class="nav-item" onclick="showPage('location',this)">
    <span class="nav-icon">🗺️</span><span>Geographic Analysis</span>
  </div>
  <div class="nav-item" onclick="showPage('aov',this)">
    <span class="nav-icon">📉</span><span>Order Value Trends</span>
  </div>
  <div class="sidebar-foot">
    Built with Python + SQLite<br>
    Olist Dataset · 99,441 orders<br>
    Aryan Chauhan · 2024
  </div>
</nav>

<!-- MAIN -->
<div class="main">

  <!-- TOPBAR -->
  <div class="topbar">
    <div>
      <div class="topbar-title" id="page-title">Executive Overview</div>
      <div class="topbar-sub">Olist Brazil E-Commerce · 99,441 delivered orders · 2016–2018</div>
    </div>
    <div class="live-badge"><div class="live-dot"></div>SQLite · Live Data</div>
  </div>

  <!-- FILTER BAR -->
  <div class="filterbar">
    <span class="filter-label">Filter by Year</span>
    <div class="filter-group">
      <button class="fbtn active" onclick="filterYear('all',this)">All Years</button>
      <button class="fbtn" onclick="filterYear('2016',this)">2016</button>
      <button class="fbtn" onclick="filterYear('2017',this)">2017</button>
      <button class="fbtn" onclick="filterYear('2018',this)">2018</button>
    </div>
    <div class="filter-sep"></div>
    <span class="filter-info" id="filter-info">22 months · R$16.0M total · 96,478 orders</span>
  </div>

  <!-- SCROLL AREA -->
  <div class="scroll">

    <!-- PAGE 1: OVERVIEW -->
    <div class="page active" id="page-overview">
      <div class="kpi-grid">
        <div class="kpi blue"><div class="kpi-ico">💰</div>
          <div class="kpi-lbl">Total Revenue</div>
          <div class="kpi-val" id="kpi-rev">R$16.0M</div>
          <div class="kpi-delta up" id="kpi-rev-d">↑ 25× growth from Oct 2016</div>
        </div>
        <div class="kpi green"><div class="kpi-ico">🛒</div>
          <div class="kpi-lbl">Total Orders</div>
          <div class="kpi-val" id="kpi-ord">96,478</div>
          <div class="kpi-delta up">↑ 97% successfully delivered</div>
        </div>
        <div class="kpi purple"><div class="kpi-ico">👤</div>
          <div class="kpi-lbl">Unique Customers</div>
          <div class="kpi-val">93,357</div>
          <div class="kpi-delta dn">↓ 93% bought only once</div>
        </div>
        <div class="kpi orange"><div class="kpi-ico">🧾</div>
          <div class="kpi-lbl">Avg Order Value</div>
          <div class="kpi-val" id="kpi-aov">R$160</div>
          <div class="kpi-delta dn">↓ Declining since 2016</div>
        </div>
      </div>
      <div class="insight">
        <div class="insight-ico">💡</div>
        <div>
          <div class="insight-title">Revenue grew 25× in 13 months — but AOV is declining</div>
          <div class="insight-text">Revenue jumped from R$46K (Oct 2016) to R$1.15M (Nov 2017) driven by Black Friday. However avg order value dropped from R$175 to R$147 — customers are buying cheaper items. The business should focus on upselling and retention rather than pure acquisition.</div>
        </div>
      </div>
      <div class="chart-grid g2">
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Monthly Revenue Trend</div><div class="chart-sub">Bar = revenue · Line = order volume · Orange = Nov 2017 Black Friday peak</div></div>
            <span class="chart-tag">Bar + Line</span>
          </div>
          <canvas id="c-revenue" height="160"></canvas>
        </div>
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Orders by Status</div><div class="chart-sub">97% of all orders delivered successfully</div></div>
            <span class="chart-tag">Donut</span>
          </div>
          <canvas id="c-status" height="160"></canvas>
        </div>
      </div>
    </div>

    <!-- PAGE 2: SEGMENTS -->
    <div class="page" id="page-segments">
      <div class="insight">
        <div class="insight-ico">⚠️</div>
        <div>
          <div class="insight-title">Critical: 93% of customers never repurchase — massive retention problem</div>
          <div class="insight-text">Only 33 Champions and 126 Loyal customers out of 93,357 total. The "Cannot Lose" segment (1,665 customers) spends R$946 avg but is drifting away — highest priority for re-engagement campaigns.</div>
        </div>
      </div>
      <div class="chart-grid g2e">
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Revenue by Customer Segment</div><div class="chart-sub">Total monetary contribution per RFM group</div></div>
            <span class="chart-tag">Horizontal Bar</span>
          </div>
          <canvas id="c-rfm-rev" height="200"></canvas>
        </div>
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Customer Segments</div><div class="chart-sub">Click a tile to highlight · RFM classification</div></div>
            <span class="chart-tag">RFM Tiles</span>
          </div>
          <div class="seg-grid">
            <div class="seg-card new" onclick="hlSeg(this)">
              <div class="seg-name">🆕 New Customer</div>
              <div class="seg-count">38,227</div>
              <div class="seg-detail">Avg R$168 · Recency 92d</div>
            </div>
            <div class="seg-card potential" onclick="hlSeg(this)">
              <div class="seg-name">✨ Potential</div>
              <div class="seg-count">33,953</div>
              <div class="seg-detail">Avg R$144 · Recency 265d</div>
            </div>
            <div class="seg-card lost" onclick="hlSeg(this)">
              <div class="seg-name">💀 Lost</div>
              <div class="seg-count">19,284</div>
              <div class="seg-detail">Last seen 463 days ago</div>
            </div>
            <div class="seg-card cannotlose" onclick="hlSeg(this)">
              <div class="seg-name">⚠️ Cannot Lose</div>
              <div class="seg-count">1,665</div>
              <div class="seg-detail">Avg R$946 · High value!</div>
            </div>
            <div class="seg-card champion" onclick="hlSeg(this)">
              <div class="seg-name">🏆 Champion</div>
              <div class="seg-count">33</div>
              <div class="seg-detail">Avg R$867 · 4.9 orders</div>
            </div>
            <div class="seg-card atrisk" onclick="hlSeg(this)">
              <div class="seg-name">🔥 At Risk</div>
              <div class="seg-count">69</div>
              <div class="seg-detail">Avg R$425 · Going cold</div>
            </div>
          </div>
        </div>
      </div>
      <div class="chart-grid g1">
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Segment Bubble Chart — Avg Spend vs Recency</div><div class="chart-sub">Bubble size = number of customers · X = avg spend · Y = days since last purchase</div></div>
            <span class="chart-tag">Bubble</span>
          </div>
          <canvas id="c-bubble" height="130"></canvas>
        </div>
      </div>
    </div>

    <!-- PAGE 3: PRODUCTS -->
    <div class="page" id="page-products">
      <div class="kpi-grid">
        <div class="kpi blue"><div class="kpi-ico">🛏️</div><div class="kpi-lbl">Top Category</div><div class="kpi-val" style="font-size:14px;padding-top:3px">Bed & Bath</div><div class="kpi-delta up">R$1.69M revenue</div></div>
        <div class="kpi green"><div class="kpi-ico">📦</div><div class="kpi-lbl">Most Orders</div><div class="kpi-val" style="font-size:14px;padding-top:3px">Bed & Bath</div><div class="kpi-delta up">9,272 orders</div></div>
        <div class="kpi purple"><div class="kpi-ico">💻</div><div class="kpi-lbl">Highest Avg Price</div><div class="kpi-val" style="font-size:14px;padding-top:3px">Computers</div><div class="kpi-delta up">R$237 per order</div></div>
        <div class="kpi orange"><div class="kpi-ico">📋</div><div class="kpi-lbl">Total Categories</div><div class="kpi-val">71</div><div class="kpi-delta up">Top 10 = 68% revenue</div></div>
      </div>
      <div class="chart-grid g2e">
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Top 10 Categories by Revenue</div><div class="chart-sub">Hover bars for exact values</div></div>
            <span class="chart-tag">Horizontal Bar</span>
          </div>
          <canvas id="c-cat-rev" height="240"></canvas>
        </div>
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Revenue vs Order Count</div><div class="chart-sub">Orders ≠ Revenue — see the difference</div></div>
            <span class="chart-tag">Grouped Bar</span>
          </div>
          <canvas id="c-cat-cmp" height="240"></canvas>
        </div>
      </div>
    </div>

    <!-- PAGE 4: LOCATION -->
    <div class="page" id="page-location">
      <div class="kpi-grid">
        <div class="kpi blue"><div class="kpi-ico">🏙️</div><div class="kpi-lbl">Top State</div><div class="kpi-val" style="font-size:14px;padding-top:3px">São Paulo</div><div class="kpi-delta up">R$5.77M · 40,500 orders</div></div>
        <div class="kpi green"><div class="kpi-ico">📍</div><div class="kpi-lbl">SP Revenue Share</div><div class="kpi-val">36%</div><div class="kpi-delta up">3× more than RJ</div></div>
        <div class="kpi purple"><div class="kpi-ico">🗺️</div><div class="kpi-lbl">States Active</div><div class="kpi-val">27</div><div class="kpi-delta up">Nationwide reach</div></div>
        <div class="kpi orange"><div class="kpi-ico">📦</div><div class="kpi-lbl">2nd State</div><div class="kpi-val" style="font-size:14px;padding-top:3px">Rio de Janeiro</div><div class="kpi-delta">R$2.06M</div></div>
      </div>
      <div class="chart-grid g2e">
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Revenue by State — Top 10</div><div class="chart-sub">SP dominates with 36% of total revenue</div></div>
            <span class="chart-tag">Bar Chart</span>
          </div>
          <canvas id="c-st-rev" height="240"></canvas>
        </div>
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Orders by State — Top 10</div><div class="chart-sub">Compare order volume vs revenue</div></div>
            <span class="chart-tag">Bar Chart</span>
          </div>
          <canvas id="c-st-ord" height="240"></canvas>
        </div>
      </div>
    </div>

    <!-- PAGE 5: AOV -->
    <div class="page" id="page-aov">
      <div class="kpi-grid">
        <div class="kpi blue"><div class="kpi-ico">📈</div><div class="kpi-lbl">Peak AOV</div><div class="kpi-val">R$175.72</div><div class="kpi-delta">Oct 2016</div></div>
        <div class="kpi orange" style="--c:#ff4d4d"><div class="kpi-ico">📉</div><div class="kpi-lbl">Lowest AOV</div><div class="kpi-val" style="color:#ff4d4d">R$147.45</div><div class="kpi-delta dn">Feb 2018</div></div>
        <div class="kpi green"><div class="kpi-ico">🧾</div><div class="kpi-lbl">Overall Average</div><div class="kpi-val">R$160.4</div><div class="kpi-delta">All months</div></div>
        <div class="kpi purple"><div class="kpi-ico">⬇️</div><div class="kpi-lbl">Total Drop</div><div class="kpi-val">−16%</div><div class="kpi-delta dn">Oct 2016 → Feb 2018</div></div>
      </div>
      <div class="insight">
        <div class="insight-ico">📉</div>
        <div>
          <div class="insight-title">AOV declining — customers shifting to cheaper products</div>
          <div class="insight-text">Average order value dropped 16% from R$175 to R$147 between Oct 2016 and Feb 2018. Recommendation: introduce product bundling and minimum order value incentives (e.g. free shipping above R$200) to lift AOV back above R$170.</div>
        </div>
      </div>
      <div class="chart-grid g1">
        <div class="chart-card">
          <div class="chart-head">
            <div><div class="chart-title">Average Order Value by Month — with Trend Line</div><div class="chart-sub">Dashed red line = linear trend showing overall decline</div></div>
            <span class="chart-tag">Line + Trend</span>
          </div>
          <canvas id="c-aov" height="200"></canvas>
        </div>
      </div>
    </div>

  </div><!-- /scroll -->
</div><!-- /main -->
</div><!-- /app -->

<script>
const monthly="""+json.dumps(monthly)+""";
const categories="""+json.dumps(categories)+""";
const states="""+json.dumps(states)+""";
const aovData="""+json.dumps(aov)+""";
const rfmData="""+json.dumps(rfm)+""";

Chart.defaults.font.family="'Inter',sans-serif";
Chart.defaults.font.size=10;
Chart.defaults.color='#5a6180';
Chart.defaults.plugins.legend.labels.boxWidth=8;
Chart.defaults.plugins.legend.labels.padding=10;
Chart.defaults.plugins.legend.labels.usePointStyle=true;

const C={blue:'#2962FF',green:'#00b67a',purple:'#7b2fbe',orange:'#ff8c00',red:'#ff4d4d',teal:'#00bcd4'};
let charts={};
let yr='all';

function getMon(){return yr==='all'?monthly:monthly.filter(d=>d.month.startsWith(yr))}

function buildRevenue(){
  const d=getMon();
  const ctx=document.getElementById('c-revenue');
  if(!ctx)return;
  if(charts.rev)charts.rev.destroy();
  charts.rev=new Chart(ctx,{
    type:'bar',
    data:{
      labels:d.map(x=>x.month),
      datasets:[
        {label:'Revenue (R$)',data:d.map(x=>x.revenue),
         backgroundColor:d.map(x=>x.month==='2017-11'?C.orange:x.month.startsWith('2018')?C.blue+'CC':C.blue+'77'),
         borderRadius:3,yAxisID:'y',order:2},
        {label:'Orders',data:d.map(x=>x.orders),type:'line',
         borderColor:C.green,backgroundColor:C.green+'15',
         borderWidth:2,pointRadius:2,pointBackgroundColor:C.green,
         yAxisID:'y2',tension:0.4,fill:true,order:1}
      ]
    },
    options:{responsive:true,
      interaction:{mode:'index',intersect:false},
      plugins:{legend:{position:'top'},
        tooltip:{callbacks:{label:c=>c.dataset.label==='Revenue (R$)'?
          ' R$'+c.raw.toLocaleString('en',{maximumFractionDigits:0}):
          ' '+c.raw.toLocaleString()+' orders'}}
      },
      scales:{
        y:{position:'left',grid:{color:'#f0f4ff'},ticks:{callback:v=>'R$'+Math.round(v/1000)+'K',font:{size:9}}},
        y2:{position:'right',grid:{display:false},ticks:{callback:v=>v.toLocaleString(),font:{size:9}}},
        x:{grid:{display:false},ticks:{maxRotation:45,minRotation:45,font:{size:8}}}
      }
    }
  });
}

function buildStatus(){
  const ctx=document.getElementById('c-status');
  if(!ctx)return;
  if(charts.status)charts.status.destroy();
  charts.status=new Chart(ctx,{
    type:'doughnut',
    data:{
      labels:['Delivered','Shipped','Canceled','Others'],
      datasets:[{data:[96478,1107,625,1231],
        backgroundColor:[C.blue,C.green,C.red,'#e2e8f8'],
        borderWidth:2,borderColor:'#fff',hoverOffset:6}]
    },
    options:{responsive:true,cutout:'70%',
      plugins:{legend:{position:'bottom',labels:{font:{size:9}}},
        tooltip:{callbacks:{label:c=>` ${c.label}: ${c.raw.toLocaleString()} (${(c.raw/99441*100).toFixed(1)}%)`}}
      }
    }
  });
}

function buildRFMRev(){
  const ctx=document.getElementById('c-rfm-rev');
  if(!ctx)return;
  if(charts.rfmr)charts.rfmr.destroy();
  const s=[...rfmData].sort((a,b)=>b.total_revenue-a.total_revenue);
  const sc={'New Customer':C.blue,'Potential':C.purple,'Lost':'#9e9e9e',
    'Cannot Lose':C.red,'Loyal':C.green,'At Risk':C.orange,'Champion':'#ffb300'};
  charts.rfmr=new Chart(ctx,{
    type:'bar',
    data:{labels:s.map(d=>d.segment),
      datasets:[{label:'Total Revenue',data:s.map(d=>d.total_revenue),
        backgroundColor:s.map(d=>sc[d.segment]||C.blue),borderRadius:4}]},
    options:{indexAxis:'y',responsive:true,
      plugins:{legend:{display:false},
        tooltip:{callbacks:{label:c=>` R$${c.raw.toLocaleString('en',{maximumFractionDigits:0})}`}}
      },
      scales:{x:{grid:{color:'#f0f4ff'},ticks:{callback:v=>'R$'+Math.round(v/1000)+'K',font:{size:9}}},
        y:{grid:{display:false},ticks:{font:{size:9}}}}
    }
  });
}

function buildBubble(){
  const ctx=document.getElementById('c-bubble');
  if(!ctx)return;
  if(charts.bubble)charts.bubble.destroy();
  const sc={'New Customer':C.blue,'Potential':C.purple,'Lost':'#9e9e9e',
    'Cannot Lose':C.red,'Loyal':C.green,'At Risk':C.orange,'Champion':'#ffb300'};
  charts.bubble=new Chart(ctx,{
    type:'bubble',
    data:{datasets:rfmData.map(d=>({
      label:d.segment,
      data:[{x:d.avg_monetary,y:d.avg_recency,r:Math.sqrt(d.customers)/4+4}],
      backgroundColor:(sc[d.segment]||C.blue)+'99',
      borderColor:sc[d.segment]||C.blue,borderWidth:1.5
    }))},
    options:{responsive:true,
      plugins:{legend:{position:'right',labels:{font:{size:9}}},
        tooltip:{callbacks:{label:c=>[` ${c.dataset.label}`,` Spend: R$${c.parsed.x}`,` Recency: ${c.parsed.y}d`]}}
      },
      scales:{
        x:{title:{display:true,text:'Avg Monetary (R$)',font:{size:9}},grid:{color:'#f0f4ff'}},
        y:{title:{display:true,text:'Avg Recency (days)',font:{size:9}},grid:{color:'#f0f4ff'}}
      }
    }
  });
}

function buildCatCharts(){
  const ctx1=document.getElementById('c-cat-rev');
  const ctx2=document.getElementById('c-cat-cmp');
  if(!ctx1||!ctx2)return;
  if(charts.cr)charts.cr.destroy();
  if(charts.cc)charts.cc.destroy();
  const pal=[C.blue,C.purple,C.blue,C.purple,C.blue,C.purple,C.blue,C.purple,C.blue,C.purple];
  const labs=categories.map(d=>d.category);
  charts.cr=new Chart(ctx1,{type:'bar',
    data:{labels:labs,datasets:[{label:'Revenue',data:categories.map(d=>d.revenue),
      backgroundColor:pal,borderRadius:3}]},
    options:{indexAxis:'y',responsive:true,
      plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>` R$${c.raw.toLocaleString('en',{maximumFractionDigits:0})}`}}},
      scales:{x:{grid:{color:'#f0f4ff'},ticks:{callback:v=>'R$'+Math.round(v/1000)+'K',font:{size:9}}},
        y:{grid:{display:false},ticks:{font:{size:9}}}}
    }
  });
  charts.cc=new Chart(ctx2,{type:'bar',
    data:{labels:labs,datasets:[
      {label:'Revenue (K)',data:categories.map(d=>Math.round(d.revenue/1000)),
        backgroundColor:C.blue+'CC',borderRadius:3},
      {label:'Orders',data:categories.map(d=>d.orders),
        backgroundColor:C.purple+'CC',borderRadius:3}
    ]},
    options:{indexAxis:'y',responsive:true,
      plugins:{legend:{position:'top',labels:{font:{size:9}}}},
      scales:{x:{grid:{color:'#f0f4ff'},ticks:{font:{size:9}}},
        y:{grid:{display:false},ticks:{font:{size:9}}}}
    }
  });
}

function buildStateCharts(){
  const ctx1=document.getElementById('c-st-rev');
  const ctx2=document.getElementById('c-st-ord');
  if(!ctx1||!ctx2)return;
  if(charts.sr)charts.sr.destroy();
  if(charts.so)charts.so.destroy();
  const labs=states.map(d=>d.state);
  charts.sr=new Chart(ctx1,{type:'bar',
    data:{labels:labs,datasets:[{label:'Revenue',data:states.map(d=>d.revenue),
      backgroundColor:states.map((_,i)=>i===0?C.blue:C.blue+'77'),borderRadius:4}]},
    options:{responsive:true,plugins:{legend:{display:false},
      tooltip:{callbacks:{label:c=>` R$${c.raw.toLocaleString('en',{maximumFractionDigits:0})}`}}},
      scales:{y:{grid:{color:'#f0f4ff'},ticks:{callback:v=>'R$'+Math.round(v/1000)+'K',font:{size:9}}},
        x:{grid:{display:false},ticks:{font:{size:9}}}}
    }
  });
  charts.so=new Chart(ctx2,{type:'bar',
    data:{labels:labs,datasets:[{label:'Orders',data:states.map(d=>d.orders),
      backgroundColor:states.map((_,i)=>i===0?C.purple:C.purple+'77'),borderRadius:4}]},
    options:{responsive:true,plugins:{legend:{display:false},
      tooltip:{callbacks:{label:c=>` ${c.raw.toLocaleString()} orders`}}},
      scales:{y:{grid:{color:'#f0f4ff'},ticks:{callback:v=>v.toLocaleString(),font:{size:9}}},
        x:{grid:{display:false},ticks:{font:{size:9}}}}
    }
  });
}

function buildAOV(){
  const ctx=document.getElementById('c-aov');
  if(!ctx)return;
  if(charts.aov)charts.aov.destroy();
  const filtered=yr==='all'?aovData:aovData.filter(d=>d.month.startsWith(yr));
  const vals=filtered.map(d=>d.aov);
  const labs=filtered.map(d=>d.month);
  const n=vals.length,xm=(n-1)/2,ym=vals.reduce((a,b)=>a+b,0)/n;
  const slope=vals.reduce((s,y,i)=>s+(i-xm)*(y-ym),0)/vals.reduce((s,_,i)=>s+(i-xm)**2,0);
  const trend=vals.map((_,i)=>+(ym+slope*(i-xm)).toFixed(2));
  charts.aov=new Chart(ctx,{type:'line',
    data:{labels:labs,datasets:[
      {label:'Avg Order Value',data:vals,borderColor:C.orange,
        backgroundColor:C.orange+'15',borderWidth:2.5,pointRadius:3,
        pointBackgroundColor:C.orange,tension:0.4,fill:true},
      {label:'Trend',data:trend,borderColor:C.red,borderWidth:1.5,
        borderDash:[5,4],pointRadius:0,tension:0}
    ]},
    options:{responsive:true,interaction:{mode:'index',intersect:false},
      plugins:{legend:{position:'top',labels:{font:{size:9}}},
        tooltip:{callbacks:{label:c=>` ${c.dataset.label}: R$${c.raw.toFixed(2)}`}}
      },
      scales:{y:{grid:{color:'#f0f4ff'},min:130,max:185,
        ticks:{callback:v=>'R$'+v,font:{size:9}}},
        x:{grid:{display:false},ticks:{maxRotation:45,minRotation:45,font:{size:8}}}
      }
    }
  });
}

function filterYear(year,btn){
  yr=year;
  document.querySelectorAll('.fbtn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  const d=getMon();
  const rev=d.reduce((s,x)=>s+x.revenue,0);
  const ord=d.reduce((s,x)=>s+x.orders,0);
  const av=yr==='all'?aovData:aovData.filter(x=>x.month.startsWith(yr));
  const maov=av.length?av.reduce((s,x)=>s+x.aov,0)/av.length:0;
  document.getElementById('filter-info').textContent=
    `${d.length} months · R$${(rev/1e6).toFixed(1)}M total · ${ord.toLocaleString()} orders`;
  document.getElementById('kpi-rev').textContent='R$'+(rev/1e6).toFixed(1)+'M';
  document.getElementById('kpi-ord').textContent=ord.toLocaleString();
  document.getElementById('kpi-aov').textContent='R$'+maov.toFixed(0);
  buildRevenue();
  buildAOV();
}

function showPage(id,el){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  el.classList.add('active');
  const titles={overview:'Executive Overview',segments:'Customer Segments — RFM Analysis',
    products:'Product Performance',location:'Geographic Analysis',aov:'Order Value Trends'};
  document.getElementById('page-title').textContent=titles[id];
  document.querySelector('.scroll').scrollTop=0;
  setTimeout(()=>{
    if(id==='overview'){buildRevenue();buildStatus();}
    if(id==='segments'){buildRFMRev();buildBubble();}
    if(id==='products'){buildCatCharts();}
    if(id==='location'){buildStateCharts();}
    if(id==='aov'){buildAOV();}
  },50);
}

function hlSeg(el){
  document.querySelectorAll('.seg-card').forEach(c=>{c.style.opacity='.4';c.style.transform='scale(.97)'});
  el.style.opacity='1';el.style.transform='scale(1.04)';
  setTimeout(()=>{document.querySelectorAll('.seg-card').forEach(c=>{c.style.opacity='1';c.style.transform=''})},2000);
}

window.addEventListener('load',()=>{buildRevenue();buildStatus();});
</script>
</body>
</html>"""

with open(r"d:\e commerce project\dashboard.html",'w',encoding='utf-8') as f:
    f.write(html)
print("Done! Open d:\\e commerce project\\dashboard.html in Chrome")
