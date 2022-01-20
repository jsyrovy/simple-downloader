import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Header from "./components/Header";
import Table from "./components/Table";
import Form2 from "./components/Form";
import {Col, Container, Row} from "react-bootstrap";
import DriveSpace from "./components/DriveSpace";

function App() {
    return (<>
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
                        <DriveSpace/>
                    </Col>

                </Row>
            </Container>
        </>);
}

export default App;
