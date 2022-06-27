import { CssBaseline } from "@mui/material";
import React from "react";
import { QueryProvider } from "./context";
import NavBar from "./NavBar";
import ResultsDisplay from "./Results";


function App() {
  return (
    <QueryProvider>
      <React.Fragment>
        <NavBar />
        <ResultsDisplay />
        <CssBaseline />
      </React.Fragment>
    </QueryProvider>
  );
}

export default App;
