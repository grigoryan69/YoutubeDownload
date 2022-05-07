let btn = document.querySelector('.btn');
btn.addEventListener("click", sendData);
async function sendData() {
    let search = document.querySelector('.main_input').value;
    await linker.sendtube(search);
}
