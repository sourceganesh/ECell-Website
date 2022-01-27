const menuBtn = document.getElementById("menuBtn");
const cancelBtn = document.getElementById("cancelBtn");
const navContent = document.getElementById("navContent");
const navLinks = document.getElementsByClassName("navLinks");

menuBtn.addEventListener("click",()=>{
    menuBtn.classList.add("notVisible");
    cancelBtn.classList.remove("notVisible");
    navContent.classList.remove("notVisible");
})
const cancelFun =()=>{
    cancelBtn.classList.add("notVisible");
    navContent.classList.add("notVisible");
    menuBtn.classList.remove("notVisible");
}
navLinks[0].addEventListener("click",cancelFun);
navLinks[1].addEventListener("click",cancelFun);
navLinks[2].addEventListener("click",cancelFun);
navLinks[3].addEventListener("click",cancelFun);
cancelBtn.addEventListener("click",cancelFun);