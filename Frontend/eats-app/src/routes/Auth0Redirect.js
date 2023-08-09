import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'
import { useNavigate } from "react-router-dom";

const Auth0RedirectHandler = () => {
    const redirect = useNavigate()
    const { isAuthenticated, getIdTokenClaims } = useAuth0()

    const handleAuth0Authentication = async () => {
        const idToken = await getIdTokenClaims()
        try {
            const myPath = process.env.REACT_APP_SERVER_BASE_URL + "auth/check-existing-user"
            let formData = new FormData()
            formData.append("uuid", idToken.sub)

            const res = await fetch(myPath, {method: "POST", body: formData})
            if (!res.ok) throw new Error(`Error with http request to ${myPath}`)
            const response = await res.json()
            
            if (response.valid_user) {
                redirect("/resteraunts")
            } else {
                redirect("/complete-sign-up")
            }
        } catch (error) {
            console.error("handleAuth0Authentication error:", error)
        }
    }

    if (isAuthenticated) handleAuth0Authentication()

    return null
}

export default Auth0RedirectHandler