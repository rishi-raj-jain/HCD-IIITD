const CACHE_NAME = 'static-cache';

const FILES_TO_CACHE = [
  '/static/offline.html',
];

self.addEventListener('install', (evt) => {
    evt.waitUntil(
      caches.open(CACHE_NAME).then((cache) => {
        return cache.addAll(FILES_TO_CACHE);
      })
    );
  
    self.skipWaiting();
});

self.addEventListener('activate', (evt) => {
    evt.waitUntil(
      caches.keys().then((keyList) => {
        return Promise.all(keyList.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        }));
      })
    );
    self.clients.claim();
});

self.addEventListener('fetch', (evt) => {
    if (evt.request.mode !== 'navigate') {
      return;
    }
    evt.respondWith(fetch(evt.request).catch(() => {
        return caches.open(CACHE_NAME).then((cache) => {
          return cache.match('offline.html');
        });
      })
    );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch(event.request).catch(function() {
      return caches.match(event.request);
    })
  );
});