import React, { useState } from "react"

const QueryContext = React.createContext()

function QueryProvider({children}) {
    const [query, setQuery] = useState({query: "", search: false});

    const value = {query, setQuery}
    return <QueryContext.Provider value={value}>{children}</QueryContext.Provider>
}



export {QueryProvider, QueryContext}