interface IAttributType{
  name: string;
  value: string
}

export const attributTypes: IAttributType[] = [
  {name: "String", value: "str"},
  {name: "Integer", value: "int"},
  {name: "Decimal", value: "float"},
  {name: "Boolean", value: "bool"},
  {name: "DateTime", value: "datetime"},
  {name: "Time", value: "time"},
  {name: "Date", value: "date"},
  {name: "Reference", value: "ref"}
]
