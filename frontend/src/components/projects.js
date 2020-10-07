import React from "react"
import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'

const Projects = () => {
    return(
        <center>
        <Card id="projects" style={{ align: 'center', width: '18rem' }}>
		<Card.Body>
			<Card.Title>Project Title</Card.Title>
			<Card.Text>
			Some quick example text to build on the card title and make up the bulk of
			the card's content.
			</Card.Text>
			<Button variant="primary">Open</Button>
		</Card.Body>
		</Card>
        </center>

    );
}

export default Projects