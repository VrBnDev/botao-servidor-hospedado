#include <stdio.h>
#include "pico/stdio.h"
#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"
#include "hardware/adc.h"
#include "lwip/altcp_tls.h"
#include "example_http_client_util.h"

// ======= CONFIGURAÇÕES ======= //
#define HOST "botao-servidor-hospedado.vercel.app"
#define PORT 80
#define USE_TLS true
#define INTERVALO_MS 50
#define BUTTON_LEFT 5
#define LED_BLUE 12
#define LED_RED 13

// ============================= //

void enviar_comando(const char* path) {
    EXAMPLE_HTTP_REQUEST_T req = {0};
    req.hostname = HOST;
    req.url = path;
    req.port = PORT;
    req.headers_fn = http_client_header_print_fn;
    req.recv_fn = http_client_receive_print_fn;
    req.tls_config = altcp_tls_create_config_client(NULL, 0);

    printf("Enviando comando: %s\n", path);
    int result = http_client_request_sync(cyw43_arch_async_context(), &req);

    if (result == 0) {
        printf("Comando enviado com sucesso!\n");
    } else {
        printf("Erro ao enviar comando: %d\n", result);
    }

    sleep_ms(100);  // Delay para evitar envios repetidos
}

int main() {
    stdio_init_all();
    gpio_init(BUTTON_LEFT);
    gpio_set_dir(BUTTON_LEFT, GPIO_IN);
    gpio_pull_up(BUTTON_LEFT);

    gpio_init(LED_BLUE);
    gpio_set_dir(LED_BLUE, GPIO_OUT);
    gpio_init(LED_RED);
    gpio_set_dir(LED_RED, GPIO_OUT);

    printf("\nIniciando cliente HTTP...\n");

    if (cyw43_arch_init()) {
        printf("Erro ao inicializar Wi-Fi\n");
        return 1;
    }
    cyw43_arch_enable_sta_mode();

    printf("Conectando ao Wi-Fi...\n");
    if (cyw43_arch_wifi_connect_timeout_ms(WIFI_SSID, WIFI_PASSWORD, 
                                           CYW43_AUTH_WPA2_AES_PSK, 30000)) {
        printf("Falha na conexão Wi-Fi\n");
        return 1;
    }

    printf("Conectado! IP: %s\n", ip4addr_ntoa(netif_ip4_addr(netif_list)));

    bool estado_anterior = true;  // Considera que o botão começa solto

    while (1) {
        bool estado_atual = gpio_get(BUTTON_LEFT);  // 1 = solto, 0 = pressionado

        if (estado_atual != estado_anterior) {
            if (estado_atual == 0) {
                enviar_comando("/pressed");
            } else {
                enviar_comando("/unpressed");
            }

            estado_anterior = estado_atual;
        }

        sleep_ms(INTERVALO_MS);
    }
}
