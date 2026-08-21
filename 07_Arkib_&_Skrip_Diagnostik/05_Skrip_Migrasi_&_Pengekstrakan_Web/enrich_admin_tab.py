import re

index_path = r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add Admin Action Buttons inside tab-admin in Index.html
admin_tools_html = """
        <!-- =========================================================================
             PUSAT TINDAKAN & AUTOMASI URUS SETIA (PENGGANTIAN MODALS GOOGLE SHEET)
             ========================================================================= -->
        <div style="margin-top: 32px; border-top: 1.5px solid var(--card-border); padding-top: 24px;">
          <h3 style="font-size: 16px; font-weight: 800; color: var(--text-main); margin-bottom: 8px;">
            ⚡ Pusat Tindakan, Pembaikan & Automasi Urus Setia
          </h3>
          <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">
            Semua fungsi tetapan yang dahulunya berada dalam modal Google Sheet kini boleh digerakkan terus dari Web App ini:
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div style="background: var(--bg-main); border: 1px solid var(--card-border); border-radius: var(--radius-sm); padding: 16px;">
              <h4 style="font-size: 14px; font-weight: 800; color: var(--primary); margin-bottom: 6px;">⚡ Diagnosis & Baiki Formula</h4>
              <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">Betulkan formula VLOOKUP, format peratus, dan struktur helaian secara automatik.</p>
              <button class="btn-header" id="btn-admin-repair-formula" style="width: 100%; justify-content: center; background: var(--primary); color: white;">
                ⚡ Jalankan Pembaikan Formula
              </button>
            </div>

            <div style="background: var(--bg-main); border: 1px solid var(--card-border); border-radius: var(--radius-sm); padding: 16px;">
              <h4 style="font-size: 14px; font-weight: 800; color: #047857; margin-bottom: 6px;">🔄 Segerakkan Markah Penguji</h4>
              <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">Kira semula wajaran 60/20/20 dan kemas kini status kelulusan (LLL/GGG) dalam Google Sheet.</p>
              <button class="btn-header" id="btn-admin-sync-scores" style="width: 100%; justify-content: center; background: #10b981; color: white;">
                🔄 Segerakkan Markah Sheet
              </button>
            </div>

            <div style="background: var(--bg-main); border: 1px solid var(--card-border); border-radius: var(--radius-sm); padding: 16px;">
              <h4 style="font-size: 14px; font-weight: 800; color: #b45309; margin-bottom: 6px;">🤖 Pasang Trigger Automasi</h4>
              <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">Pasang jadual trigger auto-sync berkala 5 minit terus pada fail Google Sheet.</p>
              <button class="btn-header" id="btn-admin-setup-trigger" style="width: 100%; justify-content: center; background: #f59e0b; color: white;">
                🤖 Pasang Trigger Masa Nyata
              </button>
            </div>
          </div>

          <div id="admin-action-status-box" style="display:none; padding:14px; border-radius:var(--radius-sm); font-size:13px; font-weight:600; margin-bottom:16px;"></div>
        </div>
"""

# Insert admin_tools_html before the closing of tab-admin section
html = html.replace('</section>\n\n  </div>\n\n  <!-- =========================================================================\n       MODAL 1: SLIP KEPUTUSAN CALON', admin_tools_html + '\n    </section>\n\n  </div>\n\n  <!-- =========================================================================\n       MODAL 1: SLIP KEPUTUSAN CALON')

# Add JS handlers in App
admin_js_handlers = """
  triggerAdminRepair() {
    this.showAdminActionStatus('Sedang menjalankan diagnosis & pembaikan formula VLOOKUP...', 'info');
    if (typeof google !== 'undefined' && google.script && google.script.run) {
      google.script.run
        .withSuccessHandler(res => {
          this.showAdminActionStatus('✅ ' + (res.message || 'Formula VLOOKUP berjaya dibaiki!'), 'success');
          this.syncLiveGoogleSheet();
        })
        .withFailureHandler(err => {
          this.showAdminActionStatus('❌ Ralat: ' + err.message, 'error');
        })
        .repairAllFormulasAndFormat();
    } else {
      setTimeout(() => {
        this.showAdminActionStatus('✅ [Mod Simulasi] Diagnosis & formula disahkan 100% tepat.', 'success');
      }, 1000);
    }
  },

  triggerAdminSync() {
    this.showAdminActionStatus('Sedang menyegerakkan markah penguji & mengira status kelulusan...', 'info');
    if (typeof google !== 'undefined' && google.script && google.script.run) {
      google.script.run
        .withSuccessHandler(res => {
          this.showAdminActionStatus('✅ ' + (res.message || 'Markah penguji berjaya disegerakkan!'), 'success');
          this.syncLiveGoogleSheet();
        })
        .withFailureHandler(err => {
          this.showAdminActionStatus('❌ Ralat: ' + err.message, 'error');
        })
        .syncAllExaminerScores();
    } else {
      setTimeout(() => {
        this.showAdminActionStatus('✅ [Mod Simulasi] Markah penguji disegerakkan ke Google Sheet.', 'success');
      }, 1000);
    }
  },

  triggerAdminSetupTrigger() {
    this.showAdminActionStatus('Sedang memasang trigger auto-sync pada Google Sheet...', 'info');
    if (typeof google !== 'undefined' && google.script && google.script.run) {
      google.script.run
        .withSuccessHandler(res => {
          this.showAdminActionStatus('✅ ' + (res.message || 'Trigger auto-sync berjaya dipasang!'), 'success');
        })
        .withFailureHandler(err => {
          this.showAdminActionStatus('❌ Ralat: ' + err.message, 'error');
        })
        .setupAutoSyncTriggers();
    } else {
      setTimeout(() => {
        this.showAdminActionStatus('✅ [Mod Simulasi] Trigger auto-sync 5 minit aktif.', 'success');
      }, 1000);
    }
  },

  showAdminActionStatus(msg, type) {
    const box = document.getElementById('admin-action-status-box');
    if (!box) return;
    box.style.display = 'block';
    box.innerText = msg;
    if (type === 'success') {
      box.style.background = '#dcfce7';
      box.style.color = '#166534';
      box.style.border = '1px solid #86efac';
    } else if (type === 'error') {
      box.style.background = '#fee2e2';
      box.style.color = '#991b1b';
      box.style.border = '1px solid #fca5a5';
    } else {
      box.style.background = '#eff6ff';
      box.style.color = '#1e40af';
      box.style.border = '1px solid #bfdbfe';
    }
  },
"""

# Insert handlers before setupEventListeners in App
html = html.replace('  setupEventListeners() {', admin_js_handlers + '\n  setupEventListeners() {')

# Add button listeners in setupEventListeners
admin_event_listeners = """
    // Admin Action Buttons
    const btnRepair = document.getElementById('btn-admin-repair-formula');
    if (btnRepair) btnRepair.addEventListener('click', () => this.triggerAdminRepair());

    const btnSyncScores = document.getElementById('btn-admin-sync-scores');
    if (btnSyncScores) btnSyncScores.addEventListener('click', () => this.triggerAdminSync());

    const btnSetupTrig = document.getElementById('btn-admin-setup-trigger');
    if (btnSetupTrig) btnSetupTrig.addEventListener('click', () => this.triggerAdminSetupTrigger());
"""

html = html.replace('    const btnApplyAdmin = document.getElementById(\'btn-apply-admin-thresholds\');', admin_event_listeners + '\n    const btnApplyAdmin = document.getElementById(\'btn-apply-admin-thresholds\');')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated Index.html with integrated admin tools from modals!")
