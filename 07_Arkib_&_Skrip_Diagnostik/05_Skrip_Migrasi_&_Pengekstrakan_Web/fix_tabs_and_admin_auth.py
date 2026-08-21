import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Fixing 5 Nav Tabs and Instant Admin PIN Authentication...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. FIX NAV BAR (Ensure exactly 5 tab buttons)
nav_pattern = r'<nav class=[\x22\x27]tab-nav-group[\x22\x27]>[\s\S]*?</nav>'
correct_nav = """<nav class="tab-nav-group">
        <button class="tab-btn active" data-tab="tab-program">
          <i class="fa-solid fa-circle-info"></i> Maklumat Program
        </button>
        <button class="tab-btn" data-tab="tab-analytics">
          <i class="fa-solid fa-chart-pie"></i> Analisis & Statistik
        </button>
        <button class="tab-btn" data-tab="tab-candidates">
          <i class="fa-solid fa-address-book"></i> Senarai Calon
        </button>
        <button class="tab-btn" data-tab="tab-top-results">
          <i class="fa-solid fa-trophy"></i> Keputusan Calon Terbaik
        </button>
        <button class="tab-btn" data-tab="tab-admin">
          <i class="fa-solid fa-sliders"></i> Tetapan Admin
        </button>
      </nav>"""

html = re.sub(nav_pattern, correct_nav, html)

# 2. CLEAN UP ANY DUPLICATE tab-top-results SECTIONS
# Find all occurrences of tab-top-results and ensure only one exists before tab-admin
html = re.sub(r'<section class="tab-content" id="tab-top-results">[\s\S]*?</section>\s*<section class="tab-content" id="tab-top-results">', '<section class="tab-content" id="tab-top-results">', html)

# 3. FIX ADMIN PIN AUTHENTICATION IN JS
old_admin_events = """      bindAdminEvents() {
        const formAuth = document.getElementById('form-admin-auth');
        formAuth?.addEventListener('submit', async (e) => {
          e.preventDefault();
          const pin = document.getElementById('input-admin-pin').value;
          const errAlert = document.getElementById('auth-error-alert');
          errAlert.style.display = 'none';

          try {
            const res = await runBackendAction('verifyAdminPIN', { pin: pin });
            if (res.success) {
              this.state.isAdminLoggedIn = true;
              sessionStorage.setItem('pentauliahan_admin_auth', 'true');
              this.updateAuthVisuals();
            } else {
              errAlert.innerText = res.message || 'PIN Admin tidak sah. Sila cuba lagi.';
              errAlert.style.display = 'block';
            }
          } catch (err) {
            // Fallback default PIN jika offline / preview
            if (pin === 'seketejb26') {
              this.state.isAdminLoggedIn = true;
              sessionStorage.setItem('pentauliahan_admin_auth', 'true');
              this.updateAuthVisuals();
            } else {
              errAlert.innerText = 'PIN Admin tidak sah: ' + err.message;
              errAlert.style.display = 'block';
            }
          }
        });"""

new_admin_events = """      bindAdminEvents() {
        const formAuth = document.getElementById('form-admin-auth');
        formAuth?.addEventListener('submit', async (e) => {
          e.preventDefault();
          const inputPin = document.getElementById('input-admin-pin');
          const pin = (inputPin?.value || '').trim();
          const errAlert = document.getElementById('auth-error-alert');
          if (errAlert) errAlert.style.display = 'none';

          // 1. SEMAKAN PIN SEGERA SISI KLIEN (INSTANT AUTHENTICATION)
          if (pin === 'seketejb26') {
            this.state.isAdminLoggedIn = true;
            sessionStorage.setItem('pentauliahan_admin_auth', 'true');
            this.updateAuthVisuals();
            if (inputPin) inputPin.value = '';
            return;
          }

          // 2. JIKA BUKAN PIN LALAI, CUBA SEMAK GOOGLE APPS SCRIPT BACKEND
          try {
            const res = await runBackendAction('verifyAdminPIN', { pin: pin });
            if (res && res.success) {
              this.state.isAdminLoggedIn = true;
              sessionStorage.setItem('pentauliahan_admin_auth', 'true');
              this.updateAuthVisuals();
              if (inputPin) inputPin.value = '';
              return;
            }
          } catch (err) {
            console.warn('Backend PIN check:', err);
          }

          // 3. JIKA SALAH PIN
          if (errAlert) {
            errAlert.innerText = '❌ PIN Admin tidak sah. Sila masukkan PIN yang tepat (seketejb26).';
            errAlert.style.display = 'block';
          }
        });"""

html = html.replace(old_admin_events, new_admin_events)

# 4. HOOK switchTab TO CALL renderTopResults WHEN ENTERING TAB 4
old_switch_tab = """      switchTab(tabId) {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(p => p.classList.remove('active'));
        
        const targetBtn = document.querySelector(`[data-tab="${tabId}"]`);
        const targetPane = document.getElementById(tabId);
        
        if (targetBtn) targetBtn.classList.add('active');
        if (targetPane) targetPane.classList.add('active');
        this.state.activeTab = tabId;
      },"""

new_switch_tab = """      switchTab(tabId) {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(p => p.classList.remove('active'));
        
        const targetBtn = document.querySelector(`[data-tab="${tabId}"]`);
        const targetPane = document.getElementById(tabId);
        
        if (targetBtn) targetBtn.classList.add('active');
        if (targetPane) targetPane.classList.add('active');
        this.state.activeTab = tabId;

        if (tabId === 'tab-top-results') {
          this.renderTopResults();
        } else if (tabId === 'tab-candidates') {
          this.renderCandidatesTable();
        } else if (tabId === 'tab-analytics') {
          this.updateCharts();
        }
      },"""

html = html.replace(old_switch_tab, new_switch_tab)

# Save Netlify index.html
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved 04_Web_App_Netlify/index.html ({len(html):,} bytes)")

# Prepare and save GAS Index.html
html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")
