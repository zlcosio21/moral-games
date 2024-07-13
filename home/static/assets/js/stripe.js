document.addEventListener('DOMContentLoaded', function () {
  var stripe = Stripe('pk_test_51ODzPyKszJaXSI9CCrypMsf0CTS0eh3elC35HRocQ11h9Spt2aYxD7PHXU49sv4VIXcM5DqmqbleDJt6sULzCEQ3001GTsGMcw');
  var elements = stripe.elements();

  var card = elements.create('card');
  card.mount('#card-element');

  var form = document.getElementById('payment-form');
  var submitButton = document.getElementById('submit-button');

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    submitButton.disabled = true;

    stripe.createToken(card).then(function (result) {
      if (result.error) {

        var errorElement = document.getElementById('card-errors');
        errorElement.textContent = result.error.message;
        submitButton.disabled = false;
      } else {

        var tokenInput = document.createElement('input');
        tokenInput.setAttribute('type', 'hidden');
        tokenInput.setAttribute('name', 'stripeToken');
        tokenInput.setAttribute('value', result.token.id);
        form.appendChild(tokenInput);

        form.submit();
      }
    });
  });
});