const request = require('request');
const fs = require('fs');
const https = require('https');

function main() {
    URLAry = urls();
    for (let i = 0; i < URLAry.length; i++) {
        var document = URLAry[i]
        console.log(document);
        fs.appendFile('urls.txt', document, (err) => {
            if (err) throw err;
        })
        fs.appendFile('urls.txt', '\n', (err) => {
            if (err) throw err;
        })
    }
}

// category list
const categories = [
    "All Season Hikes",
    "Alpine Hikes",
    "Backpackable Hikes",
    "Beach Hikes",
    "Bushwhacks",
    "Creek Hikes",
    "Crowded Hikes",
    "Exposed Hikes",
    "Family Hikes",
    "Glacier Hikes",
    "Hike and Bike",
    "Hot Spring Hikes",
    "Lake Hikes",
    "Lookout Hikes",
    "Loop Hikes",
    "Lost Hikes",
    "Off The Beaten Track",
    "Off Trail",
    "Old Growth Hikes",
    "Rails to Trails",
    "Scrambles",
    "Snowshoe Hikes",
    "Traverse Hikes",
    "Unmaintained Trails",
    "Universal Access Hikes",
    "Urban Hikes",
    "Viewpoint Hikes",
    "Volcanic Feature Hikes",
    "Waterfall Hikes",
    "Wilderness Hikes",
    "Wildflower Hikes",
    "Wildlife Refuge Hikes",
    "Wildlife Viewing Hikes",
]

function urls() {
    URLAry = [];
    for (let i = 0; i < categories.length; i++) {
        var requestData = {
            category: categories[i],
            difficulty: "?Difficulty",
            distance: "?Distance",
            elevationGain: "?Elevation Gain",
            format: "?format=broadtable"
        };
        URLAry.push(constructURL(requestData));
    }
    return URLAry;
}

function constructURL(requestData) {
    // this is the standard part of the request
    URL = "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category"
    // add # number of words in name   
    var wordCount = requestData.category.match(/(\w+)/g).length;
    var words = requestData.category.split(' ');

    /*
    console.log(wordCount);
    console.log(requestData.category);
    console.log(words);
    */

    for (let i = 0; i < wordCount; i++) {
        var cache = "";
        if (i == 0) {
            //add %3A
            cache = "%3A" + words[i];
        }
        else {
            cache = "%20" + words[i];
        }
        URL = URL + cache
    }

    //examples
    //https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AAll%20Season%20Hikes]]&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes#
    //https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AWildflower%20Hikes]]  &po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes

    //adding the final stuff
    URL = URL + "&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes";
    return URL;
}

main();