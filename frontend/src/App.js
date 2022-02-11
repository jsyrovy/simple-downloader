import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Header from "./components/Header";
import Table from "./components/Table";
import DownloadForm from "./components/DownloadForm";
import DriveSpace from "./components/DriveSpace";
import {Col, Container, Row} from "react-bootstrap";

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
                    <Col xs={5}><DownloadForm/></Col>
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
