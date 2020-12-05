let constraintObj = {
    audio: false,
    video: true,
}

function makeTime(){
    let minute = Number(document.getElementById('minute').innerText)
    let seconds = Number(document.getElementById('seconds').innerText)

    if(seconds == 60){
        seconds = 0
        minute += 1
    }else{
        seconds += 1
    }

    if(minute < 10) 
        document.getElementById('minute').innerText = String('0'+minute)
    else 
        document.getElementById('minute').innerText = String(minute)

    if(seconds < 10) 
        document.getElementById('seconds').innerText = String('0'+seconds)
    else 
        document.getElementById('seconds').innerText = String(seconds)
}

if (navigator.mediaDevices === undefined) {
    navigator.mediaDevices = {}
    navigator.mediaDevices.getUserMedia = function(constraintObj) {
        let getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia
        if (!getUserMedia) {
            return Promise.reject( new Error ('getUserMedia does not works in this browser'))
        }
        return new Promise(function(resolve, reject) {
            getUserMedia.call(navigator, constraintObj, resolve, reject)
        });
    }
}else{
    navigator.mediaDevices.enumerateDevices()
    .then(devices => {
        devices.forEach(device=>{
            //console.log(device.kind.toUpperCase(), device.label)
        })
    })
    .catch(err=>{
        console.log(err.name, err.message)
    })
}

navigator.mediaDevices.getUserMedia(constraintObj)
  .then(function(mediaStreamObj) {
      let video = document.querySelector('video')
      if ("srcObject" in video) {
          video.srcObject = mediaStreamObj
      } else {
          video.src = window.URL.createObjectURL(mediaStreamObj)
      }

      video.onloadedmetadata = function(event) {
          video.play()
      }
      
      let start = document.getElementById('btnStart')
      let stop = document.getElementById('btnStop')
      let vidSave = document.getElementById('vid2')
      let mediaRecorder = new MediaRecorder(mediaStreamObj)
      let chunks = []                
      let pointForCut = null
      let pointForTimer = null

      async function cutVedio(){
        mediaRecorder.stop()
        mediaRecorder.start()
      }

      

      start.addEventListener('click', (ev)=>{

        let time = Number(prompt("write a second"))
        //video.play()
          
        mediaRecorder.start()
          
        pointForCut = setInterval(async() => {
            cutVedio()
        }, (time*1000 + 1000))

        pointForTimer = setInterval(async()=>{
            makeTime()
        }, 1000)
          
      })

      stop.addEventListener('click', async (ev)=>{
        //video.pause()
        clearInterval(pointForCut)
        clearInterval(pointForTimer)
        mediaRecorder.stop()
        console.log("stop")

        document.getElementById('minute').innerText = '0'
        document.getElementById('seconds').innerText = '00'
      })

      mediaRecorder.ondataavailable = async function(event) {
          chunks.push(event.data)
      }

      mediaRecorder.onstop = async (event)=>{
          let blob = new Blob(chunks, { type : 'video/mp4;' })

          let form = new FormData()
          form.append('data', blob ,'myFile.mp4')

          let request = await fetch('http://178.154.250.25/:8000/makeFileMp4',{
                  method : 'POST',
                  body: form
          })

          let responce = await request.json()
          console.log(responce.answer)
          if(responce.answer == 'true'){
              document.getElementById('answerFromServer').innerText = 'Ложь не замеченна'
              document.getElementById('placeAnswer').style.backgroundColor = '#1D6B18'
          }else{
            document.getElementById('answerFromServer').innerText = 'Ложь замеченна'
            document.getElementById('placeAnswer').style.backgroundColor = '#BB1313'
          }

          chunks = []
      }
  })
  .catch(function(err) {
      console.log(err.name, err.message)
  })
