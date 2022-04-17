var script = document.createElement('script')
script.type = 'text/javascript';
script.src="https://cdn.tiny.cloud/1/ol04vqfxf3vrx85m41m053mxs7ddtjflvf87rcway94f0k8y/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

tinymce.init({
    selector: 'textarea',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'a11ycheck addcomment showcomments casechange checklist code formatpainter pageembed permanentpen table',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
});
