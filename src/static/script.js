$(document).ready(function() {
    $('#upload-form').submit(function(event) {
        event.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.error) {
                    alert(response.error);
                } else {
                    var columns = response.columns;
                    $('#column1').empty();
                    $('#column2').empty();
                    $('#column3').empty();
                    columns.forEach(function(column) {
                        $('#column1').append(new Option(column, column));
                        $('#column2').append(new Option(column, column));
                        $('#column3').append(new Option(column, column));
                    });
                    $('#column-selection').show();
                }
            }
        });
    });

    $('#graph-type').change(function() {
        var graphType = $(this).val();
        if (graphType.includes('3d')) {
            $('#column3-group').show();
        } else {
            $('#column3-group').hide();
        }
    });

    $('#plot-button').click(function() {
        var selectedColumns = {
            column1: $('#column1').val(),
            column2: $('#column2').val(),
            column3: $('#column3').val(),
            graph_type: $('#graph-type').val()
        };
        $.ajax({
            url: '/plot_graph',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(selectedColumns),
            success: function(response) {
                if (response.error) {
                    alert(response.error);
                } else {
                    var graph_json = JSON.parse(response.graph_json);
                    var plotContainer = $('<div class="plot-summary-container"></div>');
                    var graphDiv = $('<div class="graph-div"></div>').css('height', '600px'); // Adjust the height as needed
                    var summaryDiv = $('<div class="summary-div"></div>').html('<p>' + formatText(response.desc) + '</p>');
                    
                    plotContainer.append(graphDiv);
                    plotContainer.append(summaryDiv);
                    $('#plots-container').append(plotContainer);

                    Plotly.newPlot(graphDiv[0], graph_json.data, graph_json.layout);
                    $('#plot-section').show();
                }
            }
        });
    });
    $('#email-button').on('click', function() {
        // Create a new jsPDF instance
        const doc = new jsPDF();

        // Add the entire HTML content of the page to the PDF
        const htmlContent = document.documentElement.innerHTML;
        doc.html(htmlContent, {
            callback: function(doc) {
                // Save the PDF file
                doc.save('page_content.pdf');
            },
            x: 10,
            y: 10
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const section = document.getElementById('column-selection');
    const header = section.querySelector('h2');
    const form = section.querySelector('#select-columns-form');

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > header.offsetHeight) {
            header.innerText = "Scroll up to continue plotting"
            form.classList.add('hidden');
        } else {
            header.innerText = "Select Columns and Graph Type"
            form.classList.remove('hidden');
        }
    });
});


function formatText(text) {
    // Convert double asterisks to bold tags
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Convert list items starting with * to <ul> list items
    text = text.replace(/\n\s*\*\s(.*?)\n/g, '\n<ul><li>$1</li>\n</ul>');
    
    // Convert remaining single asterisks to list items within lists
    text = text.replace(/\*\s(.*?)\n/g, '<li>$1</li>\n');
    
    // Convert **X-axis:** and **Y-axis:** to strong and add line breaks
    text = text.replace(/(\*\*X-axis:\*\*|\*\*Y-axis:\*\*)/g, '<strong>$1</strong><br>');
    
    // Convert **Trends:** to strong and add line breaks
    text = text.replace(/\*\*Trends:\*\*/g, '<strong>Trends:</strong><br>');
    
    // Ensure proper list formatting
    text = text.replace(/<\/ul>\s*<ul>/g, '');
    
    return text;
}