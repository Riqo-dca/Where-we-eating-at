document.addEventListener('DOMContentLoaded', () => {
    const pickRestaurantButton = document.getElementById('pickRestaurant');
    const restaurantNameElement = document.getElementById('restaurantName');
    const restaurantResult = document.getElementById('restaurantResult');

    pickRestaurantButton.addEventListener('click', async () => {
        const locationInput = document.getElementById('locationInput').value;
        if (!locationInput) {
            return;
        }

        const response = await fetch(`/get_random_restaurant?location=${encodeURIComponent(locationInput)}`);
        const data = await response.json();

        if (data.restaurant_name) {
            restaurantNameElement.textContent = data.restaurant_name;
            restaurantResult.classList.remove('hidden');
        } else {
            restaurantNameElement.textContent = 'No restaurants found';
        }
    });
});
