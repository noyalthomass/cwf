import React, { Component } from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import "./NavbarComp.css";

export default class NavbarComp extends Component {
  render() {
    return (
      <div>
        <div className="topdiv">
          <h1 className="head">THE GOOD PLATFORM</h1>
        </div>
        <div>
          <Navbar className="navbar">
            <Container>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="items">
                  <Nav.Link as={Link} to={"/overview"}>
                    OVER VIEW
                  </Nav.Link>
                  <Nav.Link as={Link} to={"/formbuilder"}>
                    FORM BUILDER
                  </Nav.Link>
                  <Nav.Link as={Link} to={"/milestones"}>
                    MILESTONES
                  </Nav.Link>
                  <Nav.Link as={Link} to={"/reporting"}>
                    REPORTING
                  </Nav.Link>
                  <Nav.Link as={Link} to={"/"}>
                    PROPOSAL SUMMARY
                  </Nav.Link>
                </Nav>
              </Navbar.Collapse>
            </Container>
          </Navbar>
        </div>
      </div>
    );
  }
}
