let projectsUrl= 'http://127.0.0.1:8000/api/projects/'

let getProjects= () => {
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data=> {
        console.log(data)
        buildProjects(data)
    })
}



let buildProjects= (projects) => {
    let projectsWrapper= document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML=''
    for (let i=0;projects.length>i;i++){
let project= projects[i]
let projectCard= `
                  <div class="project--card">
                  <img src="http://127.0.0.1:8000${project.featured_img}">
                  <div>
                  <div class="card--header">
                  <h3>${project.title}</h3>
                  <strong class="vote--option" data-vote="up" data-project= "${project.id}">&#x2719;</strong>
                  <strong class="vote--option" data-vote="down" data-project= "${project.id}">&#x2212;</strong>
                  </div>
                  <i>${project.vote_ratio}% Postive feedback</i>
                  <p>${project.description.substring(0,150)}</p>
                  </div>
                  </div>
`
projectsWrapper.innerHTML +=projectCard
    }
    addVoteEvent()
}


let addVoteEvent =() => {
let voteBtns= document.getElementsByClassName('vote--option')
for (let i=0; voteBtns.length>i; i++){
    voteBtns[i].addEventListener('click',(e)=> {
        let vote= e.target.dataset.vote
        let project= e.target.dataset.project
        let token= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzMDgyMTQ0LCJpYXQiOjE3MDMwODE4NDQsImp0aSI6IjczYTQ2ZjQ4NzBiNjRmOWFhYTc2NDFlMDBkYThmNDgyIiwidXNlcl9pZCI6MX0.rPfRQBMRjzU6rMOEBcIc8Z_8O_Hzpq638hrphOckwEY'
        console.log("Project",project,"Vote", vote)
        fetch(`http://127.0.0.1:8000/api/project/17213ad2-7809-4881-adea-4ce610e65622/vote`,{
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                Authorization: `Bearer ${token}`,

            },
            body: JSON.stringify({'value':vote})
        })
        .then(response=>response.json())
        .then(data=>{
            console.log("Success",data)
        })
    })
}
}
getProjects()
