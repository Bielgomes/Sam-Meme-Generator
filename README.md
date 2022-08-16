
# SAM MEME GENERETOR
<img src="https://i.imgur.com/N8ELvIL.gif">
Sam meme generator é api simples para a geração de memes no estilo da sam (South America Memes).

## Funcionalidades
- Gerar memes customizados;
- Permiti o Download dos mesmos.

## Tecnologias Utilizadas
- Flask
- Pillow

## Links
<a href="https://www.figma.com/file/0n0zDN7zbzhRbaEO74Xesx/ToDo-List/duplicate">Design</a>

## DOCUMENTAÇÃO

### Retorna um meme

#### GET /api/v1/generator?base=${base}&logo=${logo}&logo_pos=${logo_pos}&text=${text}&meme_quality=${meme_quality}&logo_opacity=${logo_opacity}

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `base`      | `string` | **Obrigatório**. Nome da base a ser utilizada |

#### Nome das bases:
```
10_10
bolsonaro
diabo
irineu
nazare_confusa
pensando
ronaldinho
vin_diesel
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `logo`      | `string` | **Obrigatório**. Nome da logo da Sam a ser utilizada |

#### Nome das logos:
```
logo_sam_1
logo_sam_2
logo_sam_3
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `logo_pos`      | `string` | **Obrigatório**. Posição da Logo |

#### Posições da Logo
```
top_left
top_right
bottom_left
bottom_right
center
random
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `text`      | `string` | **Obrigatório**. Texto do meme |

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `meme_quality`      | `int` | **Obrigatório**. Qualidade da imagem a ser gerada |

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `logo_opacity`      | `int` | **Obrigatório**. Opacidade da logo |

#### Meme_quality e logo_opacity tem 100 como máximo.

### Download do meme

#### GET /api/v1/generator/download?....
