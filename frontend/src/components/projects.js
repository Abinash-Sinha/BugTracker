import React from "react"
import { render } from "react-dom"
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Form from 'react-bootstrap/Form'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Button from 'react-bootstrap/Button'
import FormControl from 'react-bootstrap/FormControl'
import Card from 'react-bootstrap/Card'

const Projects = () => {
    render(
        <Card id="projects" style={{ width: '18rem' }}>
		<Card.Img variant="top" src="holder.js/100px180" />
		<Card.Body>
			<Card.Title>Card Title</Card.Title>
			<Card.Text>
			Some quick example text to build on the card title and make up the bulk of
			the card's content.
			</Card.Text>
			<Button variant="primary">Go somewhere</Button>
		</Card.Body>
		</Card>

    );
}

export default Projects