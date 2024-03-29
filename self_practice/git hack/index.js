
const jsonfile = require('jsonfile');
// const moment = require('moment');
const simpleGit = require('simple-git');

const file_path = './data.json'

function randomDate(date1, date2){
    function randomValueBetween(min, max) {
      return Math.random() * (max - min) + min;
    }
    var date1 = date1 || '01-01-1970'
    var date2 = date2 || new Date().toLocaleDateString()
    date1 = new Date(date1).getTime()
    date2 = new Date(date2).getTime()
    if( date1>date2){
        return new Date(randomValueBetween(date2,date1)).toLocaleDateString()   
    } else{
        return new Date(randomValueBetween(date1, date2)).toLocaleDateString()  

    }
}



const makeCommits = n =>{
    if(n==0) return;

    // const x= Math.floor((Math.random() * 54) + 1);
    // const y= Math.floor((Math.random() * 6) + 1);
    
    // const DATE = moment().subtract(1, 'y').add(1, 'd').add(x, 'w').add(y, 'd').format()
    const DATE = randomDate('03/13/2023', '03/28/2024')
    
    const data = {date: DATE}
    console.log(data)


    jsonfile.writeFile(file_path, data, ()=>{
        simpleGit().add([file_path]).commit(DATE, {'--date': DATE}, makeCommits.bind(this, --n))
    })

}
makeCommits(30)