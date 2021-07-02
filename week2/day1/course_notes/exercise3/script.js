// 1. Create a numerically indexed table (ie. an array): pets, like this ['cat','dog','fish','rabbit','cow']

// 2. Display dog

// 3. Add to the array pets, the pet horse. Remove the pet rabbit

// 4. Display the array length

let pets = ['cat','dog','fish','rabbit','cow'];
pets.push('horse');
pets.splice(3,1);
console.log(pets.length);