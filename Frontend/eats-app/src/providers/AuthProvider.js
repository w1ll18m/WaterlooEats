import { useState, useEffect, createContext, useContext } from "react";
import { useLocalStorage } from "../hooks/useLocalStorage";

const AuthContext = createContext({
    user: null,
    isAuthenticated: false,
    login: () => {},
    logout: () => {}
})

export const AuthProvider = ({children}) => {
    const {getItem, setItem, removeItem} = useLocalStorage()
    const [user, setUser] = useState(null)
    const [isAuthenticated, setIsAuthenticated] = useState(false)

    useEffect(() => {
        let current_user = getItem("waterloo-user")
        if (current_user) { 
            setUser(JSON.parse(current_user))
            setIsAuthenticated(true)
        } else {
            setIsAuthenticated(false)
        }
    }, [])

    const login = (user) => {
        setItem("waterloo-user", JSON.stringify(user))
        setUser(user)
        setIsAuthenticated(true)
    }

    const logout = (user) => {
        removeItem("waterloo-user")
        setUser(null)
        setIsAuthenticated(false)
    }

    return(
        <AuthContext.Provider value={{user, isAuthenticated, login, logout}}>
            {children}
        </AuthContext.Provider>
    )   
}

export const useAuth = () => {
    return useContext(AuthContext)
}