import { Arbitrage } from "../types";

type HistTradeCardProps = {
  arbitrage: Arbitrage;
};

const HistTradeCard = ({ arbitrage }: HistTradeCardProps) => {
  return (
    <div className="border rounded-xl p-2 px-4 flex gap-4 items-center justify-between">
      <span>{arbitrage.symbol}</span>
      <span>{arbitrage.currency}</span>
      <span>{arbitrage.buy_exchange}</span>
      <span>{arbitrage.buy_price}</span>
      <span>{arbitrage.sell_exchange}</span>
      <span>{arbitrage.sell_price}</span>
      <span>{arbitrage.units}</span>
      <span>
        {Math.round(
          (arbitrage.sell_price - arbitrage.buy_price) * arbitrage.units
        )}
      </span>
    </div>
  );
};

export default HistTradeCard;
