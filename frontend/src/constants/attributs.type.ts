interface IAttributType{
  name: string;
  value: string
}

export const attributTypes: IAttributType[] = [
  {name: "String", value: "str"},
  {name: "Integer", value: "int"},
  {name: "Decimal", value: "float"},
  {name: "Boolean", value: "bool"},
  {name: "Reference", value: "ref"}
]
