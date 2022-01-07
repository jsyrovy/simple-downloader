import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Header from "./components/Header";
import Table from "./components/Table";
import Footer from "./components/Footer";
import Form2 from "./components/Form";
import {Col, Container, Row} from "react-bootstrap";

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
                        <Table data={[
                            {
                                name: "ubuntu.iso",
                                date: "2022-01-01 10:00:00",
                                size: "2GB",
                                progress: "100 %",
                                actions: ""
                            },
                            {
                                name: "fedora.iso",
                                date: "2022-01-01 08:00:00",
                                size: "2GB",
                                progress: "100 %",
                                actions: ""
                            }
                        ]}/>
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
