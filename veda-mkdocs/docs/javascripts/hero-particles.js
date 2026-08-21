/**
 * Homepage hero particle network — see HERO-BANNER-IMPLEMENTATION.md
 * Tune animation via the CONFIG object below.
 */
(function () {
  "use strict";

  var CONFIG = {
    particleCount: 28,
    minRadius: 1.2,
    maxRadius: 3.2,
    minOpacity: 0.35,
    maxOpacity: 0.88,
    speedMin: 0.08,
    speedMax: 0.22,
    connectDistance: 82,
    lineOpacityMax: 0.22,
    lineWidth: 0.5,
    glowBlur: 3,
    driftBiasX: 0.018,
    hoverLineRadius: 52,
    hoverLineOpacityBoost: 0.55,
    hoverLineWidth: 1.4,
    hoverNodeRadius: 70,
    hoverNodeOpacityBoost: 0.25
  };

  function prefersReducedMotion() {
    return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  function rand(min, max) {
    return min + Math.random() * (max - min);
  }

  function distToSegment(px, py, x1, y1, x2, y2) {
    var dx = x2 - x1;
    var dy = y2 - y1;
    var lenSq = dx * dx + dy * dy;
    var t;

    if (lenSq === 0) {
      return Math.hypot(px - x1, py - y1);
    }

    t = Math.max(0, Math.min(1, ((px - x1) * dx + (py - y1) * dy) / lenSq));
    return Math.hypot(px - (x1 + t * dx), py - (y1 + t * dy));
  }

  function initBanner(banner) {
    if (banner.getAttribute("data-veda-hero-init") === "true") {
      return;
    }

    var canvas = banner.querySelector(".veda-hero-banner__canvas");
    if (!canvas) {
      return;
    }

    banner.setAttribute("data-veda-hero-init", "true");

    var ctx = canvas.getContext("2d");
    var particles = [];
    var width = 0;
    var height = 0;
    var dpr = 1;
    var rafId = null;
    var reduced = prefersReducedMotion();
    var mouse = { x: -9999, y: -9999, active: false };

    function setMouseFromEvent(event) {
      var rect = banner.getBoundingClientRect();
      mouse.x = event.clientX - rect.left;
      mouse.y = event.clientY - rect.top;
      mouse.active = true;
    }

    function clearMouse() {
      mouse.active = false;
      mouse.x = -9999;
      mouse.y = -9999;
    }

    function requestDraw() {
      if (reduced) {
        draw();
      }
    }

    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = banner.clientWidth;
      height = banner.clientHeight;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      canvas.style.width = width + "px";
      canvas.style.height = height + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function createParticles() {
      particles = [];
      for (var i = 0; i < CONFIG.particleCount; i++) {
        var angle = rand(0, Math.PI * 2);
        var speed = rand(CONFIG.speedMin, CONFIG.speedMax);
        particles.push({
          x: rand(0, width),
          y: rand(0, height),
          vx: Math.cos(angle) * speed + CONFIG.driftBiasX,
          vy: Math.sin(angle) * speed,
          r: rand(CONFIG.minRadius, CONFIG.maxRadius),
          opacity: rand(CONFIG.minOpacity, CONFIG.maxOpacity)
        });
      }
    }

    function wrap(particle) {
      if (particle.x < -particle.r) {
        particle.x = width + particle.r;
      }
      if (particle.x > width + particle.r) {
        particle.x = -particle.r;
      }
      if (particle.y < -particle.r) {
        particle.y = height + particle.r;
      }
      if (particle.y > height + particle.r) {
        particle.y = -particle.r;
      }
    }

    function draw() {
      ctx.clearRect(0, 0, width, height);

      var i;
      var j;
      var p;
      var q;
      var dx;
      var dy;
      var dist;
      var alpha;
      var lineWidth;
      var segmentDist;
      var hoverStrength;
      var nodeAlpha;
      var nodeDist;

      for (i = 0; i < particles.length; i++) {
        p = particles[i];
        for (j = i + 1; j < particles.length; j++) {
          q = particles[j];
          dx = p.x - q.x;
          dy = p.y - q.y;
          dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < CONFIG.connectDistance) {
            alpha = (1 - dist / CONFIG.connectDistance) * CONFIG.lineOpacityMax;
            lineWidth = CONFIG.lineWidth;

            if (mouse.active) {
              segmentDist = distToSegment(mouse.x, mouse.y, p.x, p.y, q.x, q.y);
              if (segmentDist < CONFIG.hoverLineRadius) {
                hoverStrength = 1 - segmentDist / CONFIG.hoverLineRadius;
                alpha = Math.min(
                  1,
                  alpha + hoverStrength * CONFIG.hoverLineOpacityBoost
                );
                lineWidth = CONFIG.lineWidth + hoverStrength * CONFIG.hoverLineWidth;
              }
            }

            ctx.beginPath();
            ctx.strokeStyle = "rgba(255, 255, 255, " + alpha + ")";
            ctx.lineWidth = lineWidth;
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(q.x, q.y);
            ctx.stroke();
          }
        }
      }

      for (i = 0; i < particles.length; i++) {
        p = particles[i];
        nodeAlpha = p.opacity;

        if (mouse.active) {
          nodeDist = Math.hypot(mouse.x - p.x, mouse.y - p.y);
          if (nodeDist < CONFIG.hoverNodeRadius) {
            hoverStrength = 1 - nodeDist / CONFIG.hoverNodeRadius;
            nodeAlpha = Math.min(
              1,
              nodeAlpha + hoverStrength * CONFIG.hoverNodeOpacityBoost
            );
          }
        }

        ctx.beginPath();
        if (CONFIG.glowBlur > 0) {
          ctx.shadowBlur = CONFIG.glowBlur;
          ctx.shadowColor = "rgba(255, 255, 255, " + (nodeAlpha * 0.45) + ")";
        }
        ctx.fillStyle = "rgba(255, 255, 255, " + nodeAlpha + ")";
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
      }
    }

    function update() {
      for (var i = 0; i < particles.length; i++) {
        var particle = particles[i];
        particle.x += particle.vx;
        particle.y += particle.vy;
        wrap(particle);
      }
    }

    function loop() {
      update();
      draw();
      rafId = window.requestAnimationFrame(loop);
    }

    function stopLoop() {
      if (rafId) {
        window.cancelAnimationFrame(rafId);
        rafId = null;
      }
    }

    function startLoop() {
      if (!reduced && !document.hidden && !rafId) {
        rafId = window.requestAnimationFrame(loop);
      }
    }

    resize();
    createParticles();
    draw();
    startLoop();

    var resizeObserver = new ResizeObserver(function () {
      resize();
      createParticles();
      draw();
      startLoop();
    });
    resizeObserver.observe(banner);

    banner.addEventListener("mousemove", function (event) {
      setMouseFromEvent(event);
      requestDraw();
    });

    banner.addEventListener("mouseleave", function () {
      clearMouse();
      requestDraw();
    });

    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        stopLoop();
      } else {
        startLoop();
      }
    });

    var motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    var onMotionChange = function (event) {
      reduced = event.matches;
      if (reduced) {
        stopLoop();
        draw();
      } else {
        startLoop();
      }
    };

    if (motionQuery.addEventListener) {
      motionQuery.addEventListener("change", onMotionChange);
    } else if (motionQuery.addListener) {
      motionQuery.addListener(onMotionChange);
    }
  }

  function initAll() {
    var banners = document.querySelectorAll(".veda-hero-banner");
    for (var i = 0; i < banners.length; i++) {
      initBanner(banners[i]);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(function () {
      initAll();
    });
  }
})();
