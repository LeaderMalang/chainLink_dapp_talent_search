require('dotenv').config()
const axios = require('axios')

axios({
  method: 'post',
  url: `http://localhost:6688/v2/specs/${process.env.JOB_ID}/runs`,
  headers: {
    'X-Chainlink-EA-AccessKey': process.env.ACCESSKEY,
    'X-Chainlink-EA-Secret': process.env.SECRET
  },
  data:{
    'to':"shahbax@gmail.com",
    'from':"hassan@gamil.com",
    'message':"hdsdsad",
    "subject":"hdsadasdsadas"
  }
})
.then(e => {
  console.log('DONE')
})
.catch(e => {
  console.log(e)
})