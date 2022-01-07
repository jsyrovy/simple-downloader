function Table() {
    const FilterableTable = require('react-filterable-table');

    // Data for the table to display; can be anything
    const data = [
        {name: "ubuntu.iso", date: "2022-01-01 10:00:00", size: "2GB", progress: "100 %", actions: ""},
    ];

    // Fields to show in the table, and what object properties in the data they bind to
    const fields = [
        {name: 'name', displayName: "Name", inputFilterable: true, sortable: true},
        {name: 'date', displayName: "Date", inputFilterable: true, exactFilterable: true, sortable: true},
        {name: 'size', displayName: "Size", inputFilterable: true, exactFilterable: true, sortable: true},
        {name: 'progress', displayName: "Progress", inputFilterable: true, exactFilterable: true, sortable: true},
        {name: 'actions', displayName: "Actions", inputFilterable: true, exactFilterable: true, sortable: true},
    ];

    return (
        <FilterableTable
            namespace="Downloads"
            initialSort="date"
            data={data}
            fields={fields}
            noRecordsMessage="There are no downloads to display."
            noFilteredRecordsMessage="No downloads match your filters."
        />
    );
}

export default Table;
