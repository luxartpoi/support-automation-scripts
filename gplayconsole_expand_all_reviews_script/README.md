🔓 Google Play Console – Expand All Reviews Script
This script auto-expands all reviews in the Google Play Console, including:

✅ "Show original review" (for translated content)

✅ "See more" (to reveal full text)

✅ Hidden expandable sections (via aria-expanded="false")

Works great directly from the browser Developer Console.

⚙️ How to Use
Open Google Play Console – Reviews

Press F12 (or Ctrl+Shift+I) to open DevTools

Switch to the Console tab

Paste the script below

Hit Enter — done! 🙌

<pre> <code>```
(function expandAllReviews() {
    // Click buttons by visible text
    function clickButtonsByText(text) {
        const xpath = `//button[contains(., '${text}')]`;
        const buttons = document.evaluate(xpath, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
        for (let i = 0; i < buttons.snapshotLength; i++) {
            const btn = buttons.snapshotItem(i);
            if (btn) btn.click();
        }
    }

    // Expand all visible review sections
    clickButtonsByText('Show original review');
    clickButtonsByText('See more');

    // Expand all collapsed containers
    document.querySelectorAll('[aria-expanded="false"]').forEach(btn => {
        if (btn.offsetParent !== null) btn.click();
    });

    console.log('✅ All reviews expanded.');
})();
        
```</code> </pre>
