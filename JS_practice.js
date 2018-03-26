// Write a function that takes a color and the candy map. It should return the flavor or if it’s not in the map, console log “Sorry, that color doesn’t have a flavor” and return nothing.
// Write a function that takes an array of colors and returns an array of the corresponding flavors. If the map doesn’t have the color, add null to the array.

let candy = new Map([["purple","grape"],["pink","strawberry"],["yellow","lemon"],["blue","blueberry"],["green","lime"]])

console.log(candy)

console.log(candy.get("green"))
function returnFlavor(map1, color) {
    if (map1.get(color)) {
        console.log(map1.get(color));
    }
    else {
        console.log("Sorry this color has no flavor!")
    }
}

console.log(returnFlavor(candy, "green"))

function getFlavor(colorarray) {
    let new_list = [];
    for (color of colorarray) {
        if (candy.get(color)) {
            new_list.push(candy.get(color));
        }
        else {
            new_list.push("null");
        }
    }
    return new_list
}

console.log(getFlavor(["yellow","blue","red","green"]))

// Create a function that reverses a word
// Create a function that takes an array of words and returns a new array of the words with each word reversed
// Create a function that returns a random word from an array

function wordReverse(string1) {
    let newString = '';
    for (let i=string1.length-1; i >= 0; i--) {
        newString += string1[i]
    }
    
    return newString
}

console.log(wordReverse("hippo"))

function reverseEach(stringArray) {
    let newArray = [];
    for (word of stringArray) {
        reversedWord = ''
        for (let i=word.length-1; i>=0; i--) {
            reversedWord += word[i]
        }
        newArray.push(reversedWord)
    }
    return newArray
}

console.log(reverseEach(['apple','berry','cherry']))

function getRandom(stringArray) {
    randomw = Math.floor(Math.random() * Math.floor(stringArray.length));
    console.log(stringArray[randomw])
}

console.log(getRandom(['apple','berry','cherry']))




