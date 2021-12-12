import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import NavbarComp from "./components/NavbarComp";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Formbuilder from "./components/Formbuilder";
import Milestones from "./components/Milestones";
import Overview from "./components/Overview";
import Proposalsummary from "./components/Proposalsummary";
import Reporting from "./components/Reporting";

function App() {
  return (
    <div className="App">
      <Router>
        <NavbarComp />
        <Routes>
          <Route path="/overview" element={<Overview />} />

          <Route path="/formbuilder" element={<Formbuilder />} />

          <Route path="/milestones" element={<Milestones />} />

          <Route path="/reporting" element={<Reporting />} />

          <Route path="/" element={<Proposalsummary />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
