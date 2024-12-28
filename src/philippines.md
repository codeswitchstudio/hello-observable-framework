# Health and Wealth RP

```js
import { FileAttachment } from "observablehq:stdlib";

const rplife = await FileAttachment("./data/rplife02.csv").csv({ typed: true });

display(rplife);
```
