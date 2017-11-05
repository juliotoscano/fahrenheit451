const mqtt = require("mqtt");
const client = mqtt.connect("mqtt://test.mosquitto.org:1883");

client.subscribe("smoke");

client.on("connect", () => {
  console.log("connected");
});

client.on("message", (topic, message) => {
  console.log("received message %s %s", topic, message);
});
