import { question } from 'readline-sync'

function main(){
  const nome = question('Qual seu nome? ')
  const qtd = Number(question('Quantas vezes? '))
  
  // C-Like For, For de 3 Expressões, For Clássico, For Antigo
  for (let i = 0; i < qtd; i += 1){
    console.log(` ${i} > ${nome}`)
  }

}


main()