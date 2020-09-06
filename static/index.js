let file;

function deleteAllFromEl (doc){
    let child = doc.lastElementChild;
    while (child) {
        doc.removeChild(child);
        child = doc.lastElementChild;
    }
}

function scrollToBottom(){
    window.scrollTo(0,document.body.scrollHeight);
}

function  handleUploadImage (e) {
    e.preventDefault();
    input_submit = document.getElementById('submit-input');
    input_submit.setAttribute('disabled', 'true');

    doc = document.getElementById('result-image');
    deleteAllFromEl(doc);
    doc.innerHTML += `<div class="loader"></div>`;
    scrollToBottom();
    const data = new FormData();
    data.append('file', file);
    data.append('filename', file.name);
    fetch('/upload', {
        method: 'POST',
        body: data,
    }).then((response) => {
        response.json().then((body) => {
            if(body.response == "OK"){
                const fa_icon = document.getElementById('fa-icon-id');
                fa_icon.classList.remove('fa-upload-sucessful')
                url_uploads = './static/uploads/' + body.filename;
                showImage(url_uploads, 0);
                url = './static/result/' + body.filename;
                showImage(url, 1);
                input_submit.removeAttribute('disabled');
                scrollToBottom();
            }
        });
    });
}

function changeFiles (e) {
   file = e.target.files[0];
   const fa_icon = document.getElementById('fa-icon-id');
   fa_icon.classList.add('fa-upload-sucessful')
}

function showImage(url, index){
    console.log('SHOW IMAGE', url)
    element = document.getElementById('result-image')
    if(!index) deleteAllFromEl(element)
    element.innerHTML += `<img src=${url} class="demo-image ${index ? "demo-image-right" : ""}"/>`
}