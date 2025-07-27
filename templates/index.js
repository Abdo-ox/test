
  const socket = new WebSocket("wss://limset.um6p.ma/ws/notifications/");

  socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    alert(data.title + ": " + data.body);
  };

  socket.onopen = function(e) {
    console.log("WebSocket connection opened.");
  };

  socket.onclose = function(e) {
    console.log("WebSocket connection closed.");
  };