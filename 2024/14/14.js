(async function() { // only part2
  // open https://adventofcode.com/2024/day/14/input in browser and copy code to dev console
  let csz = 12
  let wait = (d = 0) => new Promise(resolve => window.tmr = setTimeout(resolve, d))
  let tick = () => new Promise(resolve => requestAnimationFrame(resolve))
  if (window.rec) try { window.rec.stop() } catch (e) {}
  clearTimeout(window.tmr)

  function initCanvas(width, height, csz) {
    let canvas = document.querySelector('canvas')
    if (!canvas) {
      canvas = document.createElement('canvas')
      document.body.appendChild(canvas)
    }
    canvas.width = width
    canvas.height = height
    Object.assign(canvas.style, {position: 'absolute', top: 0, right: 0, background: '#000', color: '#fff', zIndex: 10})
    let ctx = canvas.getContext('2d')
    ctx.font = `bold ${csz}px monospace`
    ctx.fillStyle = 'green'
    ctx.textBaseline = 'top'
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    return [canvas, ctx]
  }

  function startRec(canvas) {
    let chunks=[]
    let stream=canvas.captureStream()
    let rec = window.rec = new MediaRecorder(stream)
    rec.ondataavailable = e => chunks.push(e.data)
    rec.onstop = () => {
      let video = document.querySelector('video')
      if (!video) {
        video = document.createElement('video')
        document.body.appendChild(video)
      }
      video.controls = true
      video.src = URL.createObjectURL(new Blob(chunks, {type: 'video/webm'}))
      Object.assign(video.style, {position: 'absolute', top: `${canvas.height + 100}px`, right: 0})
    }
    rec.start()
    return rec
  }

  let pattern = /p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)/
  let robots = document.querySelector('pre').textContent.trim().split('\n').map(line => line.match(pattern).slice(1).map(v => parseInt(v)))
  let robotCount = robots.length, xmax = 101, ymax = 103
  let [canvas, ctx] = initCanvas(xmax * csz, ymax * csz, csz)
  let rec, startVizAt = 0, maxIterations = 10000

  for (let sec = 0; sec < maxIterations; sec++) {
    if (sec == startVizAt) {
      rec=startRec(canvas)
    }
    let vizpoint = sec >= startVizAt && (sec % ymax == 88 || sec % xmax == 22)
    if (vizpoint) ctx.clearRect(0, 0, csz * xmax, csz * ymax)
    for (let i=0; i<robotCount; i++) {
      let [px, py, vx, vy] = robots[i]
      px += vx
      py += vy
      if (px < 0) px += xmax
      else if (px >= xmax) px -= xmax
      if (py < 0) py += ymax
      else if (py >= ymax) py -= ymax
      if (vizpoint) ctx.fillRect(px * csz, py * csz, csz, csz)
      robots[i][0] = px
      robots[i][1] = py
    }
    if (vizpoint) {
      ctx.clearRect(0, 0, csz * 3, csz)
      ctx.fillText(sec, 0, 0)
      await wait(1000/30)
    }
  }

  window.rec?.stop()
})()
