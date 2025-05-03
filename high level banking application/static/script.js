document.addEventListener('DOMContentLoaded', () => {
    // Add animations to page elements
    animateElements();

    // Form submission handling
    setupFormAnimations();

    // Balance update animation
    setupBalanceObserver();

    // Transaction history animations
    animateTransactionRows();
});

function animateElements() {
    // Animate alerts
    document.querySelectorAll('.alert').forEach(alert => {
        alert.classList.add('fade-in');
    });

    // Animate dashboard elements
    const balanceElement = document.querySelector('.balance');
    if (balanceElement) {
        balanceElement.classList.add('fade-in');
    }
}

function setupFormAnimations() {
    // Transfer form animation
    const transferForm = document.querySelector('form[action="/transfer"]');
    if (transferForm) {
        transferForm.addEventListener('submit', function(e) {
            // Show loading spinner
            const spinner = document.createElement('div');
            spinner.className = 'loading-spinner';
            spinner.innerHTML = '⏳'; // Or use a CSS spinner
            this.appendChild(spinner);
            spinner.style.display = 'block';

            // Disable button during submission
            const submitButton = this.querySelector('button[type="submit"]');
            submitButton.disabled = true;
            submitButton.innerHTML = 'Processing...';
        });
    }
}

function setupBalanceObserver() {
    // Animate balance changes
    const balanceElement = document.querySelector('.balance h2');
    if (balanceElement) {
        let observer = new MutationObserver(mutations => {
            mutations.forEach(mutation => {
                if (mutation.type === 'characterData') {
                    balanceElement.classList.add('balance-pulse');
                    setTimeout(() => {
                        balanceElement.classList.remove('balance-pulse');
                    }, 1000);
                }
            });
        });

        observer.observe(balanceElement, {
            characterData: true,
            subtree: true
        });
    }
}

function animateTransactionRows() {
    // Animate transaction table rows
    const rows = document.querySelectorAll('table tr:not(:first-child)');
    rows.forEach((row, index) => {
        setTimeout(() => {
            row.style.opacity = 0;
            row.classList.add('slide-in');
            row.style.opacity = 1;
        }, index * 100);
    });

    // Hover effects
    document.querySelectorAll('tr').forEach(row => {
        row.classList.add('hover-grow');
    });
}

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});