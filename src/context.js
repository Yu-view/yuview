import React, { useState } from "react"
import FastAPIClient from "./client";
import { mockData } from "./mockData";

const QueryContext = React.createContext()
const client = new FastAPIClient();

function QueryProvider({children}) {
    const [query, setQuery] = useState({query: "", search: false});
    const [listings, setListings] = useState(mockData);

    const value = {query, setQuery, listings, setListings, client}
    return <QueryContext.Provider value={value}>{children}</QueryContext.Provider>
}

export {QueryProvider, QueryContext}