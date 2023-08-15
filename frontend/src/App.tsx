import { useEffect, useState } from "react";
// import { useSocketEvent } from "socket.io-react-hook";
// import { Message } from "./types";
import { io } from "socket.io-client";
const URL = "http://localhost:5001";

const socket = io(URL);

function App() {
  // const { lastMessage, sendMessage, error, status } = useSocketEvent(socket,
  //   "message"
  // );

  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<string[]>([]);
  const [isConnected, setIsConnected] = useState(socket.connected);

  useEffect(() => {
    function onConnect() {
      setIsConnected(true);
    }

    function onDisconnect() {
      setIsConnected(false);
    }

    function onMessageEvent(value: string) {
      console.log(value);
      setMessages((previous) => [...previous, value]);
    }

    socket.on("connect", onConnect);
    socket.on("disconnect", onDisconnect);
    socket.on("reverse", onMessageEvent);

    return () => {
      socket.off("connect", onConnect);
      socket.off("disconnect", onDisconnect);
      socket.off("reverse", onMessageEvent);
    };
  }, []);

  const sendMsg = () => {
    socket.emit("reverse", input);
  };

  return (
    <div className="flex gap-4 flex-col items-start">
      <span>
        Connection Status: {isConnected ? "Connected" : "Not Connected"}
      </span>
      <div className="flex gap-4">
        <input
          className="max-w-lg border-2"
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button
          className="bg-blue-600 rounded-md text-white p-2 px-4"
          onClick={sendMsg}
        >
          Send
        </button>
      </div>
      {messages.map((message) => (
        <p>{message}</p>
      ))}
    </div>
  );
}

export default App;
