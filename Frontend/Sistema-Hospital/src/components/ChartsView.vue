<template>
    <!-- Gráficas en el Dashboard -->
    <div class="p-4">
        <div class="flex justify-center gap-4 mb-4">
            <!-- Gráfica de Dona -->
            <div class="flex-1 max-w-[400px]">
                <apexchart type="donut" :options="priorityChartOptions" :series="priorityChartSeries" width="100%">
                </apexchart>
            </div>

            <!-- Gráfica de Barras -->
            <div class="flex-1 max-w-[400px]">
                <apexchart type="bar" :options="statusChartOptions" :series="statusChartSeries" width="100%">
                </apexchart>
            </div>
        </div>

        <!-- Gráficas de organos -->
        <div class="flex justify-center gap-4 mb-4">
            <!-- Gráfica de Columnas-->
            <div class="flex-1 max-w-[400px]">
                <apexchart type="bar" :options="organAvailabilityChartOptions" :series="organAvailabilityChartSeries"
                    width="100%"></apexchart>
            </div>
            <!-- Gráfica de Líneas -->
            <div class="flex-1 max-w-[400px]">
                <apexchart type="line" :options="organSystemChartOptions" :series="organSystemChartSeries" width="100%">
                </apexchart>
            </div>
        </div>
    </div>
</template>

<script>
import ApexCharts from 'vue3-apexcharts';

