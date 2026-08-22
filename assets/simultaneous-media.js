(() => {
  const nativeAudio = window.Audio;
  const ttsAudios = new Set();
  let manualPauseUntil = 0;

  window.Audio = function (...args) {
    const audio = new nativeAudio(...args);
    audio.addEventListener("play", () => {
      if (audio.currentSrc.includes("/content/i18n/") && audio.currentSrc.includes("/audio/")) {
        ttsAudios.add(audio);
      }
    });
    return audio;
  };
  window.Audio.prototype = nativeAudio.prototype;

  document.addEventListener("pointerdown", (event) => {
    if (event.target.closest("video")) manualPauseUntil = Date.now() + 600;
  }, true);

  const videoPlaying = () => Array.from(document.querySelectorAll("video")).some((video) => !video.paused);
  const ttsPlaying = () => Array.from(ttsAudios).some((audio) => !audio.paused && audio.currentSrc.includes("/audio/"));
  const protect = (media) => Date.now() > manualPauseUntil && ((media.tagName === "VIDEO" && ttsPlaying()) || (media.tagName === "AUDIO" && videoPlaying() && media.currentSrc.includes("/audio/")));
  const pause = HTMLMediaElement.prototype.pause;
  const removeAttribute = HTMLMediaElement.prototype.removeAttribute;
  const load = HTMLMediaElement.prototype.load;

  HTMLMediaElement.prototype.pause = function () {
    if (protect(this)) return;
    return pause.call(this);
  };
  HTMLMediaElement.prototype.removeAttribute = function (name) {
    if (name === "src" && protect(this)) return;
    return removeAttribute.call(this, name);
  };
  HTMLMediaElement.prototype.load = function () {
    if (protect(this)) return;
    return load.call(this);
  };
})();
