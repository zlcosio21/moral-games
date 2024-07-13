function limitQuantity(input) {
    if (parseInt(input.value) > parseInt(input.getAttribute('max'))) {
        input.value = input.getAttribute('max');
    }

    if (parseInt(input.value) < parseInt(input.getAttribute('min'))) {
        input.value = input.getAttribute('min');
    }
}