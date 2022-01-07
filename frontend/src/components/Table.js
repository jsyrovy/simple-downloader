function Table(props) {
    const FilterableTable = require('react-filterable-table');

    const fields = [
        {name: 'name', displayName: "Name", inputFilterable: true, sortable: true},
        {name: 'date', displayName: "Date", inputFilterable: true, sortable: true},
        {name: 'size', displayName: "Size", inputFilterable: true, sortable: true},
        {name: 'progress', displayName: "Progress", inputFilterable: true, sortable: true},
        {name: 'actions', displayName: "Actions", inputFilterable: true, sortable: true},
    ];

    return (
        <FilterableTable
            namespace="Downloads"
            initialSort="date"
            initialSortDir={false}
            data={props.data}
            fields={fields}
            noRecordsMessage="There are no downloads to display."
            noFilteredRecordsMessage="No downloads match your filters."
        />
    );
}

export default Table;
