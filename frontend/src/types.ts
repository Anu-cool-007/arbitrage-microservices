export type Message = {
  result: string;
};

export type User = {
  id: string;
  name: string;
  username: string;
  token: string;
};

export type AuthPayload = {
  username: string;
  password: string;
};

export type Arbitrage = {
  symbol: string;
  currency: string;
  buy_exchange: string;
  sell_exchange: string;
  buy_price: number;
  sell_price: number;
  units: number;
};
