export default{
    getUniversity: (id) => {
    return fetch('https://localhost:44331/api/university/' + id)
        .then(response => response.json());
    },

    getSuggestedUniversity: (token) => {
        return fetch('https://localhost:44331/api/university/suggestion/' + token)
            .then(response => response.json());
    }
}