import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button';

function DownloadForm() {
    return (
        <>
            <h3 className="my-2">Download file</h3>
            <Form>
                <Form.Control className="my-2 text-center" type="text" placeholder="Paste URL here" name="url" autoFocus/>
                <Button className="my-2" variant="primary" type="submit">
                    Download
                </Button>
            </Form>
        </>
    );
}

export default DownloadForm;
