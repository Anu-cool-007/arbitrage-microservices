import { useCallback, useEffect, useState } from "react";
// import { useSocketEvent } from "socket.io-react-hook";
// import { Message } from "./types";

import { io } from "socket.io-client";
import { Arbitrage, User } from "./types";
import LoginForm from "./components/loginForm";
import TradeCard from "./components/tradeCard";
import HistTradeCard from "./components/histTradeCard";

const ARBITRAGE_SERVICE_URL = "http://localhost:5001";

const socket = io(ARBITRAGE_SERVICE_URL);

const TRADE_URL = "http://localhost:5002/api/trade";

const App = () => {
  const [threshold, setThreshold] = useState("123");
  const [isConnected, setIsConnected] = useState(socket.connected);

  const [user, setUser] = useState<User | null>(null);
  const [arbitrageList, setArbitrageList] = useState<Arbitrage[]>([]);
  const [tradeList, setTradeList] = useState<Arbitrage[]>([]);

  useEffect(() => {
    function onConnect() {
      setIsConnected(true);
    }

    function onDisconnect() {
      setIsConnected(false);
    }

    function onArbitrageEvent(data: string) {
      const arbitrageList = JSON.parse(data);
      setArbitrageList(arbitrageList);
    }

    socket.on("connect", onConnect);
    socket.on("disconnect", onDisconnect);
    socket.on("arbitrage", onArbitrageEvent);

    return () => {
      socket.off("connect", onConnect);
      socket.off("disconnect", onDisconnect);
      socket.off("arbitrage", onArbitrageEvent);
    };
  }, []);

  useEffect(() => {
    if (threshold) {
      socket.emit("threshold", threshold);
    }
  }, [threshold]);

  const sendThreshold = () => {
    socket.emit("threshold", threshold);
  };

  const handleLogin = (user: User) => {
    setUser(user);
  };

  const handleTrade = useCallback(
    (arbitrage: Arbitrage) => {
      if (user) {
        fetch(TRADE_URL + "/create", {
          method: "POST",
          body: JSON.stringify(arbitrage),
          headers: {
            "Content-type": "application/json; charset=UTF-8",
            Authorization: user.token,
          },
        })
          .then((response) => response.json())
          .then(
            (data) =>
              data.result &&
              setTradeList((prev) => [...prev, data.result as Arbitrage])
          )
          .catch((err) => console.error(err));
      }
    },
    [user]
  );

  const fetchTrade = useCallback(() => {
    if (user) {
      fetch(TRADE_URL, {
        method: "GET",
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          Authorization: user.token,
        },
      })
        .then((response) => response.json())
        .then((data) => data.result && setTradeList(data.result as Arbitrage[]))
        .catch((err) => console.error(err));
    }
  }, [user]);

  if (!user) return <LoginForm onLogin={handleLogin} />;

  return (
    <div className="w-full">
      <div className="flex gap-4 flex-col items-start pt-16 max-w-6xl m-auto">
        <span>
          Connection Status: {isConnected ? "Connected" : "Not Connected"}
        </span>

        <div className="flex gap-4">
          <div className="flex gap-4 items-center">
            <span>Threshold: </span>
            <input
              className="max-w-lg border-2"
              type="number"
              value={threshold}
              onChange={(e) => setThreshold(e.target.value)}
            />
            <button
              className="bg-blue-600 rounded-md text-white p-2 px-4"
              onClick={sendThreshold}
            >
              Set Threshold
            </button>
          </div>
        </div>
        <span>Available Trades</span>
        <div className="p-2 px-4 flex items-center justify-between w-full">
          <span>Symbol</span>
          <span>Currency</span>
          <span>Buy Exchange</span>
          <span>Buy Price</span>
          <span>Sell Exchange</span>
          <span>Sell Price</span>
          <span>Units</span>
          <span>Profit</span>
          <span>Trade</span>
        </div>
        <div className="flex flex-col gap-4 w-full max-h-80 overflow-auto">
          {arbitrageList.map((arbitrage, idx) => (
            <TradeCard key={idx} arbitrage={arbitrage} onTrade={handleTrade} />
          ))}
        </div>
        <div className="flex justify-between items-center w-full">
          <span>Historical Trades</span>
          <button
            className="bg-blue-600 rounded-md text-white p-2 px-4"
            onClick={() => fetchTrade()}
          >
            Refresh Historical Trades
          </button>
        </div>
        <div className="p-2 px-4 flex items-center justify-between w-full">
          <span>Symbol</span>
          <span>Currency</span>
          <span>Buy Exchange</span>
          <span>Buy Price</span>
          <span>Sell Exchange</span>
          <span>Sell Price</span>
          <span>Units</span>
          <span>Profit</span>
        </div>
        <div className="flex flex-col gap-4 w-full max-h-80 overflow-auto">
          {tradeList.map((arbitrage, idx) => (
            <HistTradeCard key={idx} arbitrage={arbitrage} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
