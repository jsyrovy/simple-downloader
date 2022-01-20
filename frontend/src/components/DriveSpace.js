import {Component} from "react";

class DriveSpace extends Component {
    state = {
        data: {
            path: "",
            total: "",
            used: "",
            free: "",
            free_perc: "",
        }
    }

    componentDidMount() {
        fetch('http://127.0.0.1:5000/drive-space')
            .then(res => res.json())
            .then((data) => {
                this.setState({data: data})
            })
    }

    render() {
        return <>
            Drive space at "{this.state.data.path}"
            | Total: {this.state.data.total}
            | Used: {this.state.data.used}
            | Free: {this.state.data.free} ({this.state.data.free_perc})
        </>
    }
}

export default DriveSpace;
