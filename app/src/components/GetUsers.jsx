import React, { useEffect, useRef, useState } from "react";
import * as AxiosModule from 'axios';

const axios = AxiosModule.create();
function Users(){

    const dataRef = useRef(null);

    const [responseData,setResponseData] = useState([]);
    const [status,setStatus] = useState(false);
    async function get_all(){

        const djangoRegisterRoute = `users/getall/`
        const getAllUsersUrl = `${process.env.REACT_APP_API_URL}${djangoRegisterRoute}`
        
        const token = localStorage.getItem('access')
        console.log(token)

        try{
            const response = await axios.get(getAllUsersUrl, {
            headers:{
                Authorization: `Bearer ${token}`
            }
        })

            // const response = await axios.get(getAllUsersUrl)
            if(response.data.success){
                setResponseData(response.data.data)
            }else{
                setStatus(response.data.success)
            }
        }catch(e){
            console.log(`Error:${e}`)
        }
    }

    return (
        <React.Fragment>
            <table ref={dataRef} border={1} cellPadding={8}>
                <thead>
                    <tr>
                    <th>id</th>
                    <th>username</th>
                </tr>
                </thead>
                <tbody>
                    {responseData.map((data) => (
                    <tr>
                        <td>{data.id}</td>
                        <td>{data.username}</td>
                    </tr>
                ))}
                </tbody>
            </table>
            <button onClick={get_all}>Users</button>
        </React.Fragment>
    )
}

export default Users;