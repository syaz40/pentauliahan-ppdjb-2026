// Mock basic DOM environment
const fs = require('fs');

// Read the HTML to extract element IDs
const html = fs.readFileSync('Index.html', 'utf-8');
const idMatches = html.matchAll(/id="([^"]+)"/g);
const ids = new Set();
for (const match of idMatches) {
  ids.add(match[1]);
}

const mockElements = {};
ids.forEach(id => {
  mockElements[id] = {
    id: id,
    style: {},
    classList: {
      add: () => {},
      remove: () => {},
      toggle: () => {},
      contains: () => false
    },
    addEventListener: (event, fn) => {
      // console.log(`Attached listener for ${event} on #${id}`);
    },
    innerText: '',
    innerHTML: '',
    value: '0',
    options: [{ value: '0.60' }, { value: '0.40' }, { value: '0.70' }, { value: '0.50' }],
    selectedIndex: 0,
    querySelectorAll: () => [],
    focus: () => {}
  };
});

global.window = {
  print: () => {},
  addEventListener: () => {}
};
global.document = {
  readyState: 'complete',
  body: {
    classList: {
      toggle: () => {},
      contains: () => false
    }
  },
  getElementById: (id) => mockElements[id] || null,
  querySelectorAll: (selector) => {
    if (selector === '.tab-button') {
      return [
        { getAttribute: () => 'tab-overview', classList: { toggle: () => {} }, addEventListener: () => {} },
        { getAttribute: () => 'tab-awards', classList: { toggle: () => {} }, addEventListener: () => {} }
      ];
    }
    if (selector === '.tab-pane') {
      return [
        { id: 'tab-overview', classList: { toggle: () => {} } },
        { id: 'tab-awards', classList: { toggle: () => {} } }
      ];
    }
    return [];
  },
  addEventListener: (event, fn) => {
    if (event === 'DOMContentLoaded') fn();
  }
};

global.fetch = () => Promise.resolve({ text: () => Promise.resolve('{}') });
global.google = undefined;

// Load script
try {
  require('./test_web_script.js');
  console.log('Testing App.init()...');
  global.window.App.init();
  console.log('✅ App.init() succeeded without throwing any error!');
} catch (err) {
  console.error('❌ Error caught during execution:', err);
}
