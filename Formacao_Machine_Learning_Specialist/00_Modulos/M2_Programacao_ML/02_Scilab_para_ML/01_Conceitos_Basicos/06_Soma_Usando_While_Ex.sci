total = 0;
x = input('Digite o primeiro número: ');

while (x ~= 0)
    total = total + x;
    x = input('Digite o próximo número (ou 0 para encerrar): ');
end

printf('A soma dos números informados é: %d', total);
