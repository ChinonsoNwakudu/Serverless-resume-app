<<<<<<< HEAD
window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const functionApiUrl = '';
const localFunctionApi = '';

const getVisitCount = () => {
    let count = 30;
    fetch(functionApiUrl).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called function API.");
        count =  response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });
    return count;
}
=======
window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});

const functionApiUrl = 'https://nonsoresumeapp.azurewebsites.net/api/get_resume?code=t97DvBy6AdRcel_TpAAQOmmJrp1ccusWtZOIv3kXoxGIAzFunczcKA%3D%3D&api_type=visitor-counter';
const visitorCountContainer = document.getElementById("visitor_count");

const getVisitCount = () => {
    let count = 30; // Default value
    fetch(functionApiUrl)
        .then(response => {
            console.log("API Response Status:", response.status); // Log response status
            return response.json();
        })
        .then(response => {
            console.log("API Response Body:", response); // Log API response body
            count = response.visitorCount;
            visitorCountContainer.innerText = count; // Update HTML element with the count
        })
        .catch(error => {
            console.error("Fetch Error:", error); // Log any fetch errors
        });
};
>>>>>>> function app files and CI/CD pipeline
