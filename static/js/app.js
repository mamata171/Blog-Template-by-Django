

document.addEventListener("DOMContentLoaded",function(event){
    console.log("this is blog.js");
    
    let sc = document.createElement('script');
    sc.setAttribute('src','https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js');
    
    document.head.appendChild(sc);

    sc.onload = ()=>{
        tinymce.init({
            selector: '#id_content',
            plugins: [
              'a11ychecker','advlist','advcode','advtable','autolink','checklist','export',
              'lists','link','image','charmap','preview','anchor','searchreplace','visualblocks',
              'powerpaste','fullscreen','formatpainter','insertdatetime','media','table','help','wordcount'
            ],
            toolbar: 'undo redo | formatpainter casechange blocks | bold italic backcolor | ' +
              'alignleft aligncenter alignright alignjustify | ' +
              'bullist numlist checklist outdent indent | removeformat | a11ycheck code table help'

        });

    }
})
