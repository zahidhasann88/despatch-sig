document.write(
    `
<div style="margin-top: 5%; position: relative; padding: 5% 2%; text-align: center;">
    <div class="container" style="min-height:100%; width:80%">
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                    <div class="alert alert-warning alert-dismissible" role="alert">
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close" onclick=delete_flash(this)>
                        <i class="fa fa-window-close"></i>
                        </button>
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        {% block body %}{% endblock %}
    <script>
    function delete_flash(flash){
        $(flash).parent().remove()
    }
    </script>

    </div>    

    `
);