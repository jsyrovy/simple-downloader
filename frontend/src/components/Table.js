import {Component} from "react";

class Table extends Component {
    state = {
        downloads: []
    }

    componentDidMount() {
        fetch('http://127.0.0.1:5000/downloads')
            .then(res => res.json())
            .then((data) => {
                this.setState({downloads: data.downloads})
            })
    }

    render() {
        const FilterableTable = require('react-filterable-table');

        const fields = [
            {name: 'name', displayName: "Name", inputFilterable: true, sortable: true},
            {name: 'date', displayName: "Date", inputFilterable: true, sortable: true},
            {name: 'size', displayName: "Size", inputFilterable: true, sortable: true},
            {name: 'progress', displayName: "Progress", inputFilterable: true, sortable: true},
            {name: 'actions', displayName: "Actions", inputFilterable: true, sortable: true},
        ];

        return <>
            <FilterableTable
                namespace="Downloads"
                initialSort="date"
                initialSortDir={false}
                data={this.state.downloads}
                fields={fields}
                noRecordsMessage="There are no downloads to display."
                noFilteredRecordsMessage="No downloads match your filters."
            />
        </>
    }
}

export default Table;
