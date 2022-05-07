
let btn = document.querySelector('.btn');
//let download = document.querySelector('#download');
//btn.addEventListener("click", () => {
////    document.getElementById("download").style.display = "block";
//    async function call(){
//        let name = document.querySelector('.main_input').value;
//        await linker.title(name)
//    }
//    console.log(call());
//});


btn.addEventListener("click", sendData);
async function sendData() {
    let search = document.querySelector('.main_input').value;
    await linker.content(search);
}
