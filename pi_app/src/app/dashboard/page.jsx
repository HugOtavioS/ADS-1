"use client"

import { useEffect, useState } from "react"
import axios from "axios";

import { AppSidebar } from "@/components/app-sidebar"
import { Separator } from "@/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import { Database } from "lucide-react"
import { Label, Pie, PieChart, Sector } from "recharts"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart"

import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

const chartData = [
  { browser: "Azul", visitors: 275, fill: "#344BFD" },
  { browser: "Verde", visitors: 200, fill: "#2BC84D" },
  { browser: "Vermelho", visitors: 187, fill: "#B10300" },
  { browser: "Amarelo", visitors: 173, fill: "#FFCC00" },
]
const chartConfig = {
  visitors: {
    label: "Visitors",
  },
  Azul: {
    label: "Azul",
    color: "hsl(var(--chart-1))",
  },
  Verde: {
    label: "Verde",
    color: "hsl(var(--chart-2))",
  },
  Vermelho: {
    label: "Vermelho",
    color: "hsl(var(--chart-3))",
  },
  Amarelo: {
    label: "Amarelo",
    color: "hsl(var(--chart-4))",
  },
}

export default function Page() {

  const [contacts, setContacts] = useState([]);
  // Função para adicionar um contato (dados de exemplo)
  const addContact = async () => {
    try {
      const newContact = {
        id_Cor: Math.floor(Math.random() * 4) + 1, // Gera um valor entre 1 e 4
        id_Tamanho: Math.floor(Math.random() * 3) + 1, // Gera um valor entre 1 e 3
        id_Material: Math.floor(Math.random() * 2) + 1, // Gera um valor entre 1 e 2
        // Gera a data e hora atual no formato YYYY-MM-DD HH:MM:SS
        Data_hora: new Date().toISOString().replace('T', ' ').substring(0, 19),
      };
      const response = await axios.post("http://localhost:8080/addpeca", newContact, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.log(response.data)
    } catch (error) {
      console.error("Erro ao adicionar contato:", error);
    }
  };

  // Função para buscar os contatos
  const fetchContacts = async () => {
    try {
      const response = await axios.get("http://localhost:8080/getpecas");
      console.log(response.data);
      setContacts(response.data);
    } catch (error) {
      console.error("Erro ao buscar contatos:", error);
    }
  };

  // Intervalo para adicionar um contato a cada 0.5 segundos
  // useEffect(() => {
  //   const addInterval = setInterval(() => {
  //     addContact();
  //   }, 1000);
  //   return () => clearInterval(addInterval);
  // }, []);

  // Intervalo para buscar os contatos a cada 1 segundo
  useEffect(() => {
    fetchContacts();
    const fetchInterval = setInterval(() => {
      fetchContacts();
    }, 1000);
    return () => clearInterval(fetchInterval);
  }, []);

  return (
    <>
    <header className="">
      <SidebarProvider>
        <AppSidebar />
        <SidebarInset>
          <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
            <SidebarTrigger className="-ml-1" />
            <Separator orientation="vertical" className="mr-2 data-[orientation=vertical]:h-4" />
          </header>

          <main className= "w-full h-full px-12">
            <div className="chart-1 flex flex-col gap-16 justify-center w-full h-max">

              <div className="flex justify-center gap-8 w-full">
                <Card className="flex flex-col gap-4 w-full max-w-[350px]">
                  <CardHeader className="items-center pb-0">
                    <CardTitle className="text-center text-[20px]">Quantidade Total de Peças</CardTitle>
                    <CardDescription className="text-center"></CardDescription>
                  </CardHeader>
                  <CardContent className="relative flex items-center text-[32px] font-semibold text-center bg-[#4D648D] py-8 rounded-lg text-white">
                    <div className="absolute flex justify-left w-full">
                      <Database color="#FFFFFF" size={40} className="w-max" />
                    </div>
                    <span className="w-full">60</span>
                  </CardContent>
                  <CardFooter className="grid grid-cols-2 grid-rows-2 gap-2 text-sm">
                  </CardFooter>
                </Card>
              </div>

              <div className="line-1 flex justify-center gap-8 w-full">

                <Card className="flex flex-col w-full max-w-[350px] bg-[#B6CCD8]">
                  <CardHeader className="items-center pb-0">
                    <CardTitle className="text-center">Quantidade de Peças por cor</CardTitle>
                    <CardDescription className="text-center">January - June 2024</CardDescription>
                  </CardHeader>
                  <CardContent className="flex-1 pb-0">
                    <ChartContainer
                      config={chartConfig}
                      className="mx-auto aspect-square max-h-[250px]"
                    >
                      <PieChart>
                        <ChartTooltip
                          cursor={false}
                          content={<ChartTooltipContent hideLabel />}
                        />
                        <Pie
                          data={chartData}
                          dataKey="visitors"
                          nameKey="browser"
                          innerRadius={50}
                          strokeWidth={5}
                          activeIndex={0}
                          activeShape={({
                            outerRadius = 0,
                            ...props
                          }) => (
                            <Sector {...props} outerRadius={outerRadius + 10} />
                          )}
                        />
                      </PieChart>
                    </ChartContainer>
                  </CardContent>
                  <CardFooter className="grid grid-cols-2 grid-rows-2 gap-2 text-sm">
                    <div className="flex items-center gap-2 font-medium leading-none">
                      <div className="h-4 w-4 bg-red-600 rounded-full"></div> Vermelho
                    </div>
                    <div className="flex items-center gap-2 font-medium leading-none">
                      <div className="h-4 w-4 bg-green-500 rounded-full"></div> Verde
                    </div>
                    <div className="flex items-center gap-2 font-medium leading-none">
                      <div className="h-4 w-4 bg-blue-600 rounded-full"></div> Azul
                    </div>
                    <div className="flex items-center gap-2 font-medium leading-none">
                      <div className="h-4 w-4 bg-yellow-400 rounded-full"></div> Amarelo
                    </div>
                  </CardFooter>
                </Card>

                <div className="flex justify-center max-w-[732px] min-w-[732px]">
                  <div className="flex flex-wrap justify-center gap-8 w-full">
                    <Card className="relative flex flex-col items-center w-[350px] h-[200px] bg-[#B6CCD8]">
                      <div className="absolute top-0 left-0 w-1/8 h-full bg-[#344BFD] rounded-s-xl"></div>
                      <CardHeader className="items-center w-3/5">
                        <CardTitle className="text-center">Peças por Segundo <hr className="border-[#A9B1BA] my-1"></hr> Azul</CardTitle>
                      </CardHeader>

                      <CardContent className="flex  w-full h-full pb-0 p-0">
                        <span className="m-auto text-[36px]">15</span>
                      </CardContent>
                    </Card>
                    
                    <Card className="relative flex flex-col items-center w-[350px] h-[200px] bg-[#B6CCD8]">
                      <div className="absolute top-0 left-0 w-1/8 h-full bg-[#2BC84D] rounded-s-xl"></div>
                      <CardHeader className="items-center w-3/5">
                        <CardTitle className="text-center">Peças por Segundo <hr className="border-[#A9B1BA] my-1"></hr> Verde</CardTitle>
                      </CardHeader>

                      <CardContent className="flex  w-full h-full pb-0 p-0">
                        <span className="m-auto text-[36px]">15</span>
                      </CardContent>
                    </Card>
                    
                    <Card className="relative flex flex-col items-center w-[350px] h-[200px] bg-[#B6CCD8]">
                      <div className="absolute top-0 left-0 w-1/8 h-full bg-[#B10300] rounded-s-xl"></div>
                      <CardHeader className="items-center w-3/5">
                        <CardTitle className="text-center">Peças por Segundo <hr className="border-[#A9B1BA] my-1"></hr> Vermelho</CardTitle>
                      </CardHeader>

                      <CardContent className="flex  w-full h-full pb-0 p-0">
                        <span className="m-auto text-[36px]">15</span>
                      </CardContent>
                    </Card>
                    
                    <Card className="relative flex flex-col items-center w-[350px] h-[200px] bg-[#B6CCD8]">
                      <div className="absolute top-0 left-0 w-1/8 h-full bg-[#FFCC00] rounded-s-xl"></div>
                      <CardHeader className="items-center w-3/5">
                        <CardTitle className="text-center">Peças por Segundo <hr className="border-[#A9B1BA] my-1"></hr> Amarelo</CardTitle>
                      </CardHeader>

                      <CardContent className="flex  w-full h-full pb-0 p-0">
                        <span className="m-auto text-[36px]">15</span>
                      </CardContent>
                    </Card>
                  </div>
                </div>

              </div>

              <div className="grid grid-cols-3 gap-8 w-full">
                <div className="w-full bg-[#B6CCD8] rounded-lg">
                  {/* <div className="w-full h-[48px] bg-[#B10300] rounded-t-xl"></div> */}
                  <div className="w-full p-4 rounded-lg">
                    {/* <h1 className="text-center text-[24px] font-semibold py-4">Vermelho</h1> */}
                    <div className="flex justify-center items-center gap-2 py-4 w-max mx-auto">
                      <Database color="#344BFD" size={40} className="" />
                      <span className="text-[20px]">15</span>
                    </div>
                    <Table>
                      <TableCaption>Tamanho, quantidade total e por material</TableCaption>
                      <TableHeader>
                        <TableRow>
                          <TableHead className="">Tamanho</TableHead>
                          <TableHead className="">Material</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        <TableRow>
                          <TableCell className="font-medium">P</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">M</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">G</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                      </TableBody>
                    </Table>
                  </div>  
                </div>
                
                <div className="w-full bg-[#B6CCD8] rounded-lg">
                  {/* <div className="w-full h-[48px] bg-[#B10300] rounded-t-xl"></div> */}
                  <div className="w-full p-4 rounded-lg">
                    {/* <h1 className="text-center text-[24px] font-semibold py-4">Vermelho</h1> */}
                    <div className="flex justify-center items-center gap-2 py-4 w-max mx-auto">
                      <Database color="#2BC84D" size={40} className="" />
                      <span className="text-[20px]">15</span>
                    </div>
                    <Table>
                      <TableCaption>Tamanho, quantidade total e por material</TableCaption>
                      <TableHeader>
                        <TableRow>
                          <TableHead className="">Tamanho</TableHead>
                          <TableHead className="">Material</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        <TableRow>
                          <TableCell className="font-medium">P</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">M</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">G</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                      </TableBody>
                    </Table>
                  </div>
                </div>

                <div className="w-full bg-[#B6CCD8] rounded-lg">
                  {/* <div className="w-full h-[48px] bg-[#B10300] rounded-t-xl"></div> */}
                  <div className="w-full p-4 rounded-lg">
                    {/* <h1 className="text-center text-[24px] font-semibold py-4">Vermelho</h1> */}
                    <div className="flex justify-center items-center gap-2 py-4 w-max mx-auto">
                      <Database color="#B10300" size={40} className="" />
                      <span className="text-[20px]">15</span>
                    </div>
                    <Table>
                      <TableCaption>Tamanho, quantidade total e por material</TableCaption>
                      <TableHeader>
                        <TableRow>
                          <TableHead className="">Tamanho</TableHead>
                          <TableHead className="">Material</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        <TableRow>
                          <TableCell className="font-medium">P</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">M</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">G</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                      </TableBody>
                    </Table>
                  </div>
                </div>

                <div className="w-full bg-[#B6CCD8] rounded-lg">
                  {/* <div className="w-full h-[48px] bg-[#B10300] rounded-t-xl"></div> */}
                  <div className="w-full p-4 rounded-lg">
                    {/* <h1 className="text-center text-[24px] font-semibold py-4">Vermelho</h1> */}
                    <div className="flex justify-center items-center gap-2 py-4 w-max mx-auto">
                      <Database color="#FFCC00" size={40} className="" />
                      <span className="text-[20px]">15</span>
                    </div>
                    <Table>
                      <TableCaption>Tamanho, quantidade total e por material</TableCaption>
                      <TableHeader>
                        <TableRow>
                          <TableHead className="">Tamanho</TableHead>
                          <TableHead className="">Material</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        <TableRow>
                          <TableCell className="font-medium">P</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">M</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                        <TableRow>
                          <TableCell className="font-medium">G</TableCell>
                          <Table>
                            <TableBody>
                              <TableRow>
                                <TableCell className="font-medium">Aço</TableCell>
                                <TableCell className="font-medium">7</TableCell>
                              </TableRow>
                              <TableRow>
                                <TableCell className="font-medium">Plástico</TableCell>
                                <TableCell className="font-medium">8</TableCell>
                              </TableRow>
                            </TableBody>
                          </Table>
                        </TableRow>
                      </TableBody>
                    </Table>
                  </div>
                </div>
              </div>

            </div>
          </main>
        </SidebarInset>
      </SidebarProvider>
    </header>
    </>
  );
}
