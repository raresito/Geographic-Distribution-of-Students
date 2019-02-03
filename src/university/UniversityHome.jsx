import React, { Component } from 'react';
import api from "../requests/acces-point";
import {Container, Col, Row, InputGroup, InputGroupAddon, Input, Form, FormGroup} from "reactstrap";
import Label from "reactstrap/es/Label";

class UniversityHome extends Component {
    state = {
        suggestionsList: [],
        color: "black",
    };

    onInputAdded(e) {
        // console.log(e.target.value);
        if(e.target.value) {
            this.setState({color: "blue"});
            api.getSuggestedUniversity(e.target.value)
                .then(data =>
                {
                    this.setState({
                        color: "black",
                        suggestionsList: data});
                });
        }
    };

    render() {

        let datalist = <option key="0" value="No match :(" />;

        if(this.state.suggestionsList.length != 0){
            datalist =
                this.state.suggestionsList.map(x =>
                    <option key={x._id} value={x.denumire} />)
        }
        return (
            <Container>
                <Row>
                    <Col xs="6">
                        <Form>
                            <FormGroup>
                                <Label for="universityInput"> University </Label>
                                <InputGroup>
                                    {/*<Label for */}
                                    <InputGroupAddon addonType="prepend" className={this.state.color === "blue" ? "loader-container" : ""}>
                                        {this.state.color === "blue" ?
                                            <div className="spinner-border custom-spinner" role="status">
                                                <span className="sr-only">Loading...</span>
                                            </div> : "@" }
                                    </InputGroupAddon>
                                        <Input id="universityInput" placeholder="University" list="data" onKeyUp={(e) => this.onInputAdded(e)} />
                                        <datalist id="data">
                                            {datalist}
                                        </datalist>
                                </InputGroup>
                            </FormGroup>
                        </Form>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default UniversityHome;
