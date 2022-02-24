import {Link} from "react-router-dom";

import mountains from "./mountains.png";
import "./home.css";

export default function App() {
  return  (
    <div className="App">
      <header className="App-header">
        <img src={mountains} className="App-logo" alt="logo" />
        <p>
          Sabar Dasgupta
        </p>
      </header>
      <nav
        style={{
          borderBottom: "solid 1px",
          paddingBottom: "1rem"
        }}
      >
        <Link to="/articles">Articles</Link> |{" "}
        <Link to="/contact">Contact</Link>
      </nav>
    </div>
  )
}
