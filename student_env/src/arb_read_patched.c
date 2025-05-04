#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void strip_newline(char *str) {
	size_t len = strlen(str);
	if (len > 0 && str[len - 1] == '\n') {
		str[len - 1] = '\0';
	}
}

void menu(){
	printf("Terminal flag vault 2.0\n");
	printf("Keeping all your flags safe for 0xffff days!\n");
	printf("\n");
}

int check_password(char* checkme, int size){
	const char* pw_env = "ADMIN_PASS";
	const char* password = getenv(pw_env);

	if(password == NULL)
	{
		printf("Set environment variable!\n");
		exit(1);
	}
	

	strip_newline(checkme);
	return (strncmp(password, checkme, (size_t)size) == 0);

}

void get_flag(char* flag, int size){
	FILE* fd;
	fd = fopen("flag.txt", "r");
	fgets(flag, size, fd);
}	

void vuln() {	
	int SIZE = 37;
	char flag[SIZE];
	char password[SIZE];
	int admin = 0;
	get_flag(flag, SIZE);
	
	printf("Please enter the admin password: ");
	fgets(password, SIZE, stdin);

	admin = check_password(password, SIZE);

	if(admin)
		printf("%s", flag);
	else
	{
		printf("You entered: ");
		printf("%s",password);
		printf("\nThis was wrong! Goodbye!\n");
		exit(1);
	}
}	

int main() {
	setbuf(stdout, NULL);
	menu();
	vuln();
}
