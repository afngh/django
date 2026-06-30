import React, { useState } from 'react';
import * as AxiosModule from 'axios';
import { useNavigate } from 'react-router-dom'

const axios = AxiosModule.create()

function Login(){
    const navigate = useNavigate();

    const [username, SetUserName] = useState('')
    const [password, SetPassWord] = useState('')
    const [message, SetMessage] = useState('')

    async function HandleForm(e){
        e.preventDefault();

        const djangoRegisterRoute = `users/login/`
        const registerUrl = `${process.env.REACT_APP_API_URL}${djangoRegisterRoute}`

        const payload = {
            username: username,
            password: password
        }
        
        try{
            const response = await axios.post(registerUrl, payload)
            console.log(username," ",password)
            console.log(response.data)
            console.log(response.data.status)
            if (response.data.success){
                SetMessage(response.data.message)
                setTimeout(() => {
                    localStorage.setItem('username',response.data.username)
                    navigate('../dashboard/')
                }, 3);
            }else{
                SetMessage(response.data.message)
            }
        }catch(e){
            console.log(`error: ${e}`)
        }
    }
    return (
        <React.Fragment>
            <span id='error-block'>{message}</span>
            <form id='register-form' onSubmitCapture={HandleForm}>
                <input 
                    type="text" 
                    id="UserName"
                    onChange={(e) => SetUserName(e.target.value)}
                /><br />
                <input
                    type="password"
                    id="PassWord"
                    onChange={(e) => SetPassWord(e.target.value)}
                /><br />
                <button type="submit">register</button>
            </form>
        </React.Fragment>
    )
}

export default Login;