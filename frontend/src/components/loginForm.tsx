import { useState } from "react";
import { User } from "../types";

const AUTH_URL = "http://localhost:5003/api/user";

type LoginFormProps = {
  onLogin: (user: User) => void;
};

const LoginForm = ({ onLogin }: LoginFormProps) => {
  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [loginUsername, setLoginUsername] = useState("");
  const [loginPass, setLoginPass] = useState("");

  const handleApi = (subroute: string, payload: string) => {
    fetch(AUTH_URL + subroute, {
      method: "POST",
      body: payload,
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    })
      .then((response) => response.json())
      .then((data) => data.result && onLogin(data.result as User))
      .catch((err) => console.error(err));
  };

  const handleLogin = () => {
    handleApi(
      "/login",
      JSON.stringify({ username: loginUsername, password: loginPass })
    );
  };

  const handleSignin = () => {
    handleApi(
      "/create",
      JSON.stringify({
        name: name,
        username: username,
        password: password,
      })
    );
  };

  return (
    <div className="flex w-full max-w-6xl m-auto pt-16">
      {/* Signin form */}
      <div className="flex flex-col w-full p-6 gap-4">
        <h3 className="text-center text-lg">SIGN IN</h3>
        <input
          className="border-2 rounded-md px-4 py-2"
          placeholder="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          className="border-2 rounded-md px-4 py-2"
          placeholder="username"
          type="text"
          px-2
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className="border-2 rounded-md px-4 py-2"
          placeholder="password"
          type="text"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          className="p-2 px-4 rounded-md bg-blue-600 text-white"
          onClick={handleSignin}
        >
          Create Account
        </button>
      </div>
      {/* Login form */}
      <div className="flex flex-col w-full p-6 gap-4 border-l-2">
        <h3 className="text-center text-lg">LOG IN</h3>
        <input
          className="border-2 rounded-md px-4 py-2"
          placeholder="username"
          type="text"
          value={loginUsername}
          onChange={(e) => setLoginUsername(e.target.value)}
        />
        <input
          className="border-2 rounded-md px-4 py-2"
          placeholder="password"
          type="text"
          value={loginPass}
          onChange={(e) => setLoginPass(e.target.value)}
        />
        <button
          className="p-2 px-4 rounded-md bg-blue-600 text-white"
          onClick={handleLogin}
        >
          Log In
        </button>
      </div>
    </div>
  );
};

export default LoginForm;
