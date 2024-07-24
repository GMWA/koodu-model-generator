import { ISelectOption } from '../interfaces';

export const attributTypes: ISelectOption[] = [
  { label: 'String', value: 'str' },
  { label: 'Integer', value: 'int' },
  { label: 'Decimal', value: 'float' },
  { label: 'Boolean', value: 'bool' },
  { label: 'DateTime', value: 'datetime' },
  { label: 'Time', value: 'time' },
  { label: 'Date', value: 'date' },
  { label: 'Reference', value: 'ref' },
];

export const attributWithoutSize: string[] = ['bool', 'datetime', 'time', 'date', 'ref'];
