import React from 'react'

function Dashboard(){
    return (
    <React.Fragment>
        <h1>
            Hola {localStorage.getItem('username')}, Welcome!
        </h1>
        <a href="../getall/">GETUSERS</a>
    </React.Fragment>
    );
}

export default Dashboard;