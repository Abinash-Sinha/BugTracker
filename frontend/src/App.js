import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import FormControl from 'react-bootstrap/FormControl'
import { BrowserRouter, Route, Switch } from 'react-router-dom';

const Home = () => {
  	return (
		<Navbar bg="dark" expand="lg">
			<Navbar.Brand href="/" style={{color:"white"}}>Abinash's BugTracker</Navbar.Brand>
			<Navbar.Toggle aria-controls="basic-navbar-nav" />
			<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="mr-auto">
					<Nav.Link href="/" style={{color:"white"}}>Home</Nav.Link>
					<Nav.Link href="/projects" style={{color:"white"}}>Projects</Nav.Link>
					<Nav.Link href="/about"  style={{color:"white"}}>About</Nav.Link>
					<Nav.Link href="/help" style={{color:"white"}}>Help</Nav.Link>
				</Nav>
				<Form inline>
					<FormControl type="text" placeholder="Search" className="mr-sm-2" />
					<Button variant="outline-success">Search</Button>
				</Form>
			</Navbar.Collapse>
		</Navbar>
	  );
	 
}

export default Home;
