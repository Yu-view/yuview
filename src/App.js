import { CssBaseline } from "@mui/material";
import React from "react";
import { QueryProvider } from "./context";
import NavBar from "./NavBar";
import Search from "./Search";


function App() {
  return (
    <QueryProvider>
      <React.Fragment>
        <NavBar />
        <Search />
        <CssBaseline />
      </React.Fragment>
    </QueryProvider>
  );
}

export default App;
