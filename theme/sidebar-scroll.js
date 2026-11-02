/*
 * Preserve the mdBook sidebar scroll position across full page navigations.
 *
 * mdBook reloads the whole document on every chapter change. Its toc script
 * scrolls the active chapter into view each time, which feels like the sidebar
 * jumping back to the top. This small script stores the sidebar's scroll
 * position in sessionStorage and restores it after the sidebar is populated.
 */
(function () {
  "use strict";

  var KEY = "foss-mec-library:sidebar-scroll";
  var box = document.querySelector(".sidebar-scrollbox");
  if (!box) return;

  function read() {
    try {
      return window.sessionStorage.getItem(KEY);
    } catch (error) {
      return null;
    }
  }

  function write(value) {
    try {
      window.sessionStorage.setItem(KEY, String(value));
    } catch (error) {
      /* storage may be unavailable in private mode */
    }
  }

  var frame = null;
  box.addEventListener(
    "scroll",
    function () {
      if (frame !== null) return;
      frame = window.requestAnimationFrame(function () {
        frame = null;
        write(box.scrollTop);
      });
    },
    { passive: true }
  );

  function restore() {
    var saved = read();
    if (saved === null) return;
    var top = Number(saved);
    if (!Number.isFinite(top) || top < 0) return;
    if (!box.children.length) return;
    box.scrollTop = top;
  }

  // mdBook's active-chapter scrollIntoView can run after the sidebar content is
  // inserted. Restore on the next frames and once more after it settles.
  function restoreSoon() {
    window.requestAnimationFrame(function () {
      restore();
      window.setTimeout(restore, 80);
    });
  }

  if (box.children.length) {
    restoreSoon();
  } else {
    var observer = new MutationObserver(function () {
      if (box.children.length) {
        observer.disconnect();
        restoreSoon();
      }
    });
    observer.observe(box, { childList: true, subtree: true });
  }

  window.addEventListener("pageshow", restoreSoon);
  window.addEventListener("beforeunload", function () {
    write(box.scrollTop);
  });
})();
