(async function() {
  // open https://adventofcode.com/2024/day/6/input in browser and copy code to dev console
  // viz
  let cellSize=10
  let wait = (d=0) => new Promise(resolve => window.tmr=setTimeout(resolve, d))
  if (window.rec) try { window.rec.stop() } catch(e) {}
  clearTimeout(window.tmr)

  function initCanvas(canvasSize, cellSize) {
    let canvas=document.querySelector('canvas')
    if (!canvas) {
      canvas=document.createElement('canvas')
      document.body.appendChild(canvas)
    }
    canvas.width=canvasSize; canvas.height=canvasSize
    Object.assign(canvas.style, {position:'absolute', top:0, right:0, background:'#000', color:'#fff', zIndex: 10})
    let ctx=canvas.getContext('2d')
    ctx.font = `bold ${cellSize}px monospace`
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
    }
    rec.start()
    return rec
  }

  function viz(txt, i, j, color='gray') {
    ctx.clearRect(j*cellSize, i*cellSize, cellSize, cellSize)
    ctx.fillStyle = txt == 'O' ? 'cyan' : color
    ctx.fillText(txt, j*cellSize, i*cellSize)
  }

  let m=document.querySelector('pre').textContent.trim().split('\n').map(line => line.split(''))
  let sz=m.length

  let [canvas, ctx]=initCanvas(cellSize*sz, cellSize)
  let rec=startRec(canvas)

  function mdraw(){
    for (let i=0;i<sz;i++) for (let j=0;j<sz;j++) viz(m[i][j], i, j)
  }
  mdraw()

  // solve
  function solve(pi, pj, visited=new Set()) {
    let turns = new Set()
    let directions = [[-1,0], [0,1], [1,0], [0,-1]]
    let di=0
    visited.add(`${pi},${pj}`)

    function move() {
      let [hi, hj]=directions[di]
      if (!m[pi+hi] || !m[pi+hi][pj+hj]) return 1 // exit
      if (m[pi+hi][pj+hj] == '#') {
        di = (di + 1) % 4
        let turnCoord = `${pi},${pj}->${pi+hi},${pj+hj}`
        if (turns.has(turnCoord)) return 2 // loop
        turns.add(turnCoord)
      } else {
        pi += hi
        pj += hj
        visited.add(`${pi},${pj}`)
      }
    }
    let r; while (!(r=move()));
    return r
  }

  let starti, startj
  for (let i=0;i<sz;i++) for (let j=0;j<sz;j++) {
    if (m[i][j] == '^') {
      starti=i
      startj=j
    }
  }

  // part1
  let visited = new Set()
  solve(starti, startj, visited)
  console.log(`part1: visited=${visited.size}`)
  visited.forEach(v => {let [i, j] = v.split(','); viz('@', i, j, 'yellow') }); await wait(1000)

  // part2
  let obstacles = new Set()
  for (let i=0;i<sz;i++) {
    for (let j=0;j<sz;j++) {
      if (!visited.has(`${i},${j}`)) continue
      if (m[i][j] != '#' && !(starti == i && startj == j)) {
        let orig = m[i][j]
        m[i][j] = '#'
        if (solve(starti, startj) == 2) {
          m[i][j] = 'O'
          obstacles.add(`${i},${j}`)
        } else {
          m[i][j] = orig
        }
      }
    }
    mdraw()
    await wait(0)
  }
  console.log(`part2: obstacles=${obstacles.size}`)

  window.rec?.stop()
})()
