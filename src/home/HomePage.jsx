import React, { Component } from 'react';
import '../sass/homepage.scss';
import govIcon from '../assets/icons8-city-hall-96.png';
import { Container } from 'reactstrap';
import Button from "reactstrap/es/Button";
import {Link} from "react-router-dom";

import api from '../requests/acces-point';

class HomePage extends Component {
    componentDidMount() {
        api.getUniversity(23)
            .then(data => this.setState({...data}));
    }


    render() {
        return (
            <Container style={{minHeight: '600px', position: 'relative'}}>
                <div className="text-center center-block" style={{width: '100%'}}>
                    <Button className="button" color="info">
                        <Link to='/gov'>
                            <span ><img className="button-icon" src={govIcon} alt="Government Icon"/></span>
                            <p className="button-text"> Acces pentru primării </p>
                        </Link>
                    </Button>
                    <Button color="info">
                        <Link to='/uni'>
                            <span ><img className="button-icon" src={govIcon} alt="Government Icon"/></span>
                            <p className="button-text"> Acces pentru universități </p>
                        </Link>
                    </Button>
                </div>
            </Container>
        )
    }
}

export default HomePage;
