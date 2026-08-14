import React, { useState } from 'react';

const Register = () => {
    const [userName, setUserName] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = async (e) => {
        e.preventDefault();
        const register_url = window.location.origin + "/djangoapp/register";
        const res = await fetch(register_url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ userName, firstName, lastName, email, password }),
        });
        const json = await res.json();
        if (json.status === "Authenticated") {
            window.location.href = window.location.origin;
        }
    };

    return (
        <div className="container mt-5">
            <h2>Sign-Up for Dealership Portal</h2>
            <form onSubmit={handleRegister}>
                <div className="form-group mb-3">
                    <label>Username</label>
                    <input type="text" className="form-control" value={userName} onChange={(e) => setUserName(e.target.value)} required />
                </div>
                <div className="form-group mb-3">
                    <label>First Name</label>
                    <input type="text" className="form-control" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                </div>
                <div className="form-group mb-3">
                    <label>Last Name</label>
                    <input type="text" className="form-control" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                </div>
                <div className="form-group mb-3">
                    <label>Email</label>
                    <input type="email" className="form-control" value={email} onChange={(e) => setEmail(e.target.value)} required />
                </div>
                <div className="form-group mb-3">
                    <label>Password</label>
                    <input type="password" className="form-control" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </div>
                <button type="submit" className="btn btn-primary">Register</button>
            </form>
        </div>
    );
};

export default Register;
