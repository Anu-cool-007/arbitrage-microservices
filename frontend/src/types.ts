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
