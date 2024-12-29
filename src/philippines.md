# Philippines Health and Wealth (or lack of it) Index

```js
import { FileAttachment } from "observablehq:stdlib";

const rplife = await FileAttachment("./data/rplife.csv").csv({ typed: true });

display(rplife);
```

<!-- <div class="grid grid-cols-2" style="grid-auto-rows: 504px;"> -->
<div class="grid " style="grid-auto-rows: 504px;">

  <div class="card">${
    resize((width) => Plot.plot({
      title: "Life Expectancy",
      subtitle: "based on records",
      width,
      y: { grid: true, label: "Age (years)" },
      x: { label: "Year" },
      marks: [
        Plot.line(
      rplife.map(d => ({ year: new Date(d.year, 0), age: d.age })),
      { x: "year", y: "age", stroke: "steelblue" }
    )
      ]
    }))
  }</div>

  <!-- <div class="card">
  ${
    resize((width) => Plot.plot(
    {
      title: "How big are penguins, anyway? 🐧",
      width,
      grid: true,
      x: {label: "Body mass (g)"},
      y: {label: "Flipper length (mm)"},
      color: {legend: true},
      marks: 
      [
        Plot.linearRegressionY(penguins, {x: "body_mass_g", y: "flipper_length_mm", stroke: "species"}),
        Plot.dot(penguins, {x: "body_mass_g", y: "flipper_length_mm", stroke: "species", tip: true})
      ]
    }))
   }
  </div> -->
</div>
