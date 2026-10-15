 // 1. Изчисление за Събиране
        function calculateAddition() {
            const num1 = parseFloat(document.getElementById('add-num1').value) || 0;
            const num2 = parseFloat(document.getElementById('add-num2').value) || 0;
            const num3 = parseFloat(document.getElementById('add-num3').value) || 0;

            document.getElementById('add-result').value = num1 + num2 + num3;
        }

        // 2. Изчисление за Джаули
        function calculatePercentage() {
            const weightInGrams = parseFloat(document.getElementById('pct-num').value) || 0;
            const velocity = parseFloat(document.getElementById('pct-rate').value) || 0;

            if (weightInGrams < 0 || velocity < 0) {
            alert('Въведете положително число!!!');
            document.getElementById('pct-num').value = ''; // Изчиства полето при грешка
            document.getElementById('pct-rate').value = '';
        } else {
            document.getElementById('pct-result').value = ((weightInGrams / 1000) * (velocity * velocity) / 2).toFixed(2)+ 'J';
        }


        }

        // 3. Изчисление за Лице на правоъгълник
        function calculateArea() {
            const a = parseFloat(document.getElementById('area-a').value) || 0;
            const b = parseFloat(document.getElementById('area-b').value) || 0;
            document.getElementById('area-result').value = (a * b).toFixed(2);
        }

        // 4. Изчисление за ИТМ (Формула: тегло / ръст в метри на квадрат)
        function calculateBMI() {
            const weight = parseFloat(document.getElementById('bmi-weight').value) || 0;
            const heightCm = parseFloat(document.getElementById('bmi-height').value) || 0;

            if (weight > 0 && heightCm > 0) {
                const heightM = heightCm / 100;
                const bmi = weight / (heightM * heightM);
                document.getElementById('bmi-result').value = bmi.toFixed(1);
            } else {
                document.getElementById('bmi-result').value = "Грешни данни";
            }
        }

    // Тази функция се задейства САМО когато бутонът бъде натиснат
    function validateForm() {
        // 1. Намираме полето по неговото ID ('pct-result')
        let inputElement = document.getElementById('pct-result');

        // 2. Вземаме въведената стойност
        let value = Number(inputElement.value);

        // 3. Проверяваме дали полето е празно
        if (inputElement.value === '') {
            alert('Моля, първо въведете число!');
            return;
        }

        // 4. Валидация за отрицателно число
        if (value < 0) {
            alert('Въведете положително число!!!');
            inputElement.value = ''; // Изчиства полето при грешка
        } else {
            alert('Чудесно! Числото е валидно.');
            // Тук можете да продължите с изчисленията...
        }
    }
