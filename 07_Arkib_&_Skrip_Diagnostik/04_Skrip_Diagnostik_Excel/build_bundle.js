const fs = require('fs');
const path = require('path');

const srcDir = path.resolve(__dirname, '../05_Web_Application_Dashboard');
const targetFile = path.resolve(__dirname, '../03_Google_Apps_Script/WebDashboard.html');

const html = fs.readFileSync(path.join(srcDir, 'index.html'), 'utf8');
const css = fs.readFileSync(path.join(srcDir, 'css/style.css'), 'utf8');
const dataJs = fs.readFileSync(path.join(srcDir, 'js/data.js'), 'utf8');
const analyticsJs = fs.readFileSync(path.join(srcDir, 'js/analytics.js'), 'utf8');
const chartsJs = fs.readFileSync(path.join(srcDir, 'js/charts.js'), 'utf8');
const appJs = fs.readFileSync(path.join(srcDir, 'js/app.js'), 'utf8');

// Replace CSS using function replacer to avoid $ interpolation bugs
let bundle = html.replace('<link rel="stylesheet" href="css/style.css">', () => `<style>\n${css}\n</style>`);

// Build embedded scripts block
const scriptsBlock = `  <script>
${dataJs}
  </script>
  <script>
${analyticsJs}
  </script>
  <script>
${chartsJs}
  </script>
  <script>
${appJs}
  </script>`;

// Replace script references using function replacer
const regexScripts = /<script src="js\/data\.js"><\/script>[\s\S]*?<script src="js\/app\.js"><\/script>/;
if (regexScripts.test(bundle)) {
  bundle = bundle.replace(regexScripts, () => scriptsBlock);
} else {
  bundle = bundle.replace('</body>', () => `${scriptsBlock}\n</body>`);
}

fs.writeFileSync(targetFile, bundle, 'utf8');
console.log('✅ WebDashboard.html successfully bundled! Total Size:', fs.statSync(targetFile).size, 'bytes');
