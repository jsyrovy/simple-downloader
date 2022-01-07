function Footer(props) {
    return (
        <p>
            Drive space at "{props.path}" | Total: {props.total} | Used: {props.used} | Free: {props.free} ({props.freePerc})
        </p>
    );
}

export default Footer;
