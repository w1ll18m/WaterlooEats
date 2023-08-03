import { useState } from "react";

export const useLocalStorage = () => {
    const [value, setValue] = useState(null)

    function setItem(key, value) {
        localStorage.setItem(key, value)
        setValue(value)
    }

    function getItem(key) {
        value = localStorage.getItem(key)
        setValue(value)
        return value
    }

    function removeItem(key) {
        localStorage.removeItem(key)
        setValue(null)
    }

    return {value, setItem, getItem, removeItem }
}