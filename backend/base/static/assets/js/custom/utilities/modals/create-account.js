function initializePersonalAccount() {

    let needToHide = document.querySelectorAll('.company-info-nav');
    let stepperNumber = document.querySelectorAll('.stepper-number');
    needToHide.forEach((el) => {
        if (!el.classList.contains('d-none')) {
            el.classList.add('d-none');
        }
        el.removeAttribute('data-kt-stepper-element');
    });
    stepperNumber.forEach((el, i) => {
        if (i === 4) {
            el.innerText = '4';
        }
        if (i === 5) {
            el.innerText = '5';
        }
    });

}

function initializeBusinessAccount() {
    let needToHide = document.querySelectorAll('.company-info-nav');
    let stepperNumber = document.querySelectorAll('.stepper-number');

    needToHide.forEach((el, i) => {
        if (el.classList.contains('d-none')) {
            el.classList.remove('d-none');
        }
        if (i === 0) {
            el.setAttribute('data-kt-stepper-element', 'nav');
        }
        if (i === 1) {
            el.setAttribute('data-kt-stepper-element', 'content');
        }
    });
    stepperNumber.forEach((el, i) => {
        if (i === 4) {
            el.innerText = '5';
        }
        if (i === 5) {
            el.innerText = '6';
        }
    });

}

function handleAccountTypeChange() {

    let accountType = document.querySelector('input[name="account_type"]:checked').value;
    if (accountType === 'personal') {
        initializePersonalAccount();
    }
    else {
        initializeBusinessAccount();
    }
}
function nextHandler() {
    let allStepperItem = document.querySelectorAll('div[data-kt-stepper-element="nav"]');
    let allContentItem = document.querySelectorAll('div[data-kt-stepper-element="content"]');
    let stepIndex = 0;
    allStepperItem.forEach((el, i) => {
        if (el.classList.contains('current')) {
            stepIndex = i + 1;

            el.classList.remove('current');
            el.classList.add('completed');
        }
        if (allContentItem[i].classList.contains('current')) {
            allContentItem[i].classList.remove('current');
        }
    });
    console.log(stepIndex, allStepperItem.length);
    if (stepIndex < allStepperItem.length) {
        let nextElement = allStepperItem[stepIndex];
        let nextContentElement = allContentItem[stepIndex];
        if (!nextElement.classList.contains('completed')) {
            nextElement.classList.add('current');
        }
        if (!nextContentElement.classList.contains('current')) {
            nextContentElement.classList.add('current');
        }
    }
    if (stepIndex >= (allStepperItem.length - 2)) {
        if (!document.querySelector('button[data-kt-stepper-action="next"]').classList.contains('d-none')) {
            document.querySelector('button[data-kt-stepper-action="next"]').classList.add('d-none');
        }
        if (document.querySelector('button[data-kt-stepper-action="sub"]').classList.contains('d-none')) {
            document.querySelector('button[data-kt-stepper-action="sub"]').classList.remove('d-none');
        }
    }
    if (stepIndex >= 1) {
        if (document.querySelector('button[data-kt-stepper-action="prev"]').classList.contains('d-none')) {
            document.querySelector('button[data-kt-stepper-action="prev"]').classList.remove('d-none');
        }
    }

}

function backHandler() {
    let allStepperItem = document.querySelectorAll('div[data-kt-stepper-element="nav"]');
    let allContentItem = document.querySelectorAll('div[data-kt-stepper-element="content"]');

    let stepIndex = 0;

    allStepperItem.forEach((el, i) => {
        if (el.classList.contains('current')) {
            stepIndex = i - 1;
            console.log(i);

            el.classList.remove('current');

        }
        if (allContentItem[i].classList.contains('current')) {
            allContentItem[i].classList.remove('current');
        }
    });

    if (stepIndex >= 0) {
        let previousElement = allStepperItem[stepIndex];
        let prevContentElement = allContentItem[stepIndex];

        previousElement.classList.remove('completed');
        previousElement.classList.add('current');
        if (!prevContentElement.classList.contains('current')) {
            prevContentElement.classList.add('current');
        }
    }
    if ((stepIndex >= 0) && (stepIndex <= (allStepperItem.length - 2))) {
        if (document.querySelector('button[data-kt-stepper-action="next"]').classList.contains('d-none')) {
            document.querySelector('button[data-kt-stepper-action="next"]').classList.remove('d-none');
        }
        if (!document.querySelector('button[data-kt-stepper-action="sub"]').classList.contains('d-none')) {
            document.querySelector('button[data-kt-stepper-action="sub"]').classList.add('d-none');
        }
    }
    if (stepIndex <= 0) {
        if (!document.querySelector('button[data-kt-stepper-action="prev"]').classList.contains('d-none')) {
            document.querySelector('button[data-kt-stepper-action="prev"]').classList.add('d-none');
        }
    }
}

document.addEventListener("DOMContentLoaded", function () {
    initializePersonalAccount();
});

let radioButtons = document.querySelectorAll('input[type="radio"][name="account_type"]');

radioButtons.forEach((radioButton) => {
    radioButton.addEventListener("change", handleAccountTypeChange);
});

let nextButton = document.querySelector('button[data-kt-stepper-action="next"]');
nextButton.addEventListener("click", nextHandler);

let prevButton = document.querySelector('button[data-kt-stepper-action="prev"]');
prevButton.addEventListener("click", backHandler);