#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int check_key(const char *key) {
    if (strlen(key) != 8)
        return 0;

    int sum = 0;
    for (int i = 0; i < 8; i++) {
        if (key[i] < 'A' || key[i] > 'Z')  
            return 0;
        sum += key[i] * (i + 1);
    }

    return (sum % 1337 == 420); 
}

int main() {
    char key[100];
    printf("Enter your license key: ");
    scanf("%s", key);

    if (check_key(key)) {
        printf("Valid license key! Access granted.\n");
    } else {
        printf("Invalid key. Access denied.\n");
    }

    return 0;
}
