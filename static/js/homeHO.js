
$(document).ready(function() {

  /*  // setup - for draftTable
    $('#draftTable thead tr').clone(true).appendTo( '#draftTable thead' );
    $('#draftTable thead tr:eq(1) th').not(":eq(2)").each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table1.column().search() !== this.value ) {
                table1
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );


    var table1 = $('#draftTable').DataTable( {
        orderCellsTop: true,
        "scrollY": 200,
        "scrollX": true
    } );

     Setup - add a text input to each footer cell
    $('#ongoingTable thead tr').clone(true).appendTo( '#ongoingTable thead' );
    $('#ongoingTable thead tr:eq(1) th').not(":eq(3,4)").each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text"  placeholder="Search '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );


    var table = $('#ongoingTable').Table( {
        orderCellsTop: true,
        "scrollY": 200,
        "scrollX": true
    } );

*/

    // Setup - add a text input to each footer cell
    $('#sendingTable thead tr').clone(true).appendTo( '#sendingTable thead' );
    $('#sendingTable thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text"  placeholder="Search '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table3.column(i).search() !== this.value ) {
                table3
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );


    var table3 = $('#sendingTable').DataTable( {
        orderCellsTop: true,
        "scrollY": 200,
        "scrollX": true
    } );

    // Setup - add a text input to each footer cell
    $('#submittedTable thead tr').clone(true).appendTo( '#submittedTable thead' );
    $('#submittedTable thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text"  placeholder="Search '+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( table4.column(i).search() !== this.value ) {
                table4
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );


    var table4 = $('#submittedTable').DataTable( {
        orderCellsTop: true,
        "scrollY": 200,
        "scrollX": true
    } );



} );


