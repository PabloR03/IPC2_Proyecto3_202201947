$(document).ready(function() {
    $("#cargar_archivo_mensaje").click(function(e) {
        e.preventDefault();
        var form = new FormData();
        form.append('data', $("#inputData").val());
        form.append('file', $("#file-input-mensaje")[0].files[0]);
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        form.append('csrfmiddlewaretoken', csrfToken);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/cargar/Mensajes",
            data: form,
            processData: false,
            contentType: false,
            success: function(response) {
                alert(response.message);
                
            },
            error: function(xhr, status, error) {
                alert(error);
            }
        });
    });

    $("#consultar_hashtag").click(function() {
        $.get("/MyApp/consulta/Hashtags/", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });    

    $("#consultar_menciones").click(function() {
        $.get("/MyApp/consulta/Menciones", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#consultar_sentimiento").click(function() {
        $.get("/MyApp/consulta/Sentimientos", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#grafica_hashtag").click(function() {
        $.get("/MyApp/grafica/Hashtags", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });    

    $("#grafica_menciones").click(function() {
        $.get("/MyApp/grafica/Menciones", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#grafica_sentimiento").click(function() {
        $.get("/MyApp/grafica/Sentimientos", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#Info_estudiate").click(function() {
        $.get("/MyApp/informacion/estudiante", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

});

$(document).ready(function() {
    $("#cargar_archivo_config").click(function(e) {
        e.preventDefault();
        var form = new FormData();
        form.append('data', $("#inputData").val());
        form.append('file', $("#file-input-config")[0].files[0]);
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        form.append('csrfmiddlewaretoken', csrfToken);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/cargar/Configuracion",
            data: form,
            processData: false,
            contentType: false,
            success: function(response) {
                alert(response.message);
                
            },
            error: function(xhr, status, error) {
                alert(error);
            }
        });
    });
});


$(document).ready(function() {
    $("#Inicializar").click(function(e) {
        e.preventDefault();
        var form = new FormData();
        form.append('data', $("#inputData").val());
        form.append('file', $("#file-input-config")[0].files[0]);
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        form.append('csrfmiddlewaretoken', csrfToken);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/limpiarSistema",
            data: form,
            processData: false,
            contentType: false,
            success: function(response) {
                alert(response.message);
                
            },
            error: function(xhr, status, error) {
                alert(error);
            }
        });
    });
});

