import { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";

const useFetch = (url) => {
  const { getAccessTokenSilently } = useAuth0()
  const [data, setData] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true)

      try { 
        const token = await getAccessTokenSilently()
        const response = await fetch(url, {
          method: "GET",
          headers: {
            "Authorization": token
          }
        })

        if (!response.ok) {
          throw new Error("Failed to fetch data")
        }

        const data = await response.json()
        setData(data)
        console.log(token) // For Testing Purposes
      } catch (error) {
        setError(error)
      } finally {
        setIsLoading(false)
      }
    }

    fetchData()
  }, [url]);

  return { data, isLoading, error, setData }
}

export default useFetch;