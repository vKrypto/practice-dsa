
const jsonfile = require('jsonfile');
const moment = require('moment');
const simpleGit = require('simple-git');

const file_path = './data.json'



con st makeCommits = n=>{
    const x= Math.floor((Math.random() * 54) + 1);
    const y= Math.floor((Math.random() * 6) + 1);
    
    const DATE = moment().subtract(1, 'y').add(1, 'd').add(x, 'w').add(y, 'd').format()
    
    const data = {date: DATE}
    console.log(data)


    jsonfile.writeFile(file_path, data, ()=>{
        simpleGit().add([file_path]).commit(DATE, {'--date': DATE}, makeCommits.bind(this, --n))
    })

}
makeCommits(1)