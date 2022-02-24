import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Home from './home';
import Articles from "./articles"
import Contact from "./contact"

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="contact" element={<Contact />} />
        <Route path="articles" element={<Articles />} />
      </Routes>
    </BrowserRouter>
  )
}
