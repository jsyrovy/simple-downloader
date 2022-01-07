import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Header from "./components/Header";
import Table from "./components/Table";
import Footer from "./components/Footer";
import {Col, Container, Row} from "react-bootstrap";
import Form2 from "./components/Form";

function App() {
    return (
        <>
            <Container>
                <Row className="my-5 text-center">
                    <Col>
                        <Header/>
                    </Col>
                </Row>
                <Row className="my-5 text-center">
                    <Col/>
                    <Col xs={5}><Form2/></Col>
                    <Col/>
                </Row>
                <Row className="my-5 text-center">
                    <Col>
                        <Table/>
                    </Col>
                </Row>
                <Row className="my-5 text-center">
                    <Col>
                        <Footer path="path" total="666G" used="66G" free="600G" freePerc="90%"/>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default App;