export default {
    components: {
        apexchart: ApexCharts,
    },
    data() {
        return {
            // Opciones para la gráfica de dona
            priorityChartOptions: {
                chart: {
                    type: 'donut',
                },
                labels: ['Urgente', 'Alta', 'Moderada', 'Emergente', 'Normal'],
                legend: {
                    position: 'bottom',
                },
                responsive: [
                    {
                        breakpoint: 480,
                        options: {
                            chart: {
                                width: 300,
                            },
                            legend: {
                                position: 'bottom',
                            },
                        },
                    },
                ],
            },
            priorityChartSeries: [10, 10, 10, 10, 10],

            // Opciones para la gráfica de barras
            statusChartOptions: {
                chart: {
                    type: 'bar',
                },
                xaxis: {
                    categories: ['Registrada', 'Programada', 'Cancelada', 'Reprogramada', 'En_Proceso', 'Realizada'],
                },
                title: {
                    text: 'Estado de Solicitudes',
                },
                plotOptions: {
                    bar: {
                        horizontal: false,
                        endingShape: 'rounded',
                    },
                },
                dataLabels: {
                    enabled: true,
                },
                legend: {
                    position: 'top',
                },
                responsive: [
                    {
                        breakpoint: 480,
                        options: {
                            chart: {
                                width: 300,
                            },
                            legend: {
                                position: 'bottom',
                            },
                        },
                    },
                ],
            },
            statusChartSeries: [{
                name: 'Número de Solicitudes',
                data: [0, 0, 0, 0, 0, 0], // Valores iniciales
            }],
            // Opciones para la gráfica de columnas
            organAvailabilityChartOptions: {
                chart: {
                    type: 'bar',
                },
                xaxis: {
                    categories: ['Disponible', 'No Disponible', 'Reservado'],
                },
                title: {
                    text: 'Disponibilidad de Órganos',
                },
                plotOptions: {
                    bar: {
                        horizontal: false,
                        endingShape: 'rounded',
                    },
                },
                dataLabels: {
                    enabled: true,
                },
                legend: {
                    position: 'top',
                },
                responsive: [
                    {
                        breakpoint: 480,
                        options: {
                            chart: {
                                width: 300,
                            },
                            legend: {
                                position: 'bottom',
                            },
                        },
                    },
                ],
            },
            organAvailabilityChartSeries: [{
                name: 'Número de Órganos',
                data: [0, 0, 0], // Valores iniciales
            }],

            // Opciones para la gráfica de líneas
            organSystemChartOptions: {
                chart: {
                    type: 'line',
                },
                xaxis: {
                    categories: [
                        'Circulatorio', 'Digestivo', 'Respiratorio', 'Nervioso', 'Muscular', 'Esquelético',
                        'Endocrino', 'Linfático', 'Inmunológico', 'Reproductor', 'Urinario', 'Sensorial'
                    ],
                },
                title: {
                    text: 'Aparato/Sistema de Órganos',
                },
                dataLabels: {
                    enabled: true,
                },
                legend: {
                    position: 'top',
                },
                responsive: [
                    {
                        breakpoint: 480,
                        options: {
                            chart: {
                                width: 300,
                            },
                            legend: {
                                position: 'bottom',
                            },
                        },
                    },
                ],
            },
            organSystemChartSeries: [{
                name: 'Número de Órganos',
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], // Valores iniciales
            }],
        };
    },
    async created() {
        try {
            const response = await fetch('http://127.0.0.1:8000/solicitudes');
            const solicitudes = await response.json();

            const priorityCounts = {
                Urgente: 0,
                Alta: 0,
                Moderada: 0,
                Emergente: 0,
                Normal: 0,
            };

            const statusCounts = {
                Registrada: 0,
                Programada: 0,
                Cancelada: 0,
                Reprogramada: 0,
                En_Proceso: 0,
                Realizada: 0,
            };

            solicitudes.forEach(solicitud => {
                if (priorityCounts[solicitud.Prioridad] !== undefined) {
                    priorityCounts[solicitud.Prioridad]++;
                }

                if (statusCounts[solicitud.Estatus] !== undefined) {
                    statusCounts[solicitud.Estatus]++;
                }
            });

            this.priorityChartSeries = [
                priorityCounts.Urgente,
                priorityCounts.Alta,
                priorityCounts.Moderada,
                priorityCounts.Emergente,
                priorityCounts.Normal,
            ];

            this.statusChartSeries[0].data = [
                statusCounts.Registrada,
                statusCounts.Programada,
                statusCounts.Cancelada,
                statusCounts.Reprogramada,
                statusCounts.En_Proceso,
                statusCounts.Realizada,
            ];

            const result = await fetch('http://127.0.0.1:8000/organs');
            const organs = await result.json();

            const availabilityCounts = {
                Disponible: 0,
                No_Disponible: 0,
                Reservado: 0,
            };

            const systemCounts = {
                Circulatorio: 0,
                Digestivo: 0,
                Respiratorio: 0,
                Nervioso: 0,
                Muscular: 0,
                Esquelético: 0,
                Endocrino: 0,
                Linfático: 0,
                Inmunológico: 0,
                Reproductor: 0,
                Urinario: 0,
                Sensorial: 0,
            };

            organs.forEach(organ => {
                if (availabilityCounts[organ.Disponibilidad] !== undefined) {
                    availabilityCounts[organ.Disponibilidad]++;
                }

                if (systemCounts[organ.Aparato_Sistema] !== undefined) {
                    systemCounts[organ.Aparato_Sistema]++;
                }
            });

            this.organAvailabilityChartSeries[0].data = [
                availabilityCounts.Disponible,
                availabilityCounts.No_Disponible,
                availabilityCounts.Reservado,
            ];

            this.organSystemChartSeries[0].data = [
                systemCounts.Circulatorio,
                systemCounts.Digestivo,
                systemCounts.Respiratorio,
                systemCounts.Nervioso,
                systemCounts.Muscular,
                systemCounts.Esquelético,
                systemCounts.Endocrino,
                systemCounts.Linfático,
                systemCounts.Inmunológico,
                systemCounts.Reproductor,
                systemCounts.Urinario,
                systemCounts.Sensorial,
            ];

        } catch (error) {
            // console.error('Error al obtener solicitudes:', error);
            console.error('Error al obtener órganos:', error);
        }
    },
};
</script>